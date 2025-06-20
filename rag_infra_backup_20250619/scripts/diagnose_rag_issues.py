#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Diagnóstico e Correção do Sistema RAG

Este script investiga e corrige os principais problemas identificados:
1. Threshold de similaridade muito alto
2. Filtros ativos bloqueando resultados
3. Normalização de vetores
4. Configuração do backend PyTorch para RTX 2060

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import sys
import os
import json
import logging
import torch
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core_logic'))

from ..core_logic.rag_retriever import RAGRetriever
from ..core_logic.constants import MIN_SIMILARITY_SCORE, DEFAULT_TOP_K
from ..core_logic.embedding_model import EmbeddingModelManager

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RAGDiagnostics:
    """
    Classe para diagnóstico e correção de problemas do sistema RAG.
    """
    
    def __init__(self):
        self.retriever = None
        self.embedding_model = None
        self.issues_found = []
        self.fixes_applied = []
        
    def run_full_diagnosis(self) -> Dict[str, Any]:
        """
        Executa diagnóstico completo do sistema RAG.
        
        Returns:
            Dict: Relatório completo do diagnóstico
        """
        logger.info("🔍 Iniciando diagnóstico completo do sistema RAG...")
        
        report = {
            "timestamp": str(torch.cuda.current_device() if torch.cuda.is_available() else "CPU"),
            "gpu_info": self._check_gpu_configuration(),
            "threshold_analysis": self._analyze_threshold_issues(),
            "filter_analysis": self._check_active_filters(),
            "normalization_check": self._verify_vector_normalization(),
            "backend_config": self._check_pytorch_backend(),
            "search_tests": self._run_search_tests(),
            "issues_found": self.issues_found,
            "fixes_applied": self.fixes_applied,
            "recommendations": self._generate_recommendations()
        }
        
        self._save_report(report)
        self._print_summary(report)
        
        return report
    
    def _check_gpu_configuration(self) -> Dict[str, Any]:
        """
        Verifica configuração da GPU e compatibilidade com PyTorch.
        """
        logger.info("🔧 Verificando configuração da GPU...")
        
        gpu_info = {
            "cuda_available": torch.cuda.is_available(),
            "device_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
            "current_device": None,
            "gpu_name": None,
            "memory_info": None,
            "pytorch_version": torch.__version__,
            "rtx_2060_detected": False,
            "recommended_settings": {}
        }
        
        if torch.cuda.is_available():
            gpu_info["current_device"] = torch.cuda.current_device()
            gpu_info["gpu_name"] = torch.cuda.get_device_name(0)
            gpu_info["memory_info"] = {
                "total": torch.cuda.get_device_properties(0).total_memory,
                "allocated": torch.cuda.memory_allocated(0),
                "cached": torch.cuda.memory_reserved(0)
            }
            
            # Detectar RTX 2060
            if "rtx 2060" in gpu_info["gpu_name"].lower():
                gpu_info["rtx_2060_detected"] = True
                gpu_info["recommended_settings"] = {
                    "force_pytorch": True,
                    "batch_size": 16,  # Menor para RTX 2060
                    "use_optimizations": True,
                    "memory_fraction": 0.8
                }
                logger.info("✅ RTX 2060 detectada - configurações otimizadas recomendadas")
            else:
                gpu_info["recommended_settings"] = {
                    "force_pytorch": False,
                    "batch_size": 32,
                    "use_optimizations": True,
                    "memory_fraction": 0.9
                }
        else:
            self.issues_found.append("CUDA não disponível - sistema funcionará apenas em CPU")
            gpu_info["recommended_settings"] = {
                "force_cpu": True,
                "batch_size": 8
            }
        
        return gpu_info
    
    def _analyze_threshold_issues(self) -> Dict[str, Any]:
        """
        Analisa problemas relacionados ao threshold de similaridade.
        """
        logger.info("📊 Analisando threshold de similaridade...")
        
        analysis = {
            "current_threshold": MIN_SIMILARITY_SCORE,
            "threshold_too_high": False,
            "recommended_threshold": None,
            "test_results": []
        }
        
        # Testar diferentes thresholds
        test_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5]
        test_query = "arquitetura sistema"
        
        try:
            self._initialize_retriever()
            
            for threshold in test_thresholds:
                results = self.retriever.search(test_query, top_k=10, min_score=threshold)
                analysis["test_results"].append({
                    "threshold": threshold,
                    "results_count": len(results),
                    "avg_score": np.mean([r.score for r in results]) if results else 0.0
                })
            
            # Determinar threshold recomendado
            good_results = [t for t in analysis["test_results"] if t["results_count"] >= 3]
            if good_results:
                analysis["recommended_threshold"] = min(good_results, key=lambda x: x["threshold"])["threshold"]
            else:
                analysis["recommended_threshold"] = 0.1
                self.issues_found.append("Threshold muito alto - nenhum resultado encontrado")
            
            if analysis["current_threshold"] > analysis["recommended_threshold"]:
                analysis["threshold_too_high"] = True
                self.issues_found.append(f"Threshold atual ({MIN_SIMILARITY_SCORE}) muito alto")
                
        except Exception as e:
            logger.error(f"Erro na análise de threshold: {e}")
            analysis["error"] = str(e)
        
        return analysis
    
    def _check_active_filters(self) -> Dict[str, Any]:
        """
        Verifica se há filtros ativos que podem estar bloqueando resultados.
        """
        logger.info("🔍 Verificando filtros ativos...")
        
        filter_analysis = {
            "category_filters_found": False,
            "metadata_filters": [],
            "filter_impact": {}
        }
        
        try:
            self._initialize_retriever()
            
            # Testar busca sem filtros
            test_query = "arquitetura"
            results_no_filter = self.retriever.search(test_query, top_k=10, min_score=0.1)
            
            # Testar com diferentes filtros de categoria
            test_categories = ["documentacao", "arquitetura", "requisitos", "design"]
            
            for category in test_categories:
                results_with_filter = self.retriever.search(
                    test_query, top_k=10, min_score=0.1, category_filter=category
                )
                
                filter_analysis["filter_impact"][category] = {
                    "results_without_filter": len(results_no_filter),
                    "results_with_filter": len(results_with_filter),
                    "reduction_percentage": (
                        (len(results_no_filter) - len(results_with_filter)) / len(results_no_filter) * 100
                        if results_no_filter else 0
                    )
                }
            
            # Verificar se algum filtro está bloqueando muito
            for category, impact in filter_analysis["filter_impact"].items():
                if impact["reduction_percentage"] > 80:
                    self.issues_found.append(f"Filtro de categoria '{category}' muito restritivo")
                    
        except Exception as e:
            logger.error(f"Erro na verificação de filtros: {e}")
            filter_analysis["error"] = str(e)
        
        return filter_analysis
    
    def _verify_vector_normalization(self) -> Dict[str, Any]:
        """
        Verifica se os embeddings estão sendo normalizados corretamente.
        """
        logger.info("📐 Verificando normalização de vetores...")
        
        normalization_check = {
            "embeddings_normalized": False,
            "query_normalized": False,
            "normalization_method": None,
            "sample_norms": []
        }
        
        try:
            self._initialize_retriever()
            
            # Verificar normalização dos embeddings do índice
            if hasattr(self.retriever, 'pytorch_retriever') and self.retriever.pytorch_retriever:
                if hasattr(self.retriever.pytorch_retriever, 'embeddings_tensor'):
                    embeddings = self.retriever.pytorch_retriever.embeddings_tensor
                    if embeddings is not None:
                        # Calcular normas de uma amostra
                        sample_size = min(100, embeddings.shape[0])
                        sample_embeddings = embeddings[:sample_size]
                        norms = torch.norm(sample_embeddings, p=2, dim=1).cpu().numpy()
                        
                        normalization_check["sample_norms"] = norms.tolist()[:10]  # Primeiras 10
                        
                        # Verificar se estão normalizados (norma ≈ 1.0)
                        avg_norm = np.mean(norms)
                        std_norm = np.std(norms)
                        
                        if 0.99 <= avg_norm <= 1.01 and std_norm < 0.01:
                            normalization_check["embeddings_normalized"] = True
                            normalization_check["normalization_method"] = "L2 normalization"
                        else:
                            self.issues_found.append(f"Embeddings não normalizados (norma média: {avg_norm:.3f})")
            
            # Testar normalização de query
            test_query = "teste normalização"
            if self.embedding_model:
                query_embedding = self.embedding_model.embed_query(test_query)
                if query_embedding is not None:
                    query_norm = np.linalg.norm(query_embedding)
                    normalization_check["query_norm"] = float(query_norm)
                    
                    if 0.99 <= query_norm <= 1.01:
                        normalization_check["query_normalized"] = True
                    else:
                        self.issues_found.append(f"Query embedding não normalizado (norma: {query_norm:.3f})")
                        
        except Exception as e:
            logger.error(f"Erro na verificação de normalização: {e}")
            normalization_check["error"] = str(e)
        
        return normalization_check
    
    def _check_pytorch_backend(self) -> Dict[str, Any]:
        """
        Verifica configuração do backend PyTorch.
        """
        logger.info("⚙️ Verificando configuração do backend PyTorch...")
        
        backend_config = {
            "pytorch_version": torch.__version__,
            "cuda_version": None,
            "cudnn_version": None,
            "backend_selection": None,
            "memory_management": {},
            "optimization_flags": {}
        }
        
        try:
            if torch.cuda.is_available():
                backend_config["cuda_version"] = torch.version.cuda
                backend_config["cudnn_version"] = torch.backends.cudnn.version()
                
                # Verificar configurações de memória
                backend_config["memory_management"] = {
                    "memory_fraction": torch.cuda.get_device_properties(0).total_memory,
                    "allow_growth": True,  # PyTorch permite por padrão
                    "empty_cache_available": hasattr(torch.cuda, 'empty_cache')
                }
                
                # Verificar otimizações
                backend_config["optimization_flags"] = {
                    "cudnn_benchmark": torch.backends.cudnn.benchmark,
                    "cudnn_deterministic": torch.backends.cudnn.deterministic,
                    "allow_tf32": torch.backends.cuda.matmul.allow_tf32 if hasattr(torch.backends.cuda.matmul, 'allow_tf32') else None
                }
                
                # Determinar backend recomendado
                gpu_name = torch.cuda.get_device_name(0).lower()
                if "rtx 2060" in gpu_name or "gtx" in gpu_name:
                    backend_config["backend_selection"] = "pytorch_optimized"
                    backend_config["reason"] = "GPU GeForce com limitações FAISS-GPU"
                else:
                    backend_config["backend_selection"] = "faiss_gpu"
                    backend_config["reason"] = "GPU compatível com FAISS-GPU"
            else:
                backend_config["backend_selection"] = "cpu_only"
                backend_config["reason"] = "CUDA não disponível"
                
        except Exception as e:
            logger.error(f"Erro na verificação do backend: {e}")
            backend_config["error"] = str(e)
        
        return backend_config
    
    def _run_search_tests(self) -> Dict[str, Any]:
        """
        Executa testes de busca com diferentes configurações.
        """
        logger.info("🧪 Executando testes de busca...")
        
        test_results = {
            "test_queries": [
                "arquitetura sistema",
                "requisitos funcionais",
                "design interface",
                "documentação técnica"
            ],
            "results": {},
            "performance": {},
            "success_rate": 0.0
        }
        
        try:
            self._initialize_retriever()
            
            successful_tests = 0
            total_tests = len(test_results["test_queries"])
            
            for query in test_results["test_queries"]:
                try:
                    import time
                    start_time = time.time()
                    
                    # Teste com threshold baixo
                    results = self.retriever.search(query, top_k=5, min_score=0.1)
                    
                    end_time = time.time()
                    
                    test_results["results"][query] = {
                        "results_count": len(results),
                        "avg_score": np.mean([r.score for r in results]) if results else 0.0,
                        "max_score": max([r.score for r in results]) if results else 0.0,
                        "min_score": min([r.score for r in results]) if results else 0.0
                    }
                    
                    test_results["performance"][query] = {
                        "search_time": end_time - start_time,
                        "results_per_second": len(results) / (end_time - start_time) if (end_time - start_time) > 0 else 0
                    }
                    
                    if len(results) > 0:
                        successful_tests += 1
                    else:
                        self.issues_found.append(f"Nenhum resultado para query: '{query}'")
                        
                except Exception as e:
                    logger.error(f"Erro no teste de query '{query}': {e}")
                    test_results["results"][query] = {"error": str(e)}
            
            test_results["success_rate"] = successful_tests / total_tests
            
            if test_results["success_rate"] < 0.5:
                self.issues_found.append(f"Taxa de sucesso baixa: {test_results['success_rate']:.1%}")
                
        except Exception as e:
            logger.error(f"Erro nos testes de busca: {e}")
            test_results["error"] = str(e)
        
        return test_results
    
    def _initialize_retriever(self):
        """
        Inicializa o retriever se ainda não foi inicializado.
        """
        if self.retriever is None:
            # Usar configurações otimizadas para RTX 2060
            self.retriever = RAGRetriever(
                force_pytorch=True,  # Forçar PyTorch para RTX 2060
                use_optimizations=True,
                batch_size=16  # Menor batch size para RTX 2060
            )
            
            if not self.retriever.initialize():
                raise Exception("Falha ao inicializar retriever")
            
            if not self.retriever.load_index():
                raise Exception("Falha ao carregar índice")
        
        if self.embedding_model is None:
            self.embedding_model = EmbeddingModelManager()
            self.embedding_model.load_model()
    
    def _generate_recommendations(self) -> List[str]:
        """
        Gera recomendações baseadas nos problemas encontrados.
        """
        recommendations = []
        
        if any("threshold" in issue.lower() for issue in self.issues_found):
            recommendations.append("Reduzir MIN_SIMILARITY_SCORE para 0.1 ou 0.2")
        
        if any("filtro" in issue.lower() for issue in self.issues_found):
            recommendations.append("Revisar filtros de categoria - podem estar muito restritivos")
        
        if any("normaliz" in issue.lower() for issue in self.issues_found):
            recommendations.append("Verificar normalização L2 dos embeddings")
        
        if any("rtx 2060" in issue.lower() for issue in self.issues_found):
            recommendations.append("Usar PyTorchGPURetriever em vez de FAISS para RTX 2060")
        
        if any("cuda" in issue.lower() for issue in self.issues_found):
            recommendations.append("Verificar instalação do CUDA e drivers da GPU")
        
        if not recommendations:
            recommendations.append("Sistema funcionando corretamente - nenhuma correção necessária")
        
        return recommendations
    
    def _save_report(self, report: Dict[str, Any]):
        """
        Salva o relatório de diagnóstico.
        """
        try:
            # Importar configuração centralizada
             import sys
             sys.path.append(str(Path(__file__).parent.parent))
             from config import get_report_path, REPORT_CONFIG
             
             report_path = get_report_path("rag_diagnosis_report.json")
             with open(report_path, 'w', encoding=REPORT_CONFIG['encoding']) as f:
                 json.dump(report, f, 
                          indent=REPORT_CONFIG['indent'], 
                          ensure_ascii=REPORT_CONFIG['ensure_ascii'], 
                          default=REPORT_CONFIG['default_serializer'])
             logger.info(f"📄 Relatório salvo em: {report_path.absolute()}")
        except Exception as e:
            logger.error(f"Erro ao salvar relatório: {e}")
    
    def _print_summary(self, report: Dict[str, Any]):
        """
        Imprime resumo do diagnóstico.
        """
        print("\n" + "="*80)
        print("🔍 RELATÓRIO DE DIAGNÓSTICO DO SISTEMA RAG")
        print("="*80)
        
        # GPU Info
        gpu_info = report["gpu_info"]
        print(f"\n🔧 GPU: {gpu_info.get('gpu_name', 'N/A')}")
        print(f"   CUDA Disponível: {gpu_info['cuda_available']}")
        print(f"   RTX 2060 Detectada: {gpu_info['rtx_2060_detected']}")
        
        # Threshold Analysis
        threshold_analysis = report["threshold_analysis"]
        print(f"\n📊 Threshold Atual: {threshold_analysis['current_threshold']}")
        print(f"   Threshold Recomendado: {threshold_analysis.get('recommended_threshold', 'N/A')}")
        print(f"   Threshold Muito Alto: {threshold_analysis['threshold_too_high']}")
        
        # Issues Found
        print(f"\n❌ Problemas Encontrados ({len(self.issues_found)}):")
        for i, issue in enumerate(self.issues_found, 1):
            print(f"   {i}. {issue}")
        
        # Recommendations
        recommendations = report["recommendations"]
        print(f"\n💡 Recomendações ({len(recommendations)}):")
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec}")
        
        # Search Tests
        search_tests = report["search_tests"]
        if "success_rate" in search_tests:
            print(f"\n🧪 Taxa de Sucesso dos Testes: {search_tests['success_rate']:.1%}")
        
        print("\n" + "="*80)

def main():
    """
    Função principal do script de diagnóstico.
    """
    print("🚀 Iniciando diagnóstico do sistema RAG...")
    
    diagnostics = RAGDiagnostics()
    report = diagnostics.run_full_diagnosis()
    
    print("\n✅ Diagnóstico concluído!")
    print("📄 Relatório detalhado salvo em: rag_diagnosis_report.json")

if __name__ == "__main__":
    main()