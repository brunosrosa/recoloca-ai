#!/usr/bin/env python3

import sys
import os
import logging
import numpy as np

# Adicionar diretórios ao path
sys.path.insert(0, "src/core/core_logic")

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_embedding_model():
    """Testa o modelo de embedding."""
    try:
        from rag_infra.src.core.embedding_model import EmbeddingModelManager
        
        logger.info("Inicializando EmbeddingModelManager...")
        manager = EmbeddingModelManager()
        
        logger.info("Carregando modelo...")
        manager.load_model()
        
        logger.info(f"Modelo carregado: {manager.model_name}")
        logger.info(f"Tipo do modelo: {type(manager.model)}")
        
        # Testar embedding
        test_query = "arquitetura do sistema"
        logger.info(f"Gerando embedding para: '{test_query}'")
        
        embedding = manager.embed_query(test_query)
        
        if embedding is not None:
            logger.info(f"Embedding gerado com sucesso: dimensão {len(embedding)}")
            logger.info(f"Tipo do embedding: {type(embedding)}")
            logger.info(f"Primeiros 5 valores: {embedding[:5]}")
            return True
        else:
            logger.error("Embedding retornou None")
            return False
            
    except Exception as e:
        logger.error(f"Erro durante teste: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_index_files():
    """Verifica os arquivos de índice."""
    try:
        import json
        
        # Verificar arquivos do índice
        index_dir = "data_index/faiss_index_bge_m3"
        
        logger.info(f"Verificando diretório de índice: {index_dir}")
        
        # Verificar documents.json
        docs_file = os.path.join(index_dir, "documents.json")
        if os.path.exists(docs_file):
            with open(docs_file, 'r', encoding='utf-8') as f:
                docs = json.load(f)
            logger.info(f"Documentos no índice: {len(docs)}")
            if docs:
                logger.info(f"Primeiro documento: {docs[0][:100]}...")
        else:
            logger.error(f"Arquivo {docs_file} não encontrado")
            
        # Verificar metadata.json
        meta_file = os.path.join(index_dir, "metadata.json")
        if os.path.exists(meta_file):
            with open(meta_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            logger.info(f"Metadados: {len(metadata)} entradas")
        else:
            logger.error(f"Arquivo {meta_file} não encontrado")
            
        # Verificar embeddings.npy
        emb_file = os.path.join(index_dir, "embeddings.npy")
        if os.path.exists(emb_file):
            embeddings = np.load(emb_file)
            logger.info(f"Embeddings: shape {embeddings.shape}")
        else:
            logger.error(f"Arquivo {emb_file} não encontrado")
            
        return True
        
    except Exception as e:
        logger.error(f"Erro verificando arquivos de índice: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    logger.info("=== TESTE DO MODELO DE EMBEDDING ===")
    embedding_ok = test_embedding_model()
    
    logger.info("\n=== TESTE DOS ARQUIVOS DE ÍNDICE ===")
    index_ok = test_index_files()
    
    print(f"\nResultados:")
    print(f"Embedding: {'OK' if embedding_ok else 'FALHOU'}")
    print(f"Índice: {'OK' if index_ok else 'FALHOU'}")