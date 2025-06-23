# -*- coding: utf-8 -*-
"""
Teste de Integração dos Módulos Consolidados - RAG Infra
Para o projeto Recoloca.ai

Este script valida a integração de todos os módulos consolidados:
- core_logic: Lógica principal do RAG
- diagnostics: Diagnósticos e correções
- utils: Utilitários e manutenção
- server: Servidor MCP
- setup: Configuração e inicialização

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import os
import sys
import time
import json
import logging
import traceback
from pathlib import Path
from typing import List, Dict, Any, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Adicionar path do projeto
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root.parent))

class ConsolidatedModulesIntegrationTester:
    """Testador de integração dos módulos consolidados."""
    
    def __init__(self):
        self.results = {
            "timestamp": time.time(),
            "test_session_id": f"integration_test_{int(time.time())}",
            "modules_tested": [],
            "tests": {},
            "summary": {
                "total_tests": 0,
                "passed": 0,
                "failed": 0,
                "warnings": 0
            },
            "performance_metrics": {},
            "recommendations": []
        }
        self.test_queries = [
            "Como implementar autenticação FastAPI?",
            "Configurar banco de dados PostgreSQL",
            "Implementar sistema de cache Redis",
            "Deploy com Docker",
            "Testes automatizados Python"
        ]
    
    def test_core_logic_module(self) -> bool:
        """Testa o módulo core_logic consolidado."""
        logger.info("[EMOJI] Testando módulo core_logic...")
        
        test_result = {
            "module": "src/core/core_logic",
            "status": "unknown",
            "components": {},
            "errors": [],
            "warnings": []
        }
        
        try:
            # Teste 1: Importação do RAGRetriever
            try:
                from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
                test_result["components"]["rag_retriever"] = "success"
                logger.info("  [OK] RAGRetriever importado com sucesso")
            except Exception as e:
                test_result["components"]["rag_retriever"] = f"error: {str(e)}"
                test_result["errors"].append(f"RAGRetriever import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar RAGRetriever: {e}")
            
            # Teste 2: Importação do PyTorchGPURetriever
            try:
                from rag_infra.src.core.core_logic.pytorch_gpu_retriever import PyTorchGPURetriever
                test_result["components"]["pytorch_gpu_retriever"] = "success"
                logger.info("  [OK] PyTorchGPURetriever importado com sucesso")
            except Exception as e:
                test_result["components"]["pytorch_gpu_retriever"] = f"error: {str(e)}"
                test_result["errors"].append(f"PyTorchGPURetriever import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar PyTorchGPURetriever: {e}")
            
            # Teste 3: Importação do embedding_model
            try:
                from rag_infra.src.core.embedding_model import initialize_embedding_model
                test_result["components"]["embedding_model"] = "success"
                logger.info("  [OK] embedding_model importado com sucesso")
            except Exception as e:
                test_result["components"]["embedding_model"] = f"error: {str(e)}"
                test_result["errors"].append(f"embedding_model import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar embedding_model: {e}")
            
            # Teste 4: Inicialização do RAGRetriever
            try:
                retriever = RAGRetriever()
                backend_info = retriever.get_backend_info()
                test_result["components"]["rag_initialization"] = {
                    "status": "success",
                    "backend_info": backend_info
                }
                logger.info(f"  [OK] RAGRetriever inicializado - Backend: {backend_info.get('recommended_backend')}")
            except Exception as e:
                test_result["components"]["rag_initialization"] = f"error: {str(e)}"
                test_result["errors"].append(f"RAG initialization: {str(e)}")
                logger.error(f"  [ERROR] Erro na inicialização do RAG: {e}")
            
            # Determinar status geral
            if len(test_result["errors"]) == 0:
                test_result["status"] = "success"
            elif len(test_result["errors"]) < len(test_result["components"]):
                test_result["status"] = "partial"
            else:
                test_result["status"] = "failed"
            
            self.results["tests"]["src/core/core_logic"] = test_result
            self.results["modules_tested"].append("src/core/core_logic")
            
            return test_result["status"] in ["success", "partial"]
            
        except Exception as e:
            logger.error(f"[ERROR] Erro crítico no teste core_logic: {e}")
            test_result["status"] = "critical_error"
            test_result["errors"].append(f"Critical error: {str(e)}")
            self.results["tests"]["src/core/core_logic"] = test_result
            return False
    
    def test_diagnostics_module(self) -> bool:
        """Testa o módulo diagnostics consolidado."""
        logger.info("[SEARCH] Testando módulo diagnostics...")
        
        test_result = {
            "module": "diagnostics",
            "status": "unknown",
            "components": {},
            "errors": [],
            "warnings": []
        }
        
        try:
            # Teste 1: Importação do rag_diagnostics
            try:
                from diagnostics.rag_diagnostics import RAGDiagnosticsRunner
                test_result["components"]["rag_diagnostics"] = "success"
                logger.info("  [OK] rag_diagnostics importado com sucesso")
            except Exception as e:
                test_result["components"]["rag_diagnostics"] = f"error: {str(e)}"
                test_result["errors"].append(f"rag_diagnostics import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar rag_diagnostics: {e}")
            
            # Teste 2: Importação do rag_fixes
            try:
                from diagnostics.rag_fixes import RAGFixesRunner
                test_result["components"]["rag_fixes"] = "success"
                logger.info("  [OK] rag_fixes importado com sucesso")
            except Exception as e:
                test_result["components"]["rag_fixes"] = f"error: {str(e)}"
                test_result["errors"].append(f"rag_fixes import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar rag_fixes: {e}")
            
            # Teste 3: Execução de diagnóstico básico
            try:
                if "rag_diagnostics" in test_result["components"] and test_result["components"]["rag_diagnostics"] == "success":
                    diagnostics = RAGDiagnosticsRunner()
                    basic_check = diagnostics.run_all_diagnostics()
                    test_result["components"]["basic_diagnostics"] = {
                        "status": "success",
                        "result": basic_check
                    }
                    logger.info("  [OK] Diagnóstico básico executado com sucesso")
                else:
                    test_result["warnings"].append("Diagnóstico básico pulado devido a erro de importação")
            except Exception as e:
                test_result["components"]["basic_diagnostics"] = f"error: {str(e)}"
                test_result["errors"].append(f"basic_diagnostics execution: {str(e)}")
                logger.error(f"  [ERROR] Erro na execução do diagnóstico: {e}")
            
            # Determinar status geral
            if len(test_result["errors"]) == 0:
                test_result["status"] = "success"
            elif len(test_result["errors"]) < len(test_result["components"]):
                test_result["status"] = "partial"
            else:
                test_result["status"] = "failed"
            
            self.results["tests"]["diagnostics"] = test_result
            self.results["modules_tested"].append("diagnostics")
            
            return test_result["status"] in ["success", "partial"]
            
        except Exception as e:
            logger.error(f"[ERROR] Erro crítico no teste diagnostics: {e}")
            test_result["status"] = "critical_error"
            test_result["errors"].append(f"Critical error: {str(e)}")
            self.results["tests"]["diagnostics"] = test_result
            return False
    
    def test_utils_module(self) -> bool:
        """Testa o módulo utils consolidado."""
        logger.info("[EMOJI] Testando módulo utils...")
        
        test_result = {
            "module": "utils",
            "status": "unknown",
            "components": {},
            "errors": [],
            "warnings": []
        }
        
        try:
            # Teste 1: Importação do rag_utilities
            try:
                from utils.rag_utilities import RAGUtilitiesRunner
                test_result["components"]["rag_utilities"] = "success"
                logger.info("  [OK] rag_utilities importado com sucesso")
            except Exception as e:
                test_result["components"]["rag_utilities"] = f"error: {str(e)}"
                test_result["errors"].append(f"rag_utilities import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar rag_utilities: {e}")
            
            # Teste 2: Importação do rag_maintenance
            try:
                from utils.rag_maintenance import RAGMaintenance
                test_result["components"]["rag_maintenance"] = "success"
                logger.info("  [OK] rag_maintenance importado com sucesso")
            except Exception as e:
                test_result["components"]["rag_maintenance"] = f"error: {str(e)}"
                test_result["errors"].append(f"rag_maintenance import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar rag_maintenance: {e}")
            
            # Teste 3: Verificação de utilitários básicos
            try:
                if "rag_utilities" in test_result["components"] and test_result["components"]["rag_utilities"] == "success":
                    utilities = RAGUtilitiesRunner()
                    system_info = utilities.run_all_utilities()
                    test_result["components"]["system_info"] = {
                        "status": "success",
                        "info": system_info
                    }
                    logger.info("  [OK] Informações do sistema obtidas com sucesso")
                else:
                    test_result["warnings"].append("System info pulado devido a erro de importação")
            except Exception as e:
                test_result["components"]["system_info"] = f"error: {str(e)}"
                test_result["errors"].append(f"system_info execution: {str(e)}")
                logger.error(f"  [ERROR] Erro ao obter informações do sistema: {e}")
            
            # Determinar status geral
            if len(test_result["errors"]) == 0:
                test_result["status"] = "success"
            elif len(test_result["errors"]) < len(test_result["components"]):
                test_result["status"] = "partial"
            else:
                test_result["status"] = "failed"
            
            self.results["tests"]["utils"] = test_result
            self.results["modules_tested"].append("utils")
            
            return test_result["status"] in ["success", "partial"]
            
        except Exception as e:
            logger.error(f"[ERROR] Erro crítico no teste utils: {e}")
            test_result["status"] = "critical_error"
            test_result["errors"].append(f"Critical error: {str(e)}")
            self.results["tests"]["utils"] = test_result
            return False
    
    def test_server_module(self) -> bool:
        """Testa o módulo server consolidado."""
        logger.info("[EMOJI] Testando módulo server...")
        
        test_result = {
            "module": "server",
            "status": "unknown",
            "components": {},
            "errors": [],
            "warnings": []
        }
        
        try:
            # Teste 1: Importação do mcp_server
            try:
                from server.mcp_server import handle_list_tools, handle_call_tool
                test_result["components"]["mcp_server"] = "success"
                logger.info("  [OK] mcp_server importado com sucesso")
            except Exception as e:
                test_result["components"]["mcp_server"] = f"error: {str(e)}"
                test_result["errors"].append(f"mcp_server import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar mcp_server: {e}")
            
            # Teste 2: Verificação de configuração do servidor
            try:
                if "mcp_server" in test_result["components"] and test_result["components"]["mcp_server"] == "success":
                    # Verificar se as funções do servidor estão disponíveis
                    import asyncio
                    tools = asyncio.run(handle_list_tools())
                    test_result["components"]["server_config"] = {
                        "status": "success",
                        "tools_count": len(tools)
                    }
                    logger.info(f"  [OK] Servidor MCP configurado - {len(tools)} ferramentas disponíveis")
                else:
                    test_result["warnings"].append("Configuração do servidor pulada devido a erro de importação")
            except Exception as e:
                test_result["components"]["server_config"] = f"error: {str(e)}"
                test_result["errors"].append(f"server_config validation: {str(e)}")
                logger.error(f"  [ERROR] Erro na configuração do servidor: {e}")
            
            # Determinar status geral
            if len(test_result["errors"]) == 0:
                test_result["status"] = "success"
            elif len(test_result["errors"]) < len(test_result["components"]):
                test_result["status"] = "partial"
            else:
                test_result["status"] = "failed"
            
            self.results["tests"]["server"] = test_result
            self.results["modules_tested"].append("server")
            
            return test_result["status"] in ["success", "partial"]
            
        except Exception as e:
            logger.error(f"[ERROR] Erro crítico no teste server: {e}")
            test_result["status"] = "critical_error"
            test_result["errors"].append(f"Critical error: {str(e)}")
            self.results["tests"]["server"] = test_result
            return False
    
    def test_setup_module(self) -> bool:
        """Testa o módulo setup consolidado."""
        logger.info("[EMOJI] Testando módulo setup...")
        
        test_result = {
            "module": "setup",
            "status": "unknown",
            "components": {},
            "errors": [],
            "warnings": []
        }
        
        try:
            # Teste 1: Importação do setup_rag
            try:
                from setup.setup_rag import RAGSetup
                test_result["components"]["setup_rag"] = "success"
                logger.info("  [OK] setup_rag importado com sucesso")
            except Exception as e:
                test_result["components"]["setup_rag"] = f"error: {str(e)}"
                test_result["errors"].append(f"setup_rag import: {str(e)}")
                logger.error(f"  [ERROR] Erro ao importar setup_rag: {e}")
            
            # Teste 2: Verificação de configuração do sistema
            try:
                if "setup_rag" in test_result["components"] and test_result["components"]["setup_rag"] == "success":
                    # Verificar se o setup pode ser executado (modo dry-run)
                    setup = RAGSetup(verbose=True)
                    gpu_available, gpu_info = setup.check_gpu_availability()
                    test_result["components"]["setup_validation"] = {
                        "status": "success",
                        "gpu_available": gpu_available,
                        "gpu_info": gpu_info
                    }
                    logger.info(f"  [OK] Validação do setup executada - GPU: {gpu_available}")
                else:
                    test_result["warnings"].append("Validação do setup pulada devido a erro de importação")
            except Exception as e:
                test_result["components"]["setup_validation"] = f"error: {str(e)}"
                test_result["errors"].append(f"setup_validation execution: {str(e)}")
                logger.error(f"  [ERROR] Erro na validação do setup: {e}")
            
            # Determinar status geral
            if len(test_result["errors"]) == 0:
                test_result["status"] = "success"
            elif len(test_result["errors"]) < len(test_result["components"]):
                test_result["status"] = "partial"
            else:
                test_result["status"] = "failed"
            
            self.results["tests"]["setup"] = test_result
            self.results["modules_tested"].append("setup")
            
            return test_result["status"] in ["success", "partial"]
            
        except Exception as e:
            logger.error(f"[ERROR] Erro crítico no teste setup: {e}")
            test_result["status"] = "critical_error"
            test_result["errors"].append(f"Critical error: {str(e)}")
            self.results["tests"]["setup"] = test_result
            return False
    
    def test_integration_flow(self) -> bool:
        """Testa o fluxo de integração completo entre módulos."""
        logger.info("[EMOJI] Testando fluxo de integração completo...")
        
        test_result = {
            "module": "integration_flow",
            "status": "unknown",
            "components": {},
            "errors": [],
            "warnings": [],
            "performance": {}
        }
        
        try:
            start_time = time.time()
            
            # Teste 1: Inicialização completa do sistema
            try:
                from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
                retriever = RAGRetriever()
                
                # Testar consulta simples
                query = "Como implementar autenticação FastAPI?"
                start_query = time.time()
                results = retriever.search(query, top_k=3)
                query_time = time.time() - start_query
                
                test_result["components"]["full_query"] = {
                    "status": "success",
                    "query": query,
                    "results_count": len(results),
                    "query_time": query_time
                }
                test_result["performance"]["query_time"] = query_time
                
                logger.info(f"  [OK] Consulta executada em {query_time:.3f}s - {len(results)} resultados")
                
            except Exception as e:
                test_result["components"]["full_query"] = f"error: {str(e)}"
                test_result["errors"].append(f"full_query execution: {str(e)}")
                logger.error(f"  [ERROR] Erro na consulta completa: {e}")
            
            # Teste 2: Verificação de diagnósticos
            try:
                from diagnostics.rag_diagnostics import RAGDiagnosticsRunner
                diagnostics = RAGDiagnosticsRunner()
                
                start_diag = time.time()
                diag_result = diagnostics.run_all_diagnostics()
                diag_time = time.time() - start_diag
                
                test_result["components"]["diagnostics_integration"] = {
                    "status": "success",
                    "result": diag_result,
                    "diagnostics_time": diag_time
                }
                test_result["performance"]["diagnostics_time"] = diag_time
                
                logger.info(f"  [OK] Diagnósticos executados em {diag_time:.3f}s")
                
            except Exception as e:
                test_result["components"]["diagnostics_integration"] = f"error: {str(e)}"
                test_result["errors"].append(f"diagnostics_integration execution: {str(e)}")
                logger.error(f"  [ERROR] Erro nos diagnósticos integrados: {e}")
            
            # Teste 3: Verificação de utilitários
            try:
                from utils.rag_utilities import RAGUtilitiesRunner
                utilities = RAGUtilitiesRunner()
                
                start_utils = time.time()
                system_info = utilities.run_all_utilities()
                utils_time = time.time() - start_utils
                
                test_result["components"]["utilities_integration"] = {
                    "status": "success",
                    "system_info": system_info,
                    "utilities_time": utils_time
                }
                test_result["performance"]["utilities_time"] = utils_time
                
                logger.info(f"  [OK] Utilitários executados em {utils_time:.3f}s")
                
            except Exception as e:
                test_result["components"]["utilities_integration"] = f"error: {str(e)}"
                test_result["errors"].append(f"utilities_integration execution: {str(e)}")
                logger.error(f"  [ERROR] Erro nos utilitários integrados: {e}")
            
            total_time = time.time() - start_time
            test_result["performance"]["total_integration_time"] = total_time
            
            # Determinar status geral
            if len(test_result["errors"]) == 0:
                test_result["status"] = "success"
            elif len(test_result["errors"]) < len(test_result["components"]):
                test_result["status"] = "partial"
            else:
                test_result["status"] = "failed"
            
            self.results["tests"]["integration_flow"] = test_result
            self.results["performance_metrics"] = test_result["performance"]
            
            logger.info(f"[EMOJI] Fluxo de integração concluído em {total_time:.3f}s")
            
            return test_result["status"] in ["success", "partial"]
            
        except Exception as e:
            logger.error(f"[ERROR] Erro crítico no fluxo de integração: {e}")
            test_result["status"] = "critical_error"
            test_result["errors"].append(f"Critical error: {str(e)}")
            self.results["tests"]["integration_flow"] = test_result
            return False
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Executa todos os testes de integração."""
        logger.info("[START] Iniciando testes de integração dos módulos consolidados...")
        
        start_time = time.time()
        
        # Lista de testes a executar
        tests = [
            ("src/core/core_logic", self.test_core_logic_module),
            ("diagnostics", self.test_diagnostics_module),
            ("utils", self.test_utils_module),
            ("server", self.test_server_module),
            ("setup", self.test_setup_module),
            ("integration_flow", self.test_integration_flow)
        ]
        
        # Executar testes
        for test_name, test_func in tests:
            try:
                logger.info(f"\n{'='*60}")
                logger.info(f"Executando teste: {test_name}")
                logger.info(f"{'='*60}")
                
                success = test_func()
                
                if success:
                    self.results["summary"]["passed"] += 1
                    logger.info(f"[OK] Teste {test_name} PASSOU")
                else:
                    self.results["summary"]["failed"] += 1
                    logger.error(f"[ERROR] Teste {test_name} FALHOU")
                
                self.results["summary"]["total_tests"] += 1
                
            except Exception as e:
                logger.error(f"[EMOJI] Erro crítico no teste {test_name}: {e}")
                self.results["summary"]["failed"] += 1
                self.results["summary"]["total_tests"] += 1
        
        # Calcular métricas finais
        total_time = time.time() - start_time
        self.results["total_execution_time"] = total_time
        
        # Gerar recomendações
        self._generate_recommendations()
        
        # Log do resumo
        self._log_summary()
        
        return self.results
    
    def _generate_recommendations(self):
        """Gera recomendações baseadas nos resultados dos testes."""
        recommendations = []
        
        # Análise geral
        total_tests = self.results["summary"]["total_tests"]
        passed_tests = self.results["summary"]["passed"]
        failed_tests = self.results["summary"]["failed"]
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        if success_rate >= 90:
            recommendations.append("[OK] Excelente! Todos os módulos consolidados estão funcionando corretamente.")
            recommendations.append("[START] Sistema pronto para transição para Fase 1 do projeto.")
        elif success_rate >= 70:
            recommendations.append("[WARNING] Boa integração, mas alguns módulos precisam de atenção.")
            recommendations.append("[EMOJI] Revisar módulos com falhas antes da Fase 1.")
        else:
            recommendations.append("[ERROR] Problemas críticos de integração detectados.")
            recommendations.append("[EMOJI] Correções urgentes necessárias antes de prosseguir.")
        
        # Análise de performance
        if "query_time" in self.results.get("performance_metrics", {}):
            query_time = self.results["performance_metrics"]["query_time"]
            if query_time < 1.0:
                recommendations.append(f"[EMOJI] Excelente performance de consulta: {query_time:.3f}s")
            elif query_time < 3.0:
                recommendations.append(f"[OK] Boa performance de consulta: {query_time:.3f}s")
            else:
                recommendations.append(f"[WARNING] Performance de consulta pode ser melhorada: {query_time:.3f}s")
        
        # Análise por módulo
        for module_name, test_result in self.results["tests"].items():
            if test_result["status"] == "failed":
                recommendations.append(f"[EMOJI] Módulo {module_name}: Requer correção imediata")
            elif test_result["status"] == "partial":
                recommendations.append(f"🟡 Módulo {module_name}: Alguns componentes precisam de atenção")
            elif test_result["status"] == "success":
                recommendations.append(f"🟢 Módulo {module_name}: Funcionando perfeitamente")
        
        self.results["recommendations"] = recommendations
    
    def _log_summary(self):
        """Registra o resumo dos testes."""
        logger.info("\n" + "="*80)
        logger.info("[EMOJI] RESUMO DOS TESTES DE INTEGRAÇÃO DOS MÓDULOS CONSOLIDADOS")
        logger.info("="*80)
        
        summary = self.results["summary"]
        logger.info(f"Total de testes: {summary['total_tests']}")
        logger.info(f"Testes aprovados: {summary['passed']}")
        logger.info(f"Testes falharam: {summary['failed']}")
        
        success_rate = (summary['passed'] / summary['total_tests'] * 100) if summary['total_tests'] > 0 else 0
        logger.info(f"Taxa de sucesso: {success_rate:.1f}%")
        
        logger.info(f"Tempo total de execução: {self.results.get('total_execution_time', 0):.3f}s")
        
        logger.info("\n[EMOJI] Módulos testados:")
        for module in self.results["modules_tested"]:
            status = self.results["tests"][module]["status"]
            status_icon = {
                "success": "[OK]",
                "partial": "[WARNING]",
                "failed": "[ERROR]",
                "critical_error": "[EMOJI]"
            }.get(status, "[EMOJI]")
            logger.info(f"  {status_icon} {module}: {status}")
        
        logger.info("\n[EMOJI] Recomendações:")
        for rec in self.results["recommendations"]:
            logger.info(f"  {rec}")
        
        logger.info("="*80)
    
    def _make_serializable(self, obj):
        """Converte objetos não serializáveis em dicionários"""
        if hasattr(obj, '__dict__'):
            return {k: self._make_serializable(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, dict):
            return {k: self._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_serializable(item) for item in obj]
        elif isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        else:
            return str(obj)
    
    def save_results(self, filename: Optional[str] = None) -> str:
        """Salva os resultados dos testes em arquivo JSON."""
        if filename is None:
            timestamp = int(time.time())
            filename = f"consolidated_modules_integration_test_{timestamp}.json"
        
        results_dir = Path(__file__).parent.parent / "results_and_reports"
        results_dir.mkdir(exist_ok=True)
        
        filepath = results_dir / filename
        
        # Converter objetos não serializáveis
        serializable_results = self._make_serializable(self.results)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(serializable_results, f, indent=2, ensure_ascii=False)
        
        logger.info(f"[EMOJI] Resultados salvos em: {filepath}")
        return str(filepath)

def main():
    """Função principal para executar os testes."""
    try:
        # Criar e executar tester
        tester = ConsolidatedModulesIntegrationTester()
        results = tester.run_all_tests()
        
        # Salvar resultados
        results_file = tester.save_results()
        
        # Determinar código de saída
        success_rate = (results["summary"]["passed"] / results["summary"]["total_tests"] * 100) if results["summary"]["total_tests"] > 0 else 0
        
        if success_rate >= 70:
            logger.info("[EMOJI] Testes de integração concluídos com sucesso!")
            return 0
        else:
            logger.error("[EMOJI] Testes de integração falharam!")
            return 1
            
    except Exception as e:
        logger.error(f"[EMOJI] Erro crítico na execução dos testes: {e}")
        logger.error(traceback.format_exc())
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)