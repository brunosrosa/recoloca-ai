#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Validação Completa do Sistema RAG - Recoloca.ai

Este script executa uma validação completa do sistema RAG incluindo:
- Teste de conectividade e performance
- Validação contextual específica para @AgenteM_DevFastAPI
- Teste de qualidade das respostas
- Verificação da infraestrutura

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import asyncio
import json
import logging
import sys
import time
from pathlib import Path
from typing import Dict, List, Any

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Adicionar core_logic ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from rag_infra.core_logic.rag_retriever import RAGRetriever
    from rag_infra.core_logic.rag_indexer import RAGIndexer
    from rag_infra.core_logic.embedding_model import EmbeddingModelManager as EmbeddingModel
except ImportError as e:
    logger.error(f"Erro ao importar módulos RAG: {e}")
    print(f"Erro detalhado: {e}")
    # Não usar sys.exit(1) em testes pytest
    raise ImportError(f"Falha ao importar módulos RAG: {e}")

class RAGValidator:
    """Classe para validação completa do sistema RAG"""
    
    def __init__(self):
        self.retriever = None
        self.indexer = None
        self.test_results = {
            "timestamp": time.time(),
            "tests": {},
            "overall_status": "pending",
            "recommendations": []
        }
    
    async def initialize_system(self) -> bool:
        """Inicializa o sistema RAG"""
        try:
            logger.info("🔄 Inicializando sistema RAG...")
            
            # Inicializar indexer
            self.indexer = RAGIndexer()
            
            # Inicializar retriever
            success = initialize_retriever(force_pytorch=True)
            if not success:
                raise Exception("Falha ao inicializar retriever")
            
            # Obter instância do retriever
            self.retriever = get_retriever(force_pytorch=True)
            
            if self.retriever is None:
                raise Exception("Falha ao obter instância do retriever")
            
            logger.info("✅ Sistema RAG inicializado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro na inicialização: {e}")
            self.test_results["tests"]["initialization"] = {
                "status": "failed",
                "error": str(e)
            }
            return False
    
    async def test_connectivity_performance(self) -> Dict[str, Any]:
        """Testa conectividade e performance do sistema"""
        logger.info("🔄 Testando conectividade e performance...")
        
        test_result = {
            "status": "pending",
            "response_times": [],
            "queries_tested": 0,
            "average_response_time": 0,
            "errors": []
        }
        
        # Queries de teste para performance
        test_queries = [
            "FastAPI backend development",
            "Supabase integration",
            "MVP requirements",
            "authentication system",
            "API endpoints"
        ]
        
        try:
            for query in test_queries:
                start_time = time.time()
                
                try:
                    results = self.retriever.search(query, top_k=3)
                    response_time = time.time() - start_time
                    
                    test_result["response_times"].append(response_time)
                    test_result["queries_tested"] += 1
                    
                    logger.info(f"Query '{query}': {response_time:.3f}s - {len(results)} resultados")
                    
                except Exception as e:
                    test_result["errors"].append(f"Query '{query}': {str(e)}")
                    logger.error(f"Erro na query '{query}': {e}")
            
            # Calcular métricas
            if test_result["response_times"]:
                test_result["average_response_time"] = sum(test_result["response_times"]) / len(test_result["response_times"])
                test_result["status"] = "success" if len(test_result["errors"]) == 0 else "partial"
            else:
                test_result["status"] = "failed"
            
            logger.info(f"✅ Teste de performance concluído: {test_result['average_response_time']:.3f}s médio")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"❌ Erro no teste de performance: {e}")
        
        return test_result
    
    async def test_context_validation(self) -> Dict[str, Any]:
        """Valida contexto específico para @AgenteM_DevFastAPI"""
        logger.info("🔄 Testando validação contextual para @AgenteM_DevFastAPI...")
        
        test_result = {
            "status": "pending",
            "context_queries": [],
            "quality_score": 0,
            "relevant_documents_found": 0
        }
        
        # Queries específicas para desenvolvimento FastAPI
        context_queries = [
            "FastAPI backend architecture Recoloca.ai",
            "Supabase authentication integration",
            "API endpoints specification",
            "Python development patterns",
            "MVP backend requirements"
        ]
        
        try:
            total_relevance = 0
            total_documents = 0
            
            for query in context_queries:
                try:
                    results = self.retriever.search(query, top_k=5)
                    
                    query_result = {
                        "query": query,
                        "results_count": len(results),
                        "top_documents": []
                    }
                    
                    for result in results[:3]:  # Top 3 resultados
                        # Converter SearchResult para dict se necessário
                        if hasattr(result, 'to_dict'):
                            result_dict = result.to_dict()
                        else:
                            result_dict = result
                        
                        query_result["top_documents"].append({
                            "document": result_dict.get("document", "Unknown"),
                            "score": result_dict.get("score", 0),
                            "content_preview": result_dict.get("content", "")[:100] + "..."
                        })
                    
                    test_result["context_queries"].append(query_result)
                    total_documents += len(results)
                    
                    # Calcular relevância baseada na presença de documentos
                    if len(results) > 0:
                        total_relevance += min(len(results), 5)  # Max 5 pontos por query
                    
                    logger.info(f"Query contextual '{query}': {len(results)} documentos encontrados")
                    
                except Exception as e:
                    logger.error(f"Erro na query contextual '{query}': {e}")
            
            # Calcular score de qualidade
            max_possible_score = len(context_queries) * 5
            test_result["quality_score"] = (total_relevance / max_possible_score) * 100 if max_possible_score > 0 else 0
            test_result["relevant_documents_found"] = total_documents
            
            if test_result["quality_score"] >= 70:
                test_result["status"] = "excellent"
            elif test_result["quality_score"] >= 50:
                test_result["status"] = "good"
            elif test_result["quality_score"] >= 30:
                test_result["status"] = "acceptable"
            else:
                test_result["status"] = "poor"
            
            logger.info(f"✅ Validação contextual concluída: {test_result['quality_score']:.1f}% qualidade")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["error"] = str(e)
            logger.error(f"❌ Erro na validação contextual: {e}")
        
        return test_result
    
    async def test_mcp_integration(self) -> Dict[str, Any]:
        """Testa a integração MCP"""
        logger.info("🔄 Testando integração MCP...")
        
        test_result = {
            "status": "pending",
            "mcp_server_available": False,
            "config_valid": False
        }
        
        try:
            # Verificar se o arquivo de configuração MCP existe
            mcp_config_path = Path(__file__).parent.parent / "config" / "trae_mcp_config.json"
            
            if mcp_config_path.exists():
                with open(mcp_config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    test_result["config_valid"] = True
                    test_result["config_content"] = config
                    logger.info("✅ Configuração MCP encontrada e válida")
            else:
                logger.warning("⚠️ Arquivo de configuração MCP não encontrado")
            
            # Verificar se o servidor MCP existe
            mcp_server_path = Path(__file__).parent / "mcp_server.py"
            
            if mcp_server_path.exists():
                test_result["mcp_server_available"] = True
                logger.info("✅ Servidor MCP disponível")
            else:
                logger.warning("⚠️ Servidor MCP não encontrado")
            
            # Determinar status geral
            if test_result["config_valid"] and test_result["mcp_server_available"]:
                test_result["status"] = "ready"
            elif test_result["mcp_server_available"]:
                test_result["status"] = "partial"
            else:
                test_result["status"] = "not_ready"
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["error"] = str(e)
            logger.error(f"❌ Erro no teste MCP: {e}")
        
        return test_result
    
    async def generate_recommendations(self) -> List[str]:
        """Gera recomendações baseadas nos testes"""
        recommendations = []
        
        # Analisar resultados dos testes
        connectivity = self.test_results["tests"].get("connectivity_performance", {})
        context = self.test_results["tests"].get("context_validation", {})
        mcp = self.test_results["tests"].get("mcp_integration", {})
        
        # Recomendações de performance
        if connectivity.get("average_response_time", 0) > 2.0:
            recommendations.append("🔴 [PERFORMANCE] Tempo de resposta alto. Considere otimizar o índice ou usar cache.")
        elif connectivity.get("average_response_time", 0) < 0.5:
            recommendations.append("🟢 [PERFORMANCE] Excelente tempo de resposta. Sistema otimizado.")
        
        # Recomendações de qualidade
        quality_score = context.get("quality_score", 0)
        if quality_score >= 70:
            recommendations.append("🟢 [QUALITY] Excelente qualidade contextual. RAG pronto para produção.")
        elif quality_score >= 50:
            recommendations.append("🟡 [QUALITY] Boa qualidade contextual. Considere adicionar mais documentos específicos.")
        else:
            recommendations.append("🔴 [QUALITY] Qualidade contextual baixa. Re-indexação ou revisão de documentos necessária.")
        
        # Recomendações MCP
        mcp_status = mcp.get("status", "unknown")
        if mcp_status == "ready":
            recommendations.append("🟢 [MCP] Sistema MCP pronto para integração com Trae IDE.")
        elif mcp_status == "partial":
            recommendations.append("🟡 [MCP] Sistema MCP parcialmente configurado. Verificar configuração.")
        else:
            recommendations.append("🔴 [MCP] Sistema MCP não configurado. Configuração necessária para Trae IDE.")
        
        return recommendations
    
    async def run_full_validation(self) -> Dict[str, Any]:
        """Executa validação completa do sistema RAG"""
        logger.info("🚀 Iniciando validação completa do sistema RAG...")
        
        # Inicializar sistema
        if not await self.initialize_system():
            self.test_results["overall_status"] = "failed"
            return self.test_results
        
        # Executar testes
        try:
            # Teste de conectividade e performance
            self.test_results["tests"]["connectivity_performance"] = await self.test_connectivity_performance()
            
            # Teste de validação contextual
            self.test_results["tests"]["context_validation"] = await self.test_context_validation()
            
            # Teste de integração MCP
            self.test_results["tests"]["mcp_integration"] = await self.test_mcp_integration()
            
            # Gerar recomendações
            self.test_results["recommendations"] = await self.generate_recommendations()
            
            # Determinar status geral
            failed_tests = [test for test in self.test_results["tests"].values() if test.get("status") == "failed"]
            
            if len(failed_tests) == 0:
                self.test_results["overall_status"] = "success"
            elif len(failed_tests) < len(self.test_results["tests"]) / 2:
                self.test_results["overall_status"] = "partial"
            else:
                self.test_results["overall_status"] = "failed"
            
            logger.info(f"✅ Validação completa concluída: {self.test_results['overall_status']}")
            
        except Exception as e:
            logger.error(f"❌ Erro durante validação: {e}")
            self.test_results["overall_status"] = "failed"
            self.test_results["error"] = str(e)
        
        return self.test_results
    
    def save_results(self, filename: str = "utils/rag_validation_results.json"):
        """Salva os resultados da validação"""
        try:
            results_path = Path(__file__).parent / filename
            with open(results_path, 'w', encoding='utf-8') as f:
                json.dump(self.test_results, f, indent=2, ensure_ascii=False)
            logger.info(f"📄 Resultados salvos em: {results_path}")
        except Exception as e:
            logger.error(f"❌ Erro ao salvar resultados: {e}")
    
    def print_summary(self):
        """Imprime resumo dos resultados"""
        print("\n" + "="*60)
        print("📋 RESUMO DA VALIDAÇÃO RAG - RECOLOCA.AI")
        print("="*60)
        
        print(f"\n🎯 STATUS GERAL: {self.test_results['overall_status'].upper()}")
        
        print("\n📊 RESULTADOS DOS TESTES:")
        for test_name, test_result in self.test_results["tests"].items():
            status_icon = {
                "success": "✅",
                "excellent": "🌟",
                "good": "✅",
                "acceptable": "🟡",
                "partial": "🟡",
                "poor": "🔴",
                "failed": "❌",
                "ready": "✅",
                "not_ready": "❌"
            }.get(test_result.get("status", "unknown"), "❓")
            
            print(f"  {status_icon} {test_name.replace('_', ' ').title()}: {test_result.get('status', 'unknown')}")
        
        print("\n💡 RECOMENDAÇÕES:")
        for rec in self.test_results.get("recommendations", []):
            print(f"  {rec}")
        
        print("\n" + "="*60)

async def main():
    """Função principal"""
    validator = RAGValidator()
    
    # Executar validação completa
    results = await validator.run_full_validation()
    
    # Salvar resultados
    validator.save_results()
    
    # Imprimir resumo
    validator.print_summary()
    
    # Retornar código de saída baseado no status
    if results["overall_status"] == "success":
        print("\n🎉 Sistema RAG totalmente operacional!")
        return 0
    elif results["overall_status"] == "partial":
        print("\n⚠️ Sistema RAG parcialmente operacional. Verificar recomendações.")
        return 1
    else:
        print("\n❌ Sistema RAG com problemas críticos. Correções necessárias.")
        return 2

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)