# -*- coding: utf-8 -*-
"""
Sistema de Manutenção RAG - Recoloca.ai

Este script consolida funcionalidades de manutenção do sistema RAG:
- Criação e verificação de diretórios
- Debug de caminhos e configurações
- Limpeza de cache e arquivos temporários
- Verificação de integridade do sistema

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import os
import sys
import json
import logging
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Adicionar path do projeto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ..core.constants import (
        FAISS_INDEX_DIR, FAISS_INDEX_FILE, SOURCE_DOCUMENTS_DIR,
        PYTORCH_INDEX_DIR, LOGS_DIR, CACHE_DIR, METRICS_DIR
    )
except ImportError:
    logger.warning("Não foi possível importar constantes. Usando valores padrão.")
    FAISS_INDEX_DIR = Path('data_index/faiss_index_bge_m3')
    FAISS_INDEX_FILE = 'index.faiss'
    SOURCE_DOCUMENTS_DIR = Path('source_documents')
    PYTORCH_INDEX_DIR = Path('data_index/pytorch_index_bge_m3')
    LOGS_DIR = Path('logs')
    CACHE_DIR = Path('cache')
    METRICS_DIR = Path('metrics')

class RAGMaintenance:
    """
    Classe para manutenção e verificação do sistema RAG.
    """
    
    def __init__(self):
        self.required_dirs = [
            FAISS_INDEX_DIR,
            PYTORCH_INDEX_DIR,
            SOURCE_DOCUMENTS_DIR,
            LOGS_DIR,
            CACHE_DIR,
            METRICS_DIR
        ]
        
    def create_directories(self) -> Dict[str, Any]:
        """
        Cria todos os diretórios necessários para o sistema RAG.
        
        Returns:
            Dict com status da criação dos diretórios
        """
        logger.info("Criando diretórios necessários...")
        results = {}
        
        for directory in self.required_dirs:
            try:
                directory.mkdir(parents=True, exist_ok=True)
                results[str(directory)] = {
                    'status': 'success',
                    'exists': directory.exists(),
                    'absolute_path': str(directory.absolute())
                }
                logger.info(f"[OK] Diretório criado/verificado: {directory}")
            except Exception as e:
                results[str(directory)] = {
                    'status': 'error',
                    'error': str(e),
                    'exists': False
                }
                logger.error(f"[ERROR] Erro ao criar diretório {directory}: {e}")
                
        return results
    
    def debug_paths(self) -> Dict[str, Any]:
        """
        Verifica e debug dos caminhos do sistema.
        
        Returns:
            Dict com informações de debug dos caminhos
        """
        logger.info("Executando debug de caminhos...")
        
        debug_info = {
            'faiss_index_dir': {
                'path': str(FAISS_INDEX_DIR),
                'absolute': str(FAISS_INDEX_DIR.absolute()),
                'exists': FAISS_INDEX_DIR.exists(),
                'is_dir': FAISS_INDEX_DIR.is_dir() if FAISS_INDEX_DIR.exists() else False
            },
            'faiss_index_file': {
                'filename': FAISS_INDEX_FILE,
                'full_path': str(FAISS_INDEX_DIR / FAISS_INDEX_FILE),
                'exists': (FAISS_INDEX_DIR / FAISS_INDEX_FILE).exists()
            },
            'source_documents': {
                'path': str(SOURCE_DOCUMENTS_DIR),
                'exists': SOURCE_DOCUMENTS_DIR.exists(),
                'file_count': len(list(SOURCE_DOCUMENTS_DIR.glob('**/*'))) if SOURCE_DOCUMENTS_DIR.exists() else 0
            }
        }
        
        # Teste de escrita
        try:
            test_file = FAISS_INDEX_DIR / 'test_write.txt'
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write('teste de escrita')
            debug_info['write_test'] = {
                'status': 'success',
                'message': 'Conseguiu escrever arquivo de teste'
            }
            test_file.unlink()  # Remover arquivo de teste
        except Exception as e:
            debug_info['write_test'] = {
                'status': 'error',
                'error': str(e)
            }
            
        return debug_info
    
    def clean_cache(self) -> Dict[str, Any]:
        """
        Limpa arquivos de cache e temporários.
        
        Returns:
            Dict com resultado da limpeza
        """
        logger.info("Limpando cache e arquivos temporários...")
        
        cleaned = {
            'cache_files': 0,
            'temp_files': 0,
            'log_files': 0,
            'backup_files': 0,
            'errors': []
        }
        
        # Padrões de arquivos para limpeza
        patterns_to_clean = [
            '**/*.tmp',
            '**/*.temp',
            '**/*.cache',
            '**/*.backup',
            '**/*.bak',
            '**/.*~',
            '**/__pycache__',
            '**/*.pyc',
            '**/*.pyo'
        ]
        
        # Diretórios para limpeza
        dirs_to_clean = [CACHE_DIR, LOGS_DIR]
        
        for directory in dirs_to_clean:
            if not directory.exists():
                continue
                
            try:
                for pattern in patterns_to_clean:
                    for file_path in directory.glob(pattern):
                        try:
                            if file_path.is_file():
                                file_path.unlink()
                                if 'cache' in pattern:
                                    cleaned['cache_files'] += 1
                                elif 'tmp' in pattern or 'temp' in pattern:
                                    cleaned['temp_files'] += 1
                                elif 'backup' in pattern or 'bak' in pattern:
                                    cleaned['backup_files'] += 1
                                else:
                                    cleaned['temp_files'] += 1
                            elif file_path.is_dir():
                                shutil.rmtree(file_path)
                                cleaned['cache_files'] += 1
                        except Exception as e:
                            cleaned['errors'].append(f"Erro ao remover {file_path}: {e}")
            except Exception as e:
                cleaned['errors'].append(f"Erro ao limpar diretório {directory}: {e}")
        
        # Limpar logs antigos (mais de 7 dias)
        if LOGS_DIR.exists():
            try:
                cutoff_date = datetime.now().timestamp() - (7 * 24 * 60 * 60)  # 7 dias
                for log_file in LOGS_DIR.glob('*.log'):
                    if log_file.stat().st_mtime < cutoff_date:
                        log_file.unlink()
                        cleaned['log_files'] += 1
            except Exception as e:
                cleaned['errors'].append(f"Erro ao limpar logs antigos: {e}")
        
        return cleaned
    
    def verify_system_integrity(self) -> Dict[str, Any]:
        """
        Verifica a integridade do sistema RAG.
        
        Returns:
            Dict com resultado da verificação
        """
        logger.info("Verificando integridade do sistema...")
        
        integrity = {
            'directories': {},
            'files': {},
            'permissions': {},
            'overall_status': 'unknown'
        }
        
        # Verificar diretórios
        for directory in self.required_dirs:
            integrity['directories'][str(directory)] = {
                'exists': directory.exists(),
                'readable': directory.exists() and os.access(directory, os.R_OK),
                'writable': directory.exists() and os.access(directory, os.W_OK)
            }
        
        # Verificar arquivos críticos
        critical_files = [
            FAISS_INDEX_DIR / FAISS_INDEX_FILE,
            FAISS_INDEX_DIR / 'documents.json',
            FAISS_INDEX_DIR / 'metadata.json'
        ]
        
        for file_path in critical_files:
            integrity['files'][str(file_path)] = {
                'exists': file_path.exists(),
                'readable': file_path.exists() and os.access(file_path, os.R_OK),
                'size': file_path.stat().st_size if file_path.exists() else 0
            }
        
        # Determinar status geral
        all_dirs_ok = all(
            info['exists'] and info['readable'] and info['writable']
            for info in integrity['directories'].values()
        )
        
        critical_files_ok = any(
            info['exists'] and info['readable']
            for info in integrity['files'].values()
        )
        
        if all_dirs_ok and critical_files_ok:
            integrity['overall_status'] = 'healthy'
        elif all_dirs_ok:
            integrity['overall_status'] = 'needs_indexing'
        else:
            integrity['overall_status'] = 'critical'
        
        return integrity
    
    def generate_maintenance_report(self) -> Dict[str, Any]:
        """
        Gera relatório completo de manutenção.
        
        Returns:
            Dict com relatório completo
        """
        logger.info("Gerando relatório de manutenção...")
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'directories': self.create_directories(),
            'paths_debug': self.debug_paths(),
            'cache_cleanup': self.clean_cache(),
            'system_integrity': self.verify_system_integrity()
        }
        
        # Salvar relatório
        try:
            report_file = LOGS_DIR / f"maintenance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            LOGS_DIR.mkdir(parents=True, exist_ok=True)
            
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            report['report_saved'] = str(report_file)
            logger.info(f"Relatório salvo em: {report_file}")
        except Exception as e:
            report['report_error'] = str(e)
            logger.error(f"Erro ao salvar relatório: {e}")
        
        return report

def main():
    """
    Função principal para execução do script de manutenção.
    """
    print("[EMOJI] Sistema de Manutenção RAG - Recoloca.ai")
    print("=" * 50)
    
    maintenance = RAGMaintenance()
    
    try:
        # Executar manutenção completa
        report = maintenance.generate_maintenance_report()
        
        # Exibir resumo
        print("\n[EMOJI] Resumo da Manutenção:")
        print(f"- Diretórios verificados: {len(report['directories'])}")
        print(f"- Status do sistema: {report['system_integrity']['overall_status']}")
        print(f"- Arquivos de cache limpos: {report['cache_cleanup']['cache_files']}")
        print(f"- Arquivos temporários limpos: {report['cache_cleanup']['temp_files']}")
        
        if report['cache_cleanup']['errors']:
            print(f"- Erros durante limpeza: {len(report['cache_cleanup']['errors'])}")
        
        if 'report_saved' in report:
            print(f"\n[EMOJI] Relatório completo salvo em: {report['report_saved']}")
        
        print("\n[OK] Manutenção concluída com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro durante manutenção: {e}")
        print(f"\n[ERROR] Erro durante manutenção: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()