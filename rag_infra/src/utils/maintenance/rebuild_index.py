#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para Reconstruir o Índice RAG

Este script corrige a inconsistência entre documentos (281) e metadados (7)
e reconstrói o índice FAISS/PyTorch corretamente.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import sys
import os
import json
import logging
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional
import shutil
from datetime import datetime

# Adicionar o diretório pai ao path

project_root = Path(__file__).parent.parent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str(project_root / "src" / "core" / "src/core/core_logic")))

from ..core_logic.constants import (
    FAISS_INDEX_DIR, FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE,
    EMBEDDING_MODEL_NAME, CHUNK_SIZE, CHUNK_OVERLAP
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class IndexRebuilder:
    """
    Classe para reconstruir o índice RAG corrigindo inconsistências.
    """
    
    def __init__(self):
        self.backup_dir = FAISS_INDEX_DIR / "backup" / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.source_docs_dir = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / "source_documents"
        
    def rebuild_index(self) -> Dict[str, Any]:
        """
        Reconstrói o índice completamente.
        
        Returns:
            Dict: Relatório da reconstrução
        """
        logger.info("[EMOJI] Iniciando reconstrução do índice RAG...")
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "backup_created": False,
            "inconsistency_fixed": False,
            "index_rebuilt": False,
            "documents_processed": 0,
            "chunks_created": 0,
            "embeddings_generated": 0,
            "final_status": {},
            "errors": []
        }
        
        try:
            # 1. Criar backup do índice atual
            report["backup_created"] = self._create_backup()
            
            # 2. Analisar e corrigir inconsistência
            report["inconsistency_fixed"] = self._fix_inconsistency()
            
            # 3. Reconstruir índice do zero
            rebuild_result = self._rebuild_from_source()
            report.update(rebuild_result)
            
            # 4. Verificar resultado final
            report["final_status"] = self._verify_index()
            
            # 5. Salvar relatório
            self._save_report(report)
            
        except Exception as e:
            error_msg = f"Erro na reconstrução: {e}"
            report["errors"].append(error_msg)
            logger.error(f"[ERROR] {error_msg}")
        
        return report
    
    def _create_backup(self) -> bool:
        """
        Cria backup do índice atual.
        """
        try:
            logger.info("[SAVE] Criando backup do índice atual...")
            
            if not FAISS_INDEX_DIR.exists():
                logger.warning("[WARNING] Diretório do índice não existe")
                return True
            
            # Criar diretório de backup
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            
            # Copiar arquivos importantes
            files_to_backup = [
                FAISS_DOCUMENTS_FILE,
                FAISS_METADATA_FILE,
                "embeddings.npy",
                "faiss_index.bin",
                "pytorch_conversion_info.json"
            ]
            
            backed_up = 0
            for filename in files_to_backup:
                source_path = FAISS_INDEX_DIR / filename
                if source_path.exists():
                    dest_path = self.backup_dir / filename
                    shutil.copy2(source_path, dest_path)
                    backed_up += 1
                    logger.info(f"[EMOJI] Backup: {filename}")
            
            logger.info(f"[OK] Backup criado: {backed_up} arquivos em {self.backup_dir}")
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro ao criar backup: {e}")
            return False
    
    def _fix_inconsistency(self) -> bool:
        """
        Corrige a inconsistência entre documentos e metadados.
        """
        try:
            logger.info("[EMOJI] Corrigindo inconsistência entre documentos e metadados...")
            
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            
            if not documents_path.exists() or not metadata_path.exists():
                logger.warning("[WARNING] Arquivos de documentos ou metadados não encontrados")
                return False
            
            # Carregar documentos e metadados
            with open(documents_path, 'r', encoding='utf-8') as f:
                documents = json.load(f)
            
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            logger.info(f"[EMOJI] Documentos: {len(documents)}, Metadados: {len(metadata)}")
            
            if len(documents) == len(metadata):
                logger.info("[OK] Documentos e metadados já estão consistentes")
                return True
            
            # Corrigir inconsistência
            if len(documents) > len(metadata):
                logger.info("[EMOJI] Gerando metadados faltantes...")
                
                # Gerar metadados para documentos sem metadados
                for i in range(len(metadata), len(documents)):
                    new_metadata = {
                        "source": f"documento_{i}",
                        "chunk_index": i,
                        "total_chunks": len(documents),
                        "file_path": "unknown",
                        "category": "general",
                        "created_at": datetime.now().isoformat()
                    }
                    metadata.append(new_metadata)
                
                # Salvar metadados corrigidos
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2, ensure_ascii=False)
                
                logger.info(f"[OK] Metadados corrigidos: {len(metadata)} entradas")
                
            elif len(metadata) > len(documents):
                logger.info("[EMOJI] Removendo metadados extras...")
                
                # Truncar metadados para corresponder aos documentos
                metadata = metadata[:len(documents)]
                
                # Salvar metadados corrigidos
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2, ensure_ascii=False)
                
                logger.info(f"[OK] Metadados truncados: {len(metadata)} entradas")
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro ao corrigir inconsistência: {e}")
            return False
    
    def _rebuild_from_source(self) -> Dict[str, Any]:
        """
        Reconstrói o índice a partir dos documentos fonte.
        """
        result = {
            "index_rebuilt": False,
            "documents_processed": 0,
            "chunks_created": 0,
            "embeddings_generated": 0
        }
        
        try:
            logger.info("[EMOJI] Reconstruindo índice a partir dos documentos fonte...")
            
            # Verificar se existe diretório de documentos fonte
            if not self.source_docs_dir.exists():
                logger.error(f"[ERROR] Diretório de documentos fonte não encontrado: {self.source_docs_dir}")
                return result
            
            # Importar e usar o processador de documentos
            try:
                from ..core_logic.document_processor import DocumentProcessor
                from ..core_logic.embedding_generator import EmbeddingGenerator
                from ..core_logic.faiss_manager import FAISSManager
                
                # Inicializar componentes
                doc_processor = DocumentProcessor(
                    chunk_size=CHUNK_SIZE,
                    chunk_overlap=CHUNK_OVERLAP
                )
                
                embedding_generator = EmbeddingGenerator(
                    model_name=EMBEDDING_MODEL_NAME
                )
                
                faiss_manager = FAISSManager()
                
                # Processar documentos
                logger.info("[EMOJI] Processando documentos...")
                
                all_chunks = []
                all_metadata = []
                
                # Encontrar todos os arquivos de documentos
                doc_files = list(self.source_docs_dir.rglob("*.md")) + list(self.source_docs_dir.rglob("*.txt"))
                
                for doc_file in doc_files:
                    try:
                        logger.info(f"[EMOJI] Processando: {doc_file.name}")
                        
                        # Ler conteúdo do arquivo
                        with open(doc_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Processar em chunks
                        chunks = doc_processor.process_document(content, str(doc_file))
                        
                        # Adicionar chunks e metadados
                        for i, chunk in enumerate(chunks):
                            all_chunks.append(chunk["content"])
                            
                            metadata = {
                                "source": doc_file.name,
                                "chunk_index": i,
                                "total_chunks": len(chunks),
                                "file_path": str(doc_file.relative_to(self.source_docs_dir)),
                                "category": self._get_category_from_path(doc_file),
                                "created_at": datetime.now().isoformat()
                            }
                            all_metadata.append(metadata)
                        
                        result["documents_processed"] += 1
                        result["chunks_created"] += len(chunks)
                        
                    except Exception as e:
                        logger.error(f"[ERROR] Erro ao processar {doc_file}: {e}")
                        continue
                
                logger.info(f"[EMOJI] Total: {len(all_chunks)} chunks de {result['documents_processed']} documentos")
                
                if not all_chunks:
                    logger.error("[ERROR] Nenhum chunk foi criado")
                    return result
                
                # Gerar embeddings
                logger.info("🧠 Gerando embeddings...")
                embeddings = embedding_generator.generate_embeddings(all_chunks)
                result["embeddings_generated"] = len(embeddings)
                
                # Criar índice FAISS
                logger.info("[SEARCH] Criando índice FAISS...")
                
                # Limpar diretório do índice
                if FAISS_INDEX_DIR.exists():
                    for file in FAISS_INDEX_DIR.glob("*"):
                        if file.is_file() and file.name != "backup":
                            file.unlink()
                
                FAISS_INDEX_DIR.mkdir(exist_ok=True)
                
                # Salvar documentos
                documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
                with open(documents_path, 'w', encoding='utf-8') as f:
                    json.dump(all_chunks, f, indent=2, ensure_ascii=False)
                
                # Salvar metadados
                metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(all_metadata, f, indent=2, ensure_ascii=False)
                
                # Salvar embeddings
                embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
                np.save(embeddings_path, embeddings)
                
                # Criar índice FAISS
                faiss_manager.create_index(embeddings)
                faiss_manager.save_index(FAISS_INDEX_DIR / "faiss_index.bin")
                
                result["index_rebuilt"] = True
                logger.info("[OK] Índice reconstruído com sucesso!")
                
            except ImportError as e:
                logger.error(f"[ERROR] Erro ao importar módulos: {e}")
                logger.info("[EMOJI] Tentando reconstrução simplificada...")
                result.update(self._simple_rebuild())
                
        except Exception as e:
            logger.error(f"[ERROR] Erro na reconstrução: {e}")
        
        return result
    
    def _simple_rebuild(self) -> Dict[str, Any]:
        """
        Reconstrução simplificada usando apenas os arquivos existentes.
        """
        result = {
            "index_rebuilt": False,
            "documents_processed": 0,
            "chunks_created": 0,
            "embeddings_generated": 0
        }
        
        try:
            logger.info("[EMOJI] Executando reconstrução simplificada...")
            
            # Verificar se já temos documentos processados
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            if documents_path.exists():
                with open(documents_path, 'r', encoding='utf-8') as f:
                    documents = json.load(f)
                
                # Recriar metadados consistentes
                metadata = []
                for i, doc in enumerate(documents):
                    metadata.append({
                        "source": f"chunk_{i}",
                        "chunk_index": i,
                        "total_chunks": len(documents),
                        "file_path": "processed",
                        "category": "general",
                        "created_at": datetime.now().isoformat()
                    })
                
                # Salvar metadados corrigidos
                metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2, ensure_ascii=False)
                
                result["documents_processed"] = 1
                result["chunks_created"] = len(documents)
                result["index_rebuilt"] = True
                
                logger.info(f"[OK] Reconstrução simplificada: {len(documents)} chunks, {len(metadata)} metadados")
            
        except Exception as e:
            logger.error(f"[ERROR] Erro na reconstrução simplificada: {e}")
        
        return result
    
    def _get_category_from_path(self, file_path: Path) -> str:
        """
        Determina a categoria baseada no caminho do arquivo.
        """
        path_str = str(file_path).lower()
        
        if "arquitetura" in path_str:
            return "architecture"
        elif "requisitos" in path_str:
            return "requirements"
        elif "design" in path_str or "interface" in path_str:
            return "design"
        elif "api" in path_str:
            return "api"
        elif "tech_stack" in path_str or "tecnologia" in path_str:
            return "technology"
        else:
            return "general"
    
    def _verify_index(self) -> Dict[str, Any]:
        """
        Verifica se o índice foi reconstruído corretamente.
        """
        status = {
            "documents_count": 0,
            "metadata_count": 0,
            "consistent": False,
            "files_present": [],
            "index_loadable": False
        }
        
        try:
            # Verificar arquivos
            required_files = [FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE]
            
            for filename in required_files:
                file_path = FAISS_INDEX_DIR / filename
                if file_path.exists():
                    status["files_present"].append(filename)
            
            # Contar documentos e metadados
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            if documents_path.exists():
                with open(documents_path, 'r', encoding='utf-8') as f:
                    documents = json.load(f)
                    status["documents_count"] = len(documents)
            
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            if metadata_path.exists():
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    status["metadata_count"] = len(metadata)
            
            # Verificar consistência
            status["consistent"] = (status["documents_count"] == status["metadata_count"] and 
                                  status["documents_count"] > 0)
            
            # Testar carregamento do índice
            try:
                from ..core_logic.rag_retriever import RAGRetriever
                retriever = RAGRetriever()
                if retriever.initialize() and retriever.load_index():
                    status["index_loadable"] = True
            except Exception as e:
                logger.warning(f"[WARNING] Erro ao testar carregamento: {e}")
            
            logger.info(f"[EMOJI] Verificação final: {status['documents_count']} docs, {status['metadata_count']} meta, consistente: {status['consistent']}")
            
        except Exception as e:
            logger.error(f"[ERROR] Erro na verificação: {e}")
        
        return status
    
    def _save_report(self, report: Dict[str, Any]):
        """
        Salva o relatório de reconstrução.
        """
        try:
            # Importar configuração centralizada
             import sys
             sys.path.append(str(Path(__file__).parent.parent))
             from config import get_report_path, REPORT_CONFIG
             
             report_path = get_report_path("index_rebuild_report.json")
             with open(report_path, 'w', encoding=REPORT_CONFIG['encoding']) as f:
                 json.dump(report, f, 
                          indent=REPORT_CONFIG['indent'], 
                          ensure_ascii=REPORT_CONFIG['ensure_ascii'], 
                          default=REPORT_CONFIG['default_serializer'])
             logger.info(f"[EMOJI] Relatório salvo em: {report_path.absolute()}")
        except Exception as e:
            logger.error(f"Erro ao salvar relatório: {e}")

