#!/usr/bin/env python3

import sys
import os
import json
import numpy as np
import logging
from pathlib import Path

# Adicionar diretórios ao path
sys.path.insert(0, 'core_logic')

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_index_consistency():
    """Verifica a consistência do índice."""
    try:
        index_dir = "data_index/faiss_index_bge_m3"
        
        # Carregar arquivos
        docs_file = os.path.join(index_dir, "documents.json")
        meta_file = os.path.join(index_dir, "metadata.json")
        emb_file = os.path.join(index_dir, "embeddings.npy")
        
        logger.info("Verificando consistência do índice...")
        
        # Carregar documentos
        with open(docs_file, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        logger.info(f"Documentos: {len(documents)}")
        
        # Carregar metadados
        with open(meta_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        docs_metadata = metadata.get("documents_metadata", [])
        logger.info(f"Metadados de documentos: {len(docs_metadata)}")
        
        # Carregar embeddings
        embeddings = np.load(emb_file)
        logger.info(f"Embeddings: shape {embeddings.shape}")
        
        # Verificar consistência
        logger.info("\n=== ANÁLISE DE CONSISTÊNCIA ===")
        logger.info(f"Documentos: {len(documents)}")
        logger.info(f"Metadados: {len(docs_metadata)}")
        logger.info(f"Embeddings: {embeddings.shape[0]}")
        
        # Identificar problemas
        problems = []
        
        if len(documents) != len(docs_metadata):
            problems.append(f"Documentos ({len(documents)}) != Metadados ({len(docs_metadata)})")
            
        if len(documents) != embeddings.shape[0]:
            problems.append(f"Documentos ({len(documents)}) != Embeddings ({embeddings.shape[0]})")
            
        if len(docs_metadata) != embeddings.shape[0]:
            problems.append(f"Metadados ({len(docs_metadata)}) != Embeddings ({embeddings.shape[0]})")
            
        if problems:
            logger.error("\n❌ PROBLEMAS ENCONTRADOS:")
            for problem in problems:
                logger.error(f"  - {problem}")
            return False
        else:
            logger.info("\n✅ ÍNDICE CONSISTENTE")
            return True
            
    except Exception as e:
        logger.error(f"Erro verificando consistência: {e}")
        import traceback
        traceback.print_exc()
        return False

def fix_index_consistency():
    """Corrige a inconsistência truncando para o menor tamanho."""
    try:
        index_dir = "data_index/faiss_index_bge_m3"
        
        # Carregar arquivos
        docs_file = os.path.join(index_dir, "documents.json")
        meta_file = os.path.join(index_dir, "metadata.json")
        emb_file = os.path.join(index_dir, "embeddings.npy")
        
        logger.info("Corrigindo inconsistência...")
        
        # Carregar dados
        with open(docs_file, 'r', encoding='utf-8') as f:
            documents = json.load(f)
            
        with open(meta_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            
        docs_metadata = metadata.get("documents_metadata", [])
        embeddings = np.load(emb_file)
        
        # Encontrar o menor tamanho
        min_size = min(len(documents), len(docs_metadata), embeddings.shape[0])
        logger.info(f"Truncando para {min_size} elementos")
        
        # Truncar dados
        documents_fixed = documents[:min_size]
        docs_metadata_fixed = docs_metadata[:min_size]
        embeddings_fixed = embeddings[:min_size]
        
        # Fazer backup
        backup_dir = os.path.join(index_dir, "backup")
        os.makedirs(backup_dir, exist_ok=True)
        
        import shutil
        shutil.copy2(docs_file, os.path.join(backup_dir, "documents.json.bak"))
        shutil.copy2(meta_file, os.path.join(backup_dir, "metadata.json.bak"))
        shutil.copy2(emb_file, os.path.join(backup_dir, "embeddings.npy.bak"))
        
        logger.info("Backup criado")
        
        # Salvar dados corrigidos
        with open(docs_file, 'w', encoding='utf-8') as f:
            json.dump(documents_fixed, f, ensure_ascii=False, indent=2)
            
        metadata["documents_metadata"] = docs_metadata_fixed
        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
            
        np.save(emb_file, embeddings_fixed)
        
        logger.info("✅ Índice corrigido com sucesso")
        logger.info(f"Novos tamanhos: {len(documents_fixed)} documentos, {len(docs_metadata_fixed)} metadados, {embeddings_fixed.shape[0]} embeddings")
        
        return True
        
    except Exception as e:
        logger.error(f"Erro corrigindo índice: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    logger.info("=== VERIFICAÇÃO DE CONSISTÊNCIA DO ÍNDICE ===")
    
    is_consistent = check_index_consistency()
    
    if not is_consistent:
        logger.info("\n=== CORRIGINDO INCONSISTÊNCIA ===")
        success = fix_index_consistency()
        
        if success:
            logger.info("\n=== VERIFICAÇÃO FINAL ===")
            check_index_consistency()
        else:
            logger.error("Falha ao corrigir índice")
    else:
        logger.info("Índice já está consistente")