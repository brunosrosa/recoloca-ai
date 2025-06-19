#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples do sistema RAG

Este script testa o sistema RAG de forma simples e direta.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import json
import sys
import os
from pathlib import Path
import time

# Adicionar caminhos necessários
project_root = Path(__file__).parent.parent
rag_infra_path = project_root / "rag_infra"
sys.path.insert(0, str(rag_infra_path))
sys.path.insert(0, str(project_root))

print(f"Projeto: {project_root}")
print(f"RAG Infra: {rag_infra_path}")

try:
    # Importar diretamente do arquivo
    import importlib.util
    
    # Carregar constants
    constants_path = rag_infra_path / "core_logic" / "constants.py"
    spec = importlib.util.spec_from_file_location("constants", constants_path)
    constants = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(constants)
    
    # Carregar pytorch_gpu_retriever
    retriever_path = rag_infra_path / "core_logic" / "pytorch_gpu_retriever.py"
    spec = importlib.util.spec_from_file_location("pytorch_gpu_retriever", retriever_path)
    retriever_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(retriever_module)
    
    PyTorchGPURetriever = retriever_module.PyTorchGPURetriever
    FAISS_INDEX_DIR = constants.FAISS_INDEX_DIR
    
    print("✅ Módulos carregados com sucesso")
    
except Exception as e:
    print(f"❌ Erro ao carregar módulos: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

def test_rag_system():
    """Testa o sistema RAG."""
    try:
        print("\n🔍 Teste Simples do Sistema RAG")
        print("=" * 40)
        
        # 1. Verificar arquivos
        print("\n1. Verificando arquivos:")
        embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
        documents_path = FAISS_INDEX_DIR / "documents.json"
        metadata_path = FAISS_INDEX_DIR / "metadata.json"
        
        files_exist = {
            "Embeddings": embeddings_path.exists(),
            "Documents": documents_path.exists(),
            "Metadata": metadata_path.exists()
        }
        
        for name, exists in files_exist.items():
            status = "✅" if exists else "❌"
            print(f"  {name}: {status}")
        
        if not all(files_exist.values()):
            print("❌ Arquivos necessários não encontrados")
            return False
        
        # 2. Inicializar retriever
        print("\n2. Inicializando retriever:")
        try:
            retriever = PyTorchGPURetriever(
                index_dir=str(FAISS_INDEX_DIR),
                similarity_threshold=0.1
            )
            print("  ✅ Retriever inicializado")
        except Exception as e:
            print(f"  ❌ Erro na inicialização: {e}")
            return False
        
        # 3. Verificar dados carregados
        print("\n3. Verificando dados carregados:")
        try:
            if hasattr(retriever, 'embeddings') and retriever.embeddings is not None:
                print(f"  Embeddings: {retriever.embeddings.shape}")
            else:
                print("  ❌ Embeddings não carregados")
                return False
                
            if hasattr(retriever, 'documents') and retriever.documents:
                print(f"  Documentos: {len(retriever.documents)}")
            else:
                print("  ❌ Documentos não carregados")
                return False
                
            if hasattr(retriever, 'metadata') and retriever.metadata:
                print(f"  Metadados: {len(retriever.metadata)}")
            else:
                print("  ❌ Metadados não carregados")
                return False
                
        except Exception as e:
            print(f"  ❌ Erro ao verificar dados: {e}")
            return False
        
        # 4. Teste de busca simples
        print("\n4. Teste de busca:")
        test_queries = [
            "requisitos funcionais",
            "arquitetura",
            "MVP",
            "Recoloca",
            "backend"
        ]
        
        successful_searches = 0
        
        for query in test_queries:
            try:
                start_time = time.time()
                results = retriever.search(query, top_k=3)
                search_time = time.time() - start_time
                
                if results and len(results) > 0:
                    successful_searches += 1
                    print(f"  ✅ '{query}': {len(results)} resultados ({search_time:.3f}s)")
                    # Mostrar score do primeiro resultado
                    if results[0].get('score'):
                        print(f"      Score: {results[0]['score']:.3f}")
                else:
                    print(f"  ❌ '{query}': Nenhum resultado ({search_time:.3f}s)")
                    
            except Exception as e:
                print(f"  ❌ '{query}': Erro - {e}")
        
        # 5. Resultado final
        success_rate = (successful_searches / len(test_queries)) * 100
        print(f"\n5. Resultado final:")
        print(f"  Taxa de sucesso: {success_rate:.1f}% ({successful_searches}/{len(test_queries)})")
        
        if success_rate >= 60:
            print("  ✅ Sistema funcionando bem!")
            return True
        elif success_rate >= 20:
            print("  🟡 Sistema funcionando parcialmente")
            return True
        else:
            print("  ❌ Sistema com problemas")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal."""
    success = test_rag_system()
    
    if success:
        print("\n🎉 Teste concluído com sucesso!")
        print("\n🚀 Sistema RAG está operacional.")
    else:
        print("\n❌ Teste falhou.")
        print("\n💡 Verifique:")
        print("  1. Se os arquivos de índice existem")
        print("  2. Se a GPU está funcionando")
        print("  3. Se os embeddings estão corretos")

if __name__ == "__main__":
    main()