#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste final do sistema RAG com busca real

Este script testa o sistema RAG com consultas reais para verificar se está funcionando.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import json
import logging
import sys
import os
from pathlib import Path
import time

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Adicionar caminho específico para rag_infra
rag_infra_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rag_infra')
sys.path.insert(0, rag_infra_path)

from rag_infra.src.core.pytorch_gpu_retriever import PyTorchGPURetriever
from rag_infra.src.core.constants import FAISS_INDEX_DIR

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_rag_search():
    """Testa o sistema RAG com buscas reais."""
    try:
        print("[SEARCH] Teste Final do Sistema RAG")
        print("=" * 40)
        
        # 1. Inicializar o retriever
        print("\n1. Inicializando PyTorchGPURetriever...")
        start_time = time.time()
        
        retriever = PyTorchGPURetriever(
            index_dir=str(FAISS_INDEX_DIR),
            similarity_threshold=0.1  # Threshold baixo para mais resultados
        )
        
        init_time = time.time() - start_time
        print(f"  [OK] Inicializado em {init_time:.2f}s")
        
        # 2. Verificar status do sistema
        print("\n2. Verificando status do sistema:")
        print(f"  Embeddings carregados: {retriever.embeddings.shape if hasattr(retriever, 'embeddings') and retriever.embeddings is not None else 'Não carregados'}")
        print(f"  Documentos carregados: {len(retriever.documents) if hasattr(retriever, 'documents') and retriever.documents else 0}")
        print(f"  Metadados carregados: {len(retriever.metadata) if hasattr(retriever, 'metadata') and retriever.metadata else 0}")
        
        # 3. Testes de busca
        print("\n3. Executando testes de busca:")
        
        test_queries = [
            "requisitos funcionais",
            "arquitetura sistema",
            "design interface",
            "MVP",
            "Recoloca.ai",
            "backend",
            "FastAPI",
            "Supabase",
            "agentes IA",
            "mentores"
        ]
        
        successful_searches = 0
        total_results = 0
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n  Teste {i}/10: '{query}'")
            
            try:
                search_start = time.time()
                results = retriever.search(query, top_k=3)
                search_time = time.time() - search_start
                
                if results:
                    successful_searches += 1
                    total_results += len(results)
                    print(f"    [OK] {len(results)} resultados em {search_time:.3f}s")
                    
                    # Mostrar primeiro resultado
                    first_result = results[0]
                    content_preview = first_result['content'][:100] + "..." if len(first_result['content']) > 100 else first_result['content']
                    print(f"    [EMOJI] Primeiro resultado (score: {first_result['score']:.3f}): {content_preview}")
                else:
                    print(f"    [ERROR] Nenhum resultado em {search_time:.3f}s")
                    
            except Exception as e:
                print(f"    [ERROR] Erro na busca: {str(e)}")
        
        # 4. Estatísticas finais
        print("\n4. Estatísticas finais:")
        success_rate = (successful_searches / len(test_queries)) * 100
        avg_results = total_results / len(test_queries) if len(test_queries) > 0 else 0
        
        print(f"  Taxa de sucesso: {success_rate:.1f}% ({successful_searches}/{len(test_queries)})")
        print(f"  Média de resultados por consulta: {avg_results:.1f}")
        print(f"  Total de resultados encontrados: {total_results}")
        
        # 5. Teste de performance
        print("\n5. Teste de performance:")
        performance_query = "requisitos funcionais sistema"
        performance_runs = 5
        
        times = []
        for i in range(performance_runs):
            start = time.time()
            results = retriever.search(performance_query, top_k=5)
            elapsed = time.time() - start
            times.append(elapsed)
        
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        print(f"  Tempo médio de busca: {avg_time:.3f}s")
        print(f"  Tempo mínimo: {min_time:.3f}s")
        print(f"  Tempo máximo: {max_time:.3f}s")
        
        # 6. Avaliação final
        print("\n6. Avaliação final:")
        
        if success_rate >= 70:
            status = "[OK] EXCELENTE"
        elif success_rate >= 50:
            status = "🟡 BOM"
        elif success_rate >= 30:
            status = "🟠 REGULAR"
        else:
            status = "[ERROR] RUIM"
        
        print(f"  Status do sistema: {status}")
        
        if avg_time <= 0.5:
            perf_status = "[OK] RÁPIDO"
        elif avg_time <= 1.0:
            perf_status = "🟡 MODERADO"
        else:
            perf_status = "🟠 LENTO"
        
        print(f"  Performance: {perf_status}")
        
        # 7. Salvar relatório
        print("\n7. Salvando relatório:")
        
        report = {
            "test_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "initialization_time": init_time,
            "total_queries": len(test_queries),
            "successful_searches": successful_searches,
            "success_rate_percent": success_rate,
            "total_results": total_results,
            "average_results_per_query": avg_results,
            "performance_test": {
                "query": performance_query,
                "runs": performance_runs,
                "average_time": avg_time,
                "min_time": min_time,
                "max_time": max_time
            },
            "system_status": status,
            "performance_status": perf_status,
            "embeddings_shape": list(retriever.embeddings.shape) if hasattr(retriever, 'embeddings') and retriever.embeddings is not None else None,
            "documents_count": len(retriever.documents) if hasattr(retriever, 'documents') and retriever.documents else 0,
            "metadata_count": len(retriever.metadata) if hasattr(retriever, 'metadata') and retriever.metadata else 0
        }
        
        report_path = Path("scripts") / "rag_search_test_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"  Relatório salvo: {report_path}")
        
        # Resultado final
        if success_rate >= 50 and avg_time <= 1.0:
            print("\n[EMOJI] Sistema RAG funcionando corretamente!")
            return True
        else:
            print("\n[EMOJI] Sistema RAG precisa de ajustes.")
            return False
            
    except Exception as e:
        logger.error(f"Erro no teste: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal."""
    success = test_rag_search()
    
    if success:
        print("\n[OK] Teste concluído com sucesso!")
        print("\n[START] O sistema RAG está pronto para uso.")
    else:
        print("\n[ERROR] Teste falhou.")
        print("\n[EMOJI] Sugestões:")
        print("  1. Verifique os logs de erro")
        print("  2. Ajuste o threshold de similaridade")
        print("  3. Verifique a qualidade dos documentos indexados")
        print("  4. Considere reindexar com chunks menores")

if __name__ == "__main__":
    main()