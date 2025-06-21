#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Debug para Embeddings e Similaridade
Investiga por que as consultas não retornam resultados mesmo com índice carregado.
"""

import os
import sys
import json
import numpy as np
from pathlib import Path

# Adicionar o diretório rag_infra ao path
project_root = Path(__file__).parent
rag_infra_path = project_root / "rag_infra"
sys.path.insert(0, str(rag_infra_path))

try:
    from core_logic.rag_retriever import RAGRetriever
    from core_logic.embedding_model import EmbeddingModelManager
except ImportError as e:
    print(f"Erro ao importar módulos RAG: {e}")
    sys.exit(1)

def debug_embeddings_and_similarity():
    """
    Debug detalhado dos embeddings e cálculos de similaridade
    """
    print("=== DEBUG: Embeddings e Similaridade ===")
    
    # Inicializar componentes
    print("\n1. Inicializando RAGRetriever...")
    retriever = RAGRetriever()
    
    try:
        retriever.initialize()
        print("✅ RAGRetriever inicializado com sucesso")
    except Exception as e:
        print(f"❌ Erro na inicialização: {e}")
        return
    
    # Carregar índice
    print("\n2. Carregando índice...")
    try:
        retriever.load_index()
        print(f"✅ Índice carregado: {len(retriever.documents)} documentos")
    except Exception as e:
        print(f"❌ Erro ao carregar índice: {e}")
        return
    
    # Verificar alguns documentos
    print("\n3. Verificando documentos carregados...")
    if retriever.documents:
        for i, doc in enumerate(retriever.documents[:3]):
            print(f"Doc {i}: {doc[:100]}...")
    else:
        print("❌ Nenhum documento encontrado")
        return
    
    # Testar embedding de consulta
    print("\n4. Testando embedding de consulta...")
    test_queries = [
        "arquitetura sistema",
        "FastAPI",
        "Supabase",
        "backend",
        "Python"
    ]
    
    embedding_model = EmbeddingModelManager()
    
    # Carregar o modelo
    print("\n--- Carregando modelo de embedding ---")
    if not embedding_model.load_model():
        print("❌ Falha ao carregar modelo de embedding")
        return
    
    for query in test_queries:
        print(f"\n--- Testando query: '{query}' ---")
        
        try:
            # Gerar embedding da consulta
            query_embedding = embedding_model.embed_query(query)
            if query_embedding is None:
                print(f"❌ Falha ao gerar embedding para '{query}'")
                continue
            print(f"✅ Embedding gerado: shape={query_embedding.shape}, norm={np.linalg.norm(query_embedding):.4f}")
            
            # Verificar se há embeddings nos documentos
            if hasattr(retriever, 'pytorch_retriever') and retriever.pytorch_retriever:
                if hasattr(retriever.pytorch_retriever, 'base_retriever'):
                    base_retriever = retriever.pytorch_retriever.base_retriever
                else:
                    base_retriever = retriever.pytorch_retriever
                
                if hasattr(base_retriever, 'embeddings_tensor') and base_retriever.embeddings_tensor is not None:
                    doc_embeddings_tensor = base_retriever.embeddings_tensor
                    print(f"✅ Embeddings dos documentos: shape={doc_embeddings_tensor.shape}, device={doc_embeddings_tensor.device}")
                    
                    # Converter para numpy para cálculos
                    doc_embeddings = doc_embeddings_tensor.cpu().numpy()
                    
                    # Calcular similaridades manualmente
                    if len(doc_embeddings) > 0:
                        # Normalizar embeddings
                        query_norm = query_embedding / np.linalg.norm(query_embedding)
                        doc_norms = doc_embeddings / np.linalg.norm(doc_embeddings, axis=1, keepdims=True)
                        
                        # Calcular similaridade coseno
                        similarities = np.dot(doc_norms, query_norm)
                        
                        print(f"Similaridades calculadas:")
                        print(f"  - Min: {similarities.min():.4f}")
                        print(f"  - Max: {similarities.max():.4f}")
                        print(f"  - Média: {similarities.mean():.4f}")
                        print(f"  - Top 5: {sorted(similarities, reverse=True)[:5]}")
                        
                        # Verificar quantos passariam por diferentes thresholds
                        for threshold in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
                            count = np.sum(similarities >= threshold)
                            print(f"  - Threshold {threshold}: {count} resultados")
                    else:
                        print("❌ Nenhum embedding de documento encontrado")
                else:
                    print("❌ Atributo 'embeddings_tensor' não encontrado no retriever")
            
            # Testar busca real
            print(f"\n--- Testando busca real ---")
            try:
                results = retriever.search(query, top_k=5)
                print(f"Busca real retornou: {len(results)} resultados")
                
                if results:
                    for i, (doc, score, metadata) in enumerate(results):
                        print(f"  Resultado {i+1}: score={score:.4f}, doc={doc[:50]}...")
                else:
                    print("❌ Busca real não retornou resultados")
            except Exception as e:
                print(f"❌ Erro na busca real: {e}")
                
        except Exception as e:
            print(f"❌ Erro ao processar query '{query}': {e}")
    
    # Verificar configurações do retriever
    print("\n5. Verificando configurações do retriever...")
    if hasattr(retriever, 'pytorch_retriever'):
        pytorch_ret = retriever.pytorch_retriever
        if hasattr(pytorch_ret, 'base_retriever'):
            base_ret = pytorch_ret.base_retriever
        else:
            base_ret = pytorch_ret
            
        print(f"Tipo do retriever: {type(base_ret)}")
        
        # Verificar atributos importantes
        attrs_to_check = ['embeddings_tensor', 'documents', 'metadata', 'device', 'embedding_manager']
        for attr in attrs_to_check:
            if hasattr(base_ret, attr):
                value = getattr(base_ret, attr)
                if attr == 'embeddings_tensor' and value is not None:
                    print(f"  {attr}: shape={value.shape}, dtype={value.dtype}, device={value.device}")
                elif attr == 'documents' and value is not None:
                    print(f"  {attr}: {len(value)} documentos")
                elif attr == 'metadata' and value is not None:
                    print(f"  {attr}: {len(value)} metadados")
                else:
                    print(f"  {attr}: {value}")
            else:
                print(f"  {attr}: ❌ Não encontrado")

def main():
    try:
        debug_embeddings_and_similarity()
    except Exception as e:
        print(f"❌ Erro geral: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()