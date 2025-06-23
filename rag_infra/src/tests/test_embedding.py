#!/usr/bin/env python3
"""
Script de teste para o modelo de embedding
"""

import sys
from pathlib import Path

# Adicionar o diretório rag_infra ao path
rag_infra_path = Path(__file__).parent.parent

project_root = Path(__file__).parent.parent

sys.path.insert(0, str(rag_infra_path))
sys.path.insert(0, str(project_root / "src" / "core" / "src/core/core_logic"))

try:
    from ..core.embedding_model import EmbeddingModelManager
    
    print("🤖 Testando modelo de embedding...")
    
    # Inicializar o gerenciador
    em = EmbeddingModelManager()
    print(f"Dispositivo detectado: {em.device}")
    
    # Tentar carregar o modelo
    print("Carregando modelo...")
    result = em.load_model()
    
    if result:
        print("[OK] Modelo carregado com sucesso!")
        
        # Teste de embedding
        test_text = "Este é um teste do sistema de embedding."
        embedding = em.embed_query(test_text)
        
        if embedding is not None:
            print(f"[OK] Embedding gerado com sucesso! Dimensão: {len(embedding)}")
        else:
            print("[ERROR] Falha ao gerar embedding")
    else:
        print("[ERROR] Falha ao carregar modelo")
        
except Exception as e:
    print(f"[ERROR] Erro durante o teste: {e}")
    import traceback
    traceback.print_exc()