#!/usr/bin/env python3
"""
Script de debug para testar inicialização do PyTorchGPURetriever
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório core_logic ao path
core_logic_dir = Path(__file__).parent.parent / "core_logic"
sys.path.insert(0, str(core_logic_dir))

print("=== DEBUG PYTORCH INITIALIZATION ===")
print(f"Python version: {sys.version}")
print(f"Working directory: {os.getcwd()}")
print(f"Core logic dir: {core_logic_dir}")
print(f"Core logic exists: {core_logic_dir.exists()}")

try:
    print("\n1. Testando importação de constantes...")
    from constants import PYTORCH_INDEX_DIR, PYTORCH_DOCUMENTS_FILE, PYTORCH_METADATA_FILE
    print(f"✅ Constantes importadas com sucesso")
    print(f"PYTORCH_INDEX_DIR: {PYTORCH_INDEX_DIR}")
    print(f"Directory exists: {PYTORCH_INDEX_DIR.exists()}")
    print(f"Documents file exists: {(PYTORCH_INDEX_DIR / PYTORCH_DOCUMENTS_FILE).exists()}")
    print(f"Metadata file exists: {(PYTORCH_INDEX_DIR / PYTORCH_METADATA_FILE).exists()}")
    print(f"Embeddings file exists: {(PYTORCH_INDEX_DIR / 'embeddings.pt').exists()}")
except Exception as e:
    print(f"❌ Erro ao importar constantes: {e}")
    sys.exit(1)

try:
    print("\n2. Testando importação do PyTorchGPURetriever...")
    from pytorch_gpu_retriever import PyTorchGPURetriever
    print(f"✅ PyTorchGPURetriever importado com sucesso")
except Exception as e:
    print(f"❌ Erro ao importar PyTorchGPURetriever: {e}")
    sys.exit(1)

try:
    print("\n3. Testando inicialização do PyTorchGPURetriever...")
    retriever = PyTorchGPURetriever(force_cpu=False)
    print(f"✅ PyTorchGPURetriever criado com sucesso")
    print(f"Device: {retriever.device}")
except Exception as e:
    print(f"❌ Erro ao criar PyTorchGPURetriever: {e}")
    sys.exit(1)

try:
    print("\n4. Testando inicialização do modelo de embedding...")
    success = retriever.initialize()
    print(f"Resultado da inicialização: {success}")
    if success:
        print(f"✅ Modelo de embedding inicializado com sucesso")
        print(f"Embedding manager: {retriever.embedding_manager}")
    else:
        print(f"❌ Falha na inicialização do modelo de embedding")
except Exception as e:
    print(f"❌ Erro na inicialização: {e}")
    import traceback
    traceback.print_exc()

try:
    print("\n5. Testando carregamento do índice...")
    if retriever.embedding_manager:
        success = retriever.load_index()
        print(f"Resultado do carregamento: {success}")
        if success:
            print(f"✅ Índice carregado com sucesso")
            print(f"Documentos carregados: {len(retriever.documents)}")
            print(f"Metadados carregados: {len(retriever.metadata)}")
        else:
            print(f"❌ Falha no carregamento do índice")
    else:
        print("❌ Não é possível carregar índice sem embedding manager")
except Exception as e:
    print(f"❌ Erro no carregamento: {e}")
    import traceback
    traceback.print_exc()

print("\n=== FIM DO DEBUG ===")