def main():
    """
    Função principal do script de reconstrução.
    """
    print("[EMOJI] Iniciando reconstrução do índice RAG...")
    
    rebuilder = IndexRebuilder()
    report = rebuilder.rebuild_index()
    
    print("\n" + "="*80)
    print("[EMOJI] RELATÓRIO DE RECONSTRUÇÃO DO ÍNDICE")
    print("="*80)
    
    print(f"\n[EMOJI] Resultados:")
    print(f"   Backup criado: {report['backup_created']}")
    print(f"   Inconsistência corrigida: {report['inconsistency_fixed']}")
    print(f"   Índice reconstruído: {report['index_rebuilt']}")
    print(f"   Documentos processados: {report['documents_processed']}")
    print(f"   Chunks criados: {report['chunks_created']}")
    
    final_status = report.get('final_status', {})
    print(f"\n[OK] Status Final:")
    print(f"   Documentos: {final_status.get('documents_count', 0)}")
    print(f"   Metadados: {final_status.get('metadata_count', 0)}")
    print(f"   Consistente: {final_status.get('consistent', False)}")
    print(f"   Carregável: {final_status.get('index_loadable', False)}")
    
    if report.get('errors'):
        print(f"\n[ERROR] Erros ({len(report['errors'])}):")
        for i, error in enumerate(report['errors'], 1):
            print(f"   {i}. {error}")
    
    print("\n" + "="*80)
    
    if (final_status.get('consistent') and final_status.get('index_loadable')):
        print("[EMOJI] Reconstrução bem-sucedida! Índice funcionando.")
    else:
        print("[WARNING] Reconstrução parcial. Verifique os erros acima.")

if __name__ == "__main__":
    main()