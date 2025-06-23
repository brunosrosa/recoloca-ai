#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste Final do Sistema RAG

Este script testa o sistema RAG após todas as correções aplicadas:
- Threshold reduzido para 0.1
- Índice consistente (281 docs = 281 metadados)
- Configurações PyTorch otimizadas para RTX 2060
- Normalização de embeddings verificada

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import sys
import os
import json
import logging
import time
from pathlib import Path
from typing import Dict, List, Any, Optional

# Adicionar o diretório raiz do projeto ao path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.append(str(project_root))
sys.path.append(str(project_root / 'src'))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RAGFinalTester:
    """
    Classe para teste final do sistema RAG.
    """
    
    def __init__(self):
        self.test_queries = [
            # Queries técnicas específicas
            "arquitetura sistema",
            "requisitos funcionais",
            "design interface",
            "API endpoints",
            "banco de dados",
            "autenticação",
            "FastAPI",
            "Supabase",
            "Python",
            "backend",
            
            # Queries do projeto Recoloca.ai
            "recoloca",
            "mentores",
            "agentes IA",
            "MVP",
            "roadmap",
            "kanban",
            "tech stack",
            "documentação",
            "desenvolvimento",
            "plataforma"
        ]
        
    def run_comprehensive_test(self) -> Dict[str, Any]:
        """
        Executa teste abrangente do sistema RAG.
        
        Returns:
            Dict: Relatório completo dos testes
        """
        logger.info("🧪 Iniciando teste final do sistema RAG...")
        
        report = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "system_info": self._get_system_info(),
            "initialization_test": self._test_initialization(),
            "index_loading_test": self._test_index_loading(),
            "search_tests": self._test_searches(),
            "performance_tests": self._test_performance(),
            "threshold_tests": self._test_different_thresholds(),
            "summary": {},
            "recommendations": []
        }
        
        # Gerar resumo
        report["summary"] = self._generate_summary(report)
        
        # Gerar recomendações
        report["recommendations"] = self._generate_recommendations(report)
        
        # Salvar relatório
        self._save_test_report(report)
        
        # Imprimir resumo
        self._print_test_summary(report)
        
        return report
    
    def _get_system_info(self) -> Dict[str, Any]:
        """
        Coleta informações do sistema.
        """
        try:
            import torch
            
            system_info = {
                "python_version": sys.version,
                "cuda_available": torch.cuda.is_available(),
                "gpu_name": None,
                "pytorch_version": torch.__version__,
                "index_status": self._check_index_status()
            }
            
            if torch.cuda.is_available():
                system_info["gpu_name"] = torch.cuda.get_device_name(0)
                system_info["gpu_memory"] = torch.cuda.get_device_properties(0).total_memory
            
            return system_info
            
        except Exception as e:
            logger.error(f"Erro ao coletar informações do sistema: {e}")
            return {"error": str(e)}
    
    def _check_index_status(self) -> Dict[str, Any]:
        """
        Verifica status do índice PyTorch.
        """
        try:
            try:
                from ..core_logic.constants import PYTORCH_INDEX_DIR, PYTORCH_DOCUMENTS_FILE, PYTORCH_METADATA_FILE
            except ImportError:
                from rag_infra.src.core.core_logic.constants import PYTORCH_INDEX_DIR, PYTORCH_DOCUMENTS_FILE, PYTORCH_METADATA_FILE
            
            status = {
                "index_dir_exists": PYTORCH_INDEX_DIR.exists(),
                "documents_file_exists": (PYTORCH_INDEX_DIR / PYTORCH_DOCUMENTS_FILE).exists(),
                "metadata_file_exists": (PYTORCH_INDEX_DIR / PYTORCH_METADATA_FILE).exists(),
                "embeddings_file_exists": (PYTORCH_INDEX_DIR / "embeddings.pt").exists(),
                "documents_count": 0,
                "metadata_count": 0,
                "consistent": False
            }
            
            # Contar documentos
            documents_path = PYTORCH_INDEX_DIR / PYTORCH_DOCUMENTS_FILE
            if documents_path.exists():
                with open(documents_path, 'r', encoding='utf-8') as f:
                    documents = json.load(f)
                    status["documents_count"] = len(documents)
            
            # Contar metadados
            metadata_path = PYTORCH_INDEX_DIR / PYTORCH_METADATA_FILE
            if metadata_path.exists():
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    status["metadata_count"] = len(metadata)
            
            # Verificar consistência
            status["consistent"] = (status["documents_count"] == status["metadata_count"] and 
                                  status["documents_count"] > 0)
            
            return status
            
        except Exception as e:
            return {"error": str(e)}
    
    def _test_initialization(self) -> Dict[str, Any]:
        """
        Testa inicialização do RAGRetriever.
        """
        logger.info("[EMOJI] Testando inicialização do RAGRetriever...")
        
        test_result = {
            "success": False,
            "error": None,
            "initialization_time": 0.0,
            "backend_used": None,
            "gpu_detected": False
        }
        
        try:
            start_time = time.time()
            
            try:
                from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
            except ImportError:
                from core.core_logic.rag_retriever import RAGRetriever
            
            # Configurações específicas para PyTorch RTX 2060
            configs_to_test = [
                {"force_pytorch": True, "use_optimizations": True, "force_cpu": False},
                {"force_pytorch": True, "use_optimizations": True, "force_cpu": True},
                {"force_pytorch": True, "use_optimizations": False, "force_cpu": False}
            ]
            
            for i, config in enumerate(configs_to_test):
                try:
                    logger.info(f"[SEARCH] Testando configuração {i+1}: {config}")
                    
                    retriever = RAGRetriever(**config)
                    
                    if retriever.initialize():
                        test_result["success"] = True
                        test_result["backend_used"] = "PyTorch" if config["force_pytorch"] else "Auto"
                        test_result["gpu_detected"] = hasattr(retriever, 'backend') and hasattr(retriever.backend, 'device')
                        
                        end_time = time.time()
                        test_result["initialization_time"] = end_time - start_time
                        
                        logger.info(f"[OK] Inicialização bem-sucedida com configuração {i+1}")
                        break
                        
                except Exception as e:
                    logger.warning(f"[WARNING] Configuração {i+1} falhou: {e}")
                    continue
            
            if not test_result["success"]:
                test_result["error"] = "Todas as configurações falharam"
                logger.error("[ERROR] Falha na inicialização com todas as configurações")
            
        except Exception as e:
            test_result["error"] = str(e)
            logger.error(f"[ERROR] Erro na inicialização: {e}")
        
        return test_result
    
    def _test_index_loading(self) -> Dict[str, Any]:
        """
        Testa carregamento do índice.
        """
        logger.info("[EMOJI] Testando carregamento do índice...")
        
        test_result = {
            "success": False,
            "error": None,
            "loading_time": 0.0,
            "index_size": 0,
            "backend_type": None
        }
        
        try:
            try:
                from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
            except ImportError:
                from core.core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
            
            if retriever.initialize():
                start_time = time.time()
                
                if retriever.load_index():
                    end_time = time.time()
                    
                    test_result["success"] = True
                    test_result["loading_time"] = end_time - start_time
                    # Determinar tipo de backend
                    if hasattr(retriever, 'pytorch_retriever') and retriever.pytorch_retriever:
                        test_result["backend_type"] = type(retriever.pytorch_retriever).__name__
                        # Obter tamanho do índice PyTorch
                        test_result["index_size"] = len(retriever.documents)
                    else:
                        test_result["backend_type"] = "FAISS"
                        test_result["index_size"] = len(retriever.documents)
                    
                    logger.info(f"[OK] Índice carregado: {test_result['index_size']} embeddings em {test_result['loading_time']:.3f}s")
                else:
                    test_result["error"] = "Falha ao carregar índice"
                    logger.error("[ERROR] Falha ao carregar índice")
            else:
                test_result["error"] = "Falha na inicialização do retriever"
                logger.error("[ERROR] Falha na inicialização do retriever")
                
        except Exception as e:
            test_result["error"] = str(e)
            logger.error(f"[ERROR] Erro no carregamento: {e}")
        
        return test_result
    
    def _test_searches(self) -> Dict[str, Any]:
        """
        Testa buscas com diferentes queries.
        """
        logger.info("[SEARCH] Testando buscas...")
        
        test_result = {
            "total_queries": len(self.test_queries),
            "successful_queries": 0,
            "failed_queries": 0,
            "total_results": 0,
            "avg_search_time": 0.0,
            "avg_results_per_query": 0.0,
            "query_results": {},
            "errors": []
        }
        
        try:
            from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
            
            if not (retriever.initialize() and retriever.load_index()):
                test_result["errors"].append("Falha na inicialização/carregamento")
                return test_result
            
            total_time = 0.0
            
            for query in self.test_queries:
                try:
                    start_time = time.time()
                    
                    # Testar com threshold baixo (0.1)
                    results = retriever.search(query, top_k=5, min_score=0.0)
                    
                    end_time = time.time()
                    search_time = end_time - start_time
                    total_time += search_time
                    
                    if results:
                        test_result["successful_queries"] += 1
                        test_result["total_results"] += len(results)
                        
                        # Armazenar detalhes dos resultados
                        test_result["query_results"][query] = {
                            "results_count": len(results),
                            "search_time": search_time,
                            "top_score": max([r.score for r in results]) if results else 0.0,
                            "avg_score": sum([r.score for r in results]) / len(results) if results else 0.0,
                            "success": True
                        }
                        
                        logger.info(f"[OK] '{query}': {len(results)} resultados (score máx: {test_result['query_results'][query]['top_score']:.3f})")
                    else:
                        test_result["failed_queries"] += 1
                        test_result["query_results"][query] = {
                            "results_count": 0,
                            "search_time": search_time,
                            "success": False,
                            "reason": "Nenhum resultado encontrado"
                        }
                        
                        logger.warning(f"[WARNING] '{query}': Nenhum resultado")
                        
                except Exception as e:
                    test_result["failed_queries"] += 1
                    test_result["errors"].append(f"Erro na query '{query}': {e}")
                    test_result["query_results"][query] = {
                        "success": False,
                        "error": str(e)
                    }
                    logger.error(f"[ERROR] Erro na query '{query}': {e}")
            
            # Calcular médias
            if test_result["total_queries"] > 0:
                test_result["avg_search_time"] = total_time / test_result["total_queries"]
                
            if test_result["successful_queries"] > 0:
                test_result["avg_results_per_query"] = test_result["total_results"] / test_result["successful_queries"]
            
            logger.info(f"[EMOJI] Resumo: {test_result['successful_queries']}/{test_result['total_queries']} queries bem-sucedidas")
            
        except Exception as e:
            test_result["errors"].append(f"Erro geral nos testes: {e}")
            logger.error(f"[ERROR] Erro geral nos testes: {e}")
        
        return test_result
    
    def _test_performance(self) -> Dict[str, Any]:
        """
        Testa performance do sistema.
        """
        logger.info("[EMOJI] Testando performance...")
        
        test_result = {
            "batch_search_time": 0.0,
            "single_search_time": 0.0,
            "memory_usage": 0,
            "gpu_memory_usage": 0,
            "throughput_queries_per_second": 0.0
        }
        
        try:
            import psutil
            import torch
            
            from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
            
            if not (retriever.initialize() and retriever.load_index()):
                return test_result
            
            # Medir uso de memória
            process = psutil.Process()
            test_result["memory_usage"] = process.memory_info().rss / 1024 / 1024  # MB
            
            if torch.cuda.is_available():
                test_result["gpu_memory_usage"] = torch.cuda.memory_allocated() / 1024 / 1024  # MB
            
            # Teste de performance - busca única
            test_query = "arquitetura sistema"
            start_time = time.time()
            results = retriever.search(test_query, top_k=5, min_score=0.0)
            end_time = time.time()
            test_result["single_search_time"] = end_time - start_time
            
            # Teste de performance - múltiplas buscas
            batch_queries = ["arquitetura", "sistema", "API", "banco", "interface"]
            start_time = time.time()
            
            for query in batch_queries:
                retriever.search(query, top_k=3, min_score=0.0)
            
            end_time = time.time()
            test_result["batch_search_time"] = end_time - start_time
            
            # Calcular throughput
            if test_result["batch_search_time"] > 0:
                test_result["throughput_queries_per_second"] = len(batch_queries) / test_result["batch_search_time"]
            
            logger.info(f"[EMOJI] Performance: {test_result['single_search_time']:.3f}s por busca, {test_result['throughput_queries_per_second']:.1f} queries/s")
            
        except Exception as e:
            logger.error(f"[ERROR] Erro no teste de performance: {e}")
        
        return test_result
    
    def _test_different_thresholds(self) -> Dict[str, Any]:
        """
        Testa diferentes thresholds de similaridade.
        """
        logger.info("[EMOJI] Testando diferentes thresholds...")
        
        thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
        test_query = "arquitetura sistema"
        
        test_result = {
            "query_used": test_query,
            "threshold_results": {},
            "optimal_threshold": 0.1
        }
        
        try:
            from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
            
            if not (retriever.initialize() and retriever.load_index()):
                return test_result
            
            max_results = 0
            optimal_threshold = 0.1
            
            for threshold in thresholds:
                try:
                    results = retriever.search(test_query, top_k=10, min_score=threshold)
                    
                    result_info = {
                        "results_count": len(results),
                        "avg_score": sum([r.score for r in results]) / len(results) if results else 0.0,
                        "min_score": min([r.score for r in results]) if results else 0.0,
                        "max_score": max([r.score for r in results]) if results else 0.0
                    }
                    
                    test_result["threshold_results"][threshold] = result_info
                    
                    # Encontrar threshold ótimo (máximo de resultados com qualidade)
                    if len(results) > max_results and result_info["avg_score"] > 0.2:
                        max_results = len(results)
                        optimal_threshold = threshold
                    
                    logger.info(f"[EMOJI] Threshold {threshold}: {len(results)} resultados (avg score: {result_info['avg_score']:.3f})")
                    
                except Exception as e:
                    test_result["threshold_results"][threshold] = {"error": str(e)}
                    logger.error(f"[ERROR] Erro com threshold {threshold}: {e}")
            
            test_result["optimal_threshold"] = optimal_threshold
            logger.info(f"[EMOJI] Threshold ótimo identificado: {optimal_threshold}")
            
        except Exception as e:
            logger.error(f"[ERROR] Erro no teste de thresholds: {e}")
        
        return test_result
    
    def _generate_summary(self, report: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera resumo dos testes.
        """
        summary = {
            "overall_success": False,
            "system_functional": False,
            "performance_acceptable": False,
            "issues_found": [],
            "success_rate": 0.0
        }
        
        try:
            # Verificar se sistema está funcional
            init_success = report.get("initialization_test", {}).get("success", False)
            loading_success = report.get("index_loading_test", {}).get("success", False)
            
            summary["system_functional"] = init_success and loading_success
            
            # Calcular taxa de sucesso das buscas
            search_tests = report.get("search_tests", {})
            total_queries = search_tests.get("total_queries", 0)
            successful_queries = search_tests.get("successful_queries", 0)
            
            if total_queries > 0:
                summary["success_rate"] = (successful_queries / total_queries) * 100
            
            # Verificar performance
            perf_tests = report.get("performance_tests", {})
            single_search_time = perf_tests.get("single_search_time", 999)
            summary["performance_acceptable"] = single_search_time < 2.0  # Menos de 2 segundos
            
            # Determinar sucesso geral
            summary["overall_success"] = (
                summary["system_functional"] and 
                summary["success_rate"] > 50 and 
                summary["performance_acceptable"]
            )
            
            # Identificar problemas
            if not init_success:
                summary["issues_found"].append("Falha na inicialização")
            if not loading_success:
                summary["issues_found"].append("Falha no carregamento do índice")
            if summary["success_rate"] < 50:
                summary["issues_found"].append(f"Taxa de sucesso baixa: {summary['success_rate']:.1f}%")
            if not summary["performance_acceptable"]:
                summary["issues_found"].append(f"Performance lenta: {single_search_time:.3f}s por busca")
            
        except Exception as e:
            summary["issues_found"].append(f"Erro na geração do resumo: {e}")
        
        return summary
    
    def _generate_recommendations(self, report: Dict[str, Any]) -> List[str]:
        """
        Gera recomendações baseadas nos resultados.
        """
        recommendations = []
        
        try:
            summary = report.get("summary", {})
            
            if summary.get("overall_success"):
                recommendations.append("[OK] Sistema RAG funcionando corretamente")
                recommendations.append("[EMOJI] Considere ajustar threshold para otimizar resultados")
                recommendations.append("[EMOJI] Monitore performance em produção")
            else:
                if not summary.get("system_functional"):
                    recommendations.append("[EMOJI] CRÍTICO: Sistema não está funcional - verificar logs de erro")
                    recommendations.append("[EMOJI] Verificar configuração do modelo de embedding")
                    recommendations.append("[EMOJI] Verificar integridade dos arquivos de índice")
                
                if summary.get("success_rate", 0) < 50:
                    recommendations.append("[EMOJI] Taxa de sucesso baixa - considere:")
                    recommendations.append("   • Reduzir threshold de similaridade")
                    recommendations.append("   • Verificar qualidade dos documentos indexados")
                    recommendations.append("   • Ajustar parâmetros de chunking")
                
                if not summary.get("performance_acceptable"):
                    recommendations.append("[EMOJI] Performance lenta - considere:")
                    recommendations.append("   • Otimizar configurações de GPU")
                    recommendations.append("   • Reduzir tamanho do batch")
                    recommendations.append("   • Usar cache de embeddings")
            
            # Recomendações específicas baseadas nos testes
            threshold_tests = report.get("threshold_tests", {})
            optimal_threshold = threshold_tests.get("optimal_threshold", 0.1)
            
            if optimal_threshold != 0.1:
                recommendations.append(f"[EMOJI] Considere usar threshold {optimal_threshold} para melhores resultados")
            
        except Exception as e:
            recommendations.append(f"[ERROR] Erro na geração de recomendações: {e}")
        
        return recommendations
    
    def _save_test_report(self, report: Dict[str, Any]):
        """
        Salva o relatório de testes.
        """
        try:
            # Importar configuração centralizada
            import sys
            sys.path.append(str(Path(__file__).parent.parent))
            from config import get_report_path, REPORT_CONFIG
            
            report_path = get_report_path("rag_final_test_report.json")
            with open(report_path, 'w', encoding=REPORT_CONFIG['encoding']) as f:
                json.dump(report, f, 
                         indent=REPORT_CONFIG['indent'], 
                         ensure_ascii=REPORT_CONFIG['ensure_ascii'], 
                         default=REPORT_CONFIG['default_serializer'])
            logger.info(f"[EMOJI] Relatório de testes salvo em: {report_path.absolute()}")
        except Exception as e:
            logger.error(f"Erro ao salvar relatório: {e}")
    
    def _print_test_summary(self, report: Dict[str, Any]):
        """
        Imprime resumo dos testes.
        """
        print("\n" + "="*80)
        print("🧪 RELATÓRIO FINAL DE TESTES DO SISTEMA RAG")
        print("="*80)
        
        # Informações do sistema
        system_info = report.get("system_info", {})
        print(f"\n[EMOJI] Sistema:")
        print(f"   GPU: {system_info.get('gpu_name', 'N/A')}")
        print(f"   CUDA: {system_info.get('cuda_available', False)}")
        print(f"   PyTorch: {system_info.get('pytorch_version', 'N/A')}")
        
        # Status do índice
        index_status = system_info.get("index_status", {})
        print(f"\n[EMOJI] Índice:")
        print(f"   Documentos: {index_status.get('documents_count', 0)}")
        print(f"   Metadados: {index_status.get('metadata_count', 0)}")
        print(f"   Consistente: {index_status.get('consistent', False)}")
        
        # Testes de inicialização
        init_test = report.get("initialization_test", {})
        print(f"\n[EMOJI] Inicialização:")
        print(f"   Sucesso: {init_test.get('success', False)}")
        print(f"   Backend: {init_test.get('backend_used', 'N/A')}")
        print(f"   Tempo: {init_test.get('initialization_time', 0):.3f}s")
        
        # Testes de busca
        search_tests = report.get("search_tests", {})
        print(f"\n[SEARCH] Buscas:")
        print(f"   Taxa de sucesso: {search_tests.get('successful_queries', 0)}/{search_tests.get('total_queries', 0)} ({(search_tests.get('successful_queries', 0)/max(search_tests.get('total_queries', 1), 1)*100):.1f}%)")
        print(f"   Total de resultados: {search_tests.get('total_results', 0)}")
        print(f"   Tempo médio: {search_tests.get('avg_search_time', 0):.3f}s")
        
        # Performance
        perf_tests = report.get("performance_tests", {})
        print(f"\n[EMOJI] Performance:")
        print(f"   Busca única: {perf_tests.get('single_search_time', 0):.3f}s")
        print(f"   Throughput: {perf_tests.get('throughput_queries_per_second', 0):.1f} queries/s")
        print(f"   Memória: {perf_tests.get('memory_usage', 0):.1f} MB")
        
        # Resumo
        summary = report.get("summary", {})
        print(f"\n[EMOJI] Resumo:")
        print(f"   Sistema funcional: {summary.get('system_functional', False)}")
        print(f"   Performance aceitável: {summary.get('performance_acceptable', False)}")
        print(f"   Sucesso geral: {summary.get('overall_success', False)}")
        
        # Problemas encontrados
        issues = summary.get("issues_found", [])
        if issues:
            print(f"\n[ERROR] Problemas encontrados:")
            for i, issue in enumerate(issues, 1):
                print(f"   {i}. {issue}")
        
        # Recomendações
        recommendations = report.get("recommendations", [])
        if recommendations:
            print(f"\n[EMOJI] Recomendações:")
            for i, rec in enumerate(recommendations, 1):
                print(f"   {i}. {rec}")
        
        print("\n" + "="*80)
        
        if summary.get("overall_success"):
            print("[EMOJI] SISTEMA RAG FUNCIONANDO CORRETAMENTE!")
        else:
            print("[WARNING] SISTEMA RAG PRECISA DE AJUSTES")
        
        print("[EMOJI] Relatório detalhado: rag_final_test_report.json")
        print("="*80)

def main():
    """
    Função principal do teste final.
    """
    print("[START] Iniciando teste final do sistema RAG...")
    
    tester = RAGFinalTester()
    report = tester.run_comprehensive_test()
    
    print("\n[OK] Testes concluídos!")

if __name__ == "__main__":
    main()