#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Sincronização Automática RAG - Recoloca.ai

Este script implementa um sistema de sincronização automática que:
- Monitora mudanças nos documentos fonte
- Executa re-indexação incremental quando necessário
- Mantém logs de sincronização
- Oferece interface para sincronização manual

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import asyncio
import hashlib
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Set, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Adicionar core_logic ao path (subindo um nível da pasta scripts)

project_root = Path(__file__).parent.parent

sys.path.insert(0, str(project_root / "src" / "core" / "src/core/core_logic"))

try:
    from rag_indexer import RAGIndexer
    from rag_retriever import get_retriever, initialize_retriever
except ImportError as e:
    logger.error(f"Erro ao importar módulos RAG: {e}")
    sys.exit(1)

class DocumentChangeHandler(FileSystemEventHandler):
    """Handler para monitorar mudanças nos documentos"""
    
    def __init__(self, sync_manager):
        super().__init__()
        self.sync_manager = sync_manager
        self.last_event_time = {}
        self.debounce_time = 2.0  # 2 segundos de debounce
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Filtrar apenas arquivos relevantes
        if not self._is_relevant_file(file_path):
            return
        
        # Debounce para evitar múltiplos eventos
        current_time = time.time()
        if file_path in self.last_event_time:
            if current_time - self.last_event_time[file_path] < self.debounce_time:
                return
        
        self.last_event_time[file_path] = current_time
        
        logger.info(f"[EMOJI] Documento modificado: {file_path}")
        self.sync_manager.mark_for_sync(file_path)
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        if not self._is_relevant_file(file_path):
            return
        
        logger.info(f"[EMOJI] Novo documento: {file_path}")
        self.sync_manager.mark_for_sync(file_path)
    
    def on_deleted(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        if not self._is_relevant_file(file_path):
            return
        
        logger.info(f"[EMOJI] Documento removido: {file_path}")
        self.sync_manager.mark_for_removal(file_path)
    
    def _is_relevant_file(self, file_path: Path) -> bool:
        """Verifica se o arquivo é relevante para indexação"""
        # Extensões suportadas
        supported_extensions = {'.md', '.txt', '.py', '.js', '.json', '.yaml', '.yml'}
        
        # Verificar extensão
        if file_path.suffix.lower() not in supported_extensions:
            return False
        
        # Ignorar arquivos temporários e de sistema
        if file_path.name.startswith('.') or file_path.name.startswith('~'):
            return False
        
        # Ignorar diretórios específicos
        ignored_dirs = {'__pycache__', '.git', 'node_modules', '.vscode', '.idea'}
        if any(part in ignored_dirs for part in file_path.parts):
            return False
        
        return True

class RAGSyncManager:
    """Gerenciador de sincronização automática do RAG"""
    
    def __init__(self, source_dir: Optional[Path] = None):
        self.source_dir = source_dir or Path(__file__).parent / "source_documents"
        self.sync_state_file = Path(__file__).parent / "sync_state.json"
        self.sync_log_file = Path(__file__).parent / "logs" / "sync.log"
        
        # Estado de sincronização
        self.pending_files: Set[Path] = set()
        self.removed_files: Set[Path] = set()
        self.file_hashes: Dict[str, str] = {}
        self.last_sync_time: Optional[datetime] = None
        
        # Configurações
        self.auto_sync_interval = 300  # 5 minutos
        self.batch_size = 50  # Processar até 50 arquivos por vez
        
        # Componentes RAG
        self.indexer: Optional[RAGIndexer] = None
        self.observer: Optional[Observer] = None
        
        # Carregar estado anterior
        self._load_sync_state()
        
        # Configurar logging para arquivo
        self._setup_file_logging()
    
    def _setup_file_logging(self):
        """Configura logging para arquivo"""
        self.sync_log_file.parent.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler(self.sync_log_file)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        sync_logger = logging.getLogger('rag_sync')
        sync_logger.addHandler(file_handler)
        sync_logger.setLevel(logging.INFO)
        
        self.sync_logger = sync_logger
    
    def _load_sync_state(self):
        """Carrega estado de sincronização anterior"""
        if self.sync_state_file.exists():
            try:
                with open(self.sync_state_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                
                self.file_hashes = state.get('file_hashes', {})
                last_sync_str = state.get('last_sync_time')
                if last_sync_str:
                    self.last_sync_time = datetime.fromisoformat(last_sync_str)
                
                logger.info(f"[EMOJI] Estado de sincronização carregado: {len(self.file_hashes)} arquivos")
                
            except Exception as e:
                logger.error(f"[ERROR] Erro ao carregar estado de sincronização: {e}")
    
    def _save_sync_state(self):
        """Salva estado de sincronização"""
        try:
            state = {
                'file_hashes': self.file_hashes,
                'last_sync_time': self.last_sync_time.isoformat() if self.last_sync_time else None,
                'total_files': len(self.file_hashes)
            }
            
            with open(self.sync_state_file, 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            
        except Exception as e:
            logger.error(f"[ERROR] Erro ao salvar estado de sincronização: {e}")
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calcula hash MD5 de um arquivo"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            logger.error(f"[ERROR] Erro ao calcular hash de {file_path}: {e}")
            return ""
    
    def mark_for_sync(self, file_path: Path):
        """Marca arquivo para sincronização"""
        self.pending_files.add(file_path)
        self.sync_logger.info(f"Arquivo marcado para sincronização: {file_path}")
    
    def mark_for_removal(self, file_path: Path):
        """Marca arquivo para remoção do índice"""
        self.removed_files.add(file_path)
        self.sync_logger.info(f"Arquivo marcado para remoção: {file_path}")
    
    def scan_for_changes(self) -> Dict[str, List[Path]]:
        """Escaneia diretório em busca de mudanças"""
        logger.info(f"[SEARCH] Escaneando mudanças em: {self.source_dir}")
        
        changes = {
            'new': [],
            'modified': [],
            'deleted': []
        }
        
        # Arquivos atuais no diretório
        current_files = set()
        
        for file_path in self.source_dir.rglob('*'):
            if file_path.is_file() and self._is_relevant_file(file_path):
                current_files.add(file_path)
                
                file_str = str(file_path)
                current_hash = self._calculate_file_hash(file_path)
                
                if file_str not in self.file_hashes:
                    # Arquivo novo
                    changes['new'].append(file_path)
                    self.file_hashes[file_str] = current_hash
                elif self.file_hashes[file_str] != current_hash:
                    # Arquivo modificado
                    changes['modified'].append(file_path)
                    self.file_hashes[file_str] = current_hash
        
        # Verificar arquivos deletados
        existing_files = set(Path(f) for f in self.file_hashes.keys())
        deleted_files = existing_files - current_files
        
        for deleted_file in deleted_files:
            changes['deleted'].append(deleted_file)
            del self.file_hashes[str(deleted_file)]
        
        total_changes = sum(len(files) for files in changes.values())
        logger.info(f"[EMOJI] Mudanças encontradas: {total_changes} ({len(changes['new'])} novos, {len(changes['modified'])} modificados, {len(changes['deleted'])} deletados)")
        
        return changes
    
    def _is_relevant_file(self, file_path: Path) -> bool:
        """Verifica se o arquivo é relevante para indexação"""
        supported_extensions = {'.md', '.txt', '.py', '.js', '.json', '.yaml', '.yml'}
        
        if file_path.suffix.lower() not in supported_extensions:
            return False
        
        if file_path.name.startswith('.') or file_path.name.startswith('~'):
            return False
        
        ignored_dirs = {'__pycache__', '.git', 'node_modules', '.vscode', '.idea'}
        if any(part in ignored_dirs for part in file_path.parts):
            return False
        
        return True
    
    async def sync_changes(self, force_full_reindex: bool = False) -> Dict[str, any]:
        """Sincroniza mudanças com o índice RAG"""
        logger.info("[EMOJI] Iniciando sincronização RAG...")
        
        sync_result = {
            'timestamp': datetime.now().isoformat(),
            'success': False,
            'changes_processed': 0,
            'errors': [],
            'duration': 0
        }
        
        start_time = time.time()
        
        try:
            # Inicializar indexer se necessário
            if self.indexer is None:
                self.indexer = RAGIndexer()
            
            if force_full_reindex:
                logger.info("[EMOJI] Executando re-indexação completa...")
                success = self.indexer.index_documents(reindex=True)
                if success:
                    sync_result['changes_processed'] = len(self.file_hashes)
                    sync_result['success'] = True
                    self.sync_logger.info("Re-indexação completa executada com sucesso")
                else:
                    sync_result['errors'].append("Falha na re-indexação completa")
            else:
                # Escanear mudanças
                changes = self.scan_for_changes()
                
                # Processar arquivos pendentes
                all_pending = list(self.pending_files) + changes['new'] + changes['modified']
                all_removed = list(self.removed_files) + changes['deleted']
                
                changes_count = len(all_pending) + len(all_removed)
                
                if changes_count > 0:
                    logger.info(f"[EMOJI] Processando {changes_count} mudanças...")
                    
                    # Para mudanças incrementais, executar re-indexação
                    # (O RAGIndexer atual não suporta indexação incremental)
                    success = self.indexer.index_documents(reindex=True)
                    
                    if success:
                        sync_result['changes_processed'] = changes_count
                        sync_result['success'] = True
                        
                        # Limpar pendências
                        self.pending_files.clear()
                        self.removed_files.clear()
                        
                        self.sync_logger.info(f"Sincronização concluída: {changes_count} mudanças processadas")
                    else:
                        sync_result['errors'].append("Falha na re-indexação")
                else:
                    logger.info("[OK] Nenhuma mudança detectada")
                    sync_result['success'] = True
            
            # Atualizar timestamp
            self.last_sync_time = datetime.now()
            
        except Exception as e:
            error_msg = f"Erro durante sincronização: {e}"
            logger.error(f"[ERROR] {error_msg}")
            sync_result['errors'].append(error_msg)
        
        sync_result['duration'] = time.time() - start_time
        
        # Salvar estado
        self._save_sync_state()
        
        return sync_result
    
    def start_monitoring(self):
        """Inicia monitoramento automático de arquivos"""
        if self.observer is not None:
            logger.warning("[WARNING] Monitoramento já está ativo")
            return
        
        logger.info(f"[EMOJI] Iniciando monitoramento de: {self.source_dir}")
        
        event_handler = DocumentChangeHandler(self)
        self.observer = Observer()
        self.observer.schedule(event_handler, str(self.source_dir), recursive=True)
        self.observer.start()
        
        self.sync_logger.info("Monitoramento de arquivos iniciado")
    
    def stop_monitoring(self):
        """Para monitoramento de arquivos"""
        if self.observer is not None:
            self.observer.stop()
            self.observer.join()
            self.observer = None
            logger.info("[EMOJI] Monitoramento parado")
            self.sync_logger.info("Monitoramento de arquivos parado")
    
    async def run_auto_sync_loop(self):
        """Executa loop de sincronização automática"""
        logger.info(f"[EMOJI] Iniciando loop de sincronização automática (intervalo: {self.auto_sync_interval}s)")
        
        while True:
            try:
                await asyncio.sleep(self.auto_sync_interval)
                
                # Verificar se há mudanças pendentes
                if self.pending_files or self.removed_files:
                    logger.info("[EMOJI] Executando sincronização automática...")
                    result = await self.sync_changes()
                    
                    if result['success']:
                        logger.info(f"[OK] Sincronização automática concluída: {result['changes_processed']} mudanças")
                    else:
                        logger.error(f"[ERROR] Falha na sincronização automática: {result['errors']}")
                
            except asyncio.CancelledError:
                logger.info("[EMOJI] Loop de sincronização cancelado")
                break
            except Exception as e:
                logger.error(f"[ERROR] Erro no loop de sincronização: {e}")
                await asyncio.sleep(60)  # Aguardar 1 minuto antes de tentar novamente
    
    def get_sync_status(self) -> Dict[str, any]:
        """Retorna status atual da sincronização"""
        return {
            'last_sync_time': self.last_sync_time.isoformat() if self.last_sync_time else None,
            'pending_files': len(self.pending_files),
            'removed_files': len(self.removed_files),
            'total_indexed_files': len(self.file_hashes),
            'monitoring_active': self.observer is not None,
            'source_directory': str(self.source_dir)
        }

async def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Sistema de Sincronização Automática RAG')
    parser.add_argument('--mode', choices=['sync', 'monitor', 'status', 'full-reindex'], 
                       default='sync', help='Modo de operação')
    parser.add_argument('--source-dir', type=Path, help='Diretório de documentos fonte')
    parser.add_argument('--auto-sync', action='store_true', help='Ativar sincronização automática')
    
    args = parser.parse_args()
    
    # Criar gerenciador de sincronização
    sync_manager = RAGSyncManager(source_dir=args.source_dir)
    
    try:
        if args.mode == 'status':
            # Mostrar status
            status = sync_manager.get_sync_status()
            print("\n[EMOJI] STATUS DE SINCRONIZAÇÃO RAG")
            print("=" * 40)
            print(f"Última sincronização: {status['last_sync_time'] or 'Nunca'}")
            print(f"Arquivos pendentes: {status['pending_files']}")
            print(f"Arquivos para remoção: {status['removed_files']}")
            print(f"Total de arquivos indexados: {status['total_indexed_files']}")
            print(f"Monitoramento ativo: {'Sim' if status['monitoring_active'] else 'Não'}")
            print(f"Diretório fonte: {status['source_directory']}")
            
        elif args.mode == 'full-reindex':
            # Re-indexação completa
            print("[EMOJI] Executando re-indexação completa...")
            result = await sync_manager.sync_changes(force_full_reindex=True)
            
            if result['success']:
                print(f"[OK] Re-indexação concluída em {result['duration']:.2f}s")
            else:
                print(f"[ERROR] Falha na re-indexação: {result['errors']}")
                
        elif args.mode == 'sync':
            # Sincronização única
            print("[EMOJI] Executando sincronização...")
            result = await sync_manager.sync_changes()
            
            if result['success']:
                print(f"[OK] Sincronização concluída: {result['changes_processed']} mudanças em {result['duration']:.2f}s")
            else:
                print(f"[ERROR] Falha na sincronização: {result['errors']}")
                
        elif args.mode == 'monitor':
            # Modo de monitoramento
            print("[EMOJI] Iniciando monitoramento contínuo...")
            sync_manager.start_monitoring()
            
            if args.auto_sync:
                print("[EMOJI] Sincronização automática ativada")
                # Executar sincronização inicial
                await sync_manager.sync_changes()
                
                # Iniciar loop de sincronização automática
                await sync_manager.run_auto_sync_loop()
            else:
                print("Pressione Ctrl+C para parar o monitoramento")
                try:
                    while True:
                        await asyncio.sleep(1)
                except KeyboardInterrupt:
                    print("\n[EMOJI] Parando monitoramento...")
            
            sync_manager.stop_monitoring()
    
    except KeyboardInterrupt:
        print("\n[EMOJI] Operação cancelada pelo usuário")
    except Exception as e:
        logger.error(f"[ERROR] Erro na execução: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)