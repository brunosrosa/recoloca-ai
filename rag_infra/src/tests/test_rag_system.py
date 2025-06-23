#!/usr/bin/env python3
"""
Teste Completo do Sistema RAG

Este script testa todas as funcionalidades do sistema RAG:
- Indexação de documentos
- Busca semântica
- Servidor MCP

Autor: Sistema RAG Recoloca.ai
Data: Junho 2025
"""

import os
import sys
import time
import json
import asyncio
import logging
from pathlib import Path
from typing import List, Dict, Any



from constants import (
    SOURCE_DOCUMENTS_DIR,
    FAISS_INDEX_DIR,
    LOGS_DIR,
    create_directories
)
from rag_infra.src.core.rag_indexer import RAGIndexer
from rag_infra.src.core.rag_retriever import RAGRetriever
from rag_infra.src.core.embedding_model import initialize_embedding_model, get_embedding_manager

class RAGSystemTester:
    """
    Classe para testar o sistema RAG completo.
    """
    
    def __init__(self, force_cpu: bool = False):
        """
        Inicializa o testador.
        
        Args:
            force_cpu: Se True, força o uso de CPU
        """
        self.force_cpu = force_cpu
        self.test_results = []
        self.start_time = time.time()
    
    def log_test(self, test_name: str, success: bool, message: str = "", duration: float = 0.0):
        """
        Registra resultado de um teste.
        
        Args:
            test_name: Nome do teste
            success: Se o teste passou
            message: Mensagem adicional
            duration: Duração do teste em segundos
        """
        status = "[OK] PASSOU" if success else "[ERROR] FALHOU"
        duration_str = f" ({duration:.2f}s)" if duration > 0 else ""
        
        result = {
            "test": test_name,
            "success": success,
            "message": message,
            "duration": duration
        }
        
        self.test_results.append(result)
        print(f"{status} {test_name}{duration_str}")
        if message:
            print(f"   [EMOJI] {message}")
    
    def test_environment(self) -> bool:
        """
        Testa o ambiente e dependências.
        
        Returns:
            bool: True se o ambiente está OK
        """
        print("\n[SEARCH] Testando Ambiente...")
        start_time = time.time()
        
        try:
            # Testar importações
            import faiss
            import numpy as np
            import torch
            from sentence_transformers import SentenceTransformer
            from langchain.embeddings import HuggingFaceEmbeddings
            
            # Verificar CUDA
            cuda_available = torch.cuda.is_available()
            device_info = f"CUDA: {cuda_available}"
            if cuda_available:
                device_info += f", GPU: {torch.cuda.get_device_name()}"
            
            # Verificar diretórios
            source_exists = SOURCE_DOCUMENTS_DIR.exists()
            index_exists = FAISS_INDEX_DIR.exists()
            
            duration = time.time() - start_time
            
            if source_exists:
                self.log_test(
                    "Ambiente e Dependências", 
                    True, 
                    f"{device_info}, Diretórios: OK", 
                    duration
                )
                return True
            else:
                self.log_test(
                    "Ambiente e Dependências", 
                    False, 
                    f"Diretório de documentos não encontrado: {SOURCE_DOCUMENTS_DIR}", 
                    duration
                )
                return False
                
        except ImportError as e:
            duration = time.time() - start_time
            self.log_test(
                "Ambiente e Dependências", 
                False, 
                f"Dependência faltando: {e}", 
                duration
            )
            return False
        except Exception as e:
            duration = time.time() - start_time
            self.log_test(
                "Ambiente e Dependências", 
                False, 
                f"Erro inesperado: {e}", 
                duration
            )
            return False
    
    def test_embedding_model(self) -> bool:
        """
        Testa o modelo de embedding.
        
        Returns:
            bool: True se o modelo funciona
        """
        print("\n🤖 Testando Modelo de Embedding...")
        start_time = time.time()
        
        try:
            # Inicializar modelo
            success = initialize_embedding_model(force_cpu=self.force_cpu)
            
            if not success:
                duration = time.time() - start_time
                self.log_test(
                    "Modelo de Embedding", 
                    False, 
                    "Falha na inicialização", 
                    duration
                )
                return False
            
            # Testar embedding
            manager = get_embedding_manager()
            test_text = "Este é um teste do modelo de embedding"
            embedding = manager.embed_query(test_text)
            
            if embedding is not None and len(embedding) > 0:
                duration = time.time() - start_time
                self.log_test(
                    "Modelo de Embedding", 
                    True, 
                    f"Dimensão: {len(embedding)}, Modelo: {manager.model_name}", 
                    duration
                )
                return True
            else:
                duration = time.time() - start_time
                self.log_test(
                    "Modelo de Embedding", 
                    False, 
                    "Embedding vazio ou None", 
                    duration
                )
                return False
                
        except Exception as e:
            duration = time.time() - start_time
            self.log_test(
                "Modelo de Embedding", 
                False, 
                f"Erro: {e}", 
                duration
            )
            return False
    
    def test_indexing(self) -> bool:
        """
        Testa o processo de indexação.
        
        Returns:
            bool: True se a indexação funciona
        """
        print("\n[EMOJI] Testando Indexação...")
        start_time = time.time()
        
        try:
            # Criar indexer
            indexer = RAGIndexer(force_cpu=self.force_cpu)
            
            # Executar indexação
            success = indexer.index_documents()
            
            if success:
                # Verificar arquivos criados
                index_file = FAISS_INDEX_DIR / "faiss_index.bin"
                docs_file = FAISS_INDEX_DIR / "documents.json"
                meta_file = FAISS_INDEX_DIR / "metadata.json"
                
                files_exist = all([index_file.exists(), docs_file.exists(), meta_file.exists()])
                
                if files_exist:
                    # Verificar conteúdo
                    with open(meta_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    
                    total_docs = metadata.get("total_documents", 0)
                    total_chunks = metadata.get("total_chunks", 0)
                    
                    duration = time.time() - start_time
                    self.log_test(
                        "Indexação", 
                        True, 
                        f"Documentos: {total_docs}, Chunks: {total_chunks}", 
                        duration
                    )
                    return True
                else:
                    duration = time.time() - start_time
                    self.log_test(
                        "Indexação", 
                        False, 
                        "Arquivos de índice não criados", 
                        duration
                    )
                    return False
            else:
                duration = time.time() - start_time
                self.log_test(
                    "Indexação", 
                    False, 
                    "Falha no processo de indexação", 
                    duration
                )
                return False
                
        except Exception as e:
            duration = time.time() - start_time
            self.log_test(
                "Indexação", 
                False, 
                f"Erro: {e}", 
                duration
            )
            return False
    
    def test_retrieval(self) -> bool:
        """
        Testa o sistema de retrieval.
        
        Returns:
            bool: True se o retrieval funciona
        """
        print("\n[SEARCH] Testando Retrieval...")
        start_time = time.time()
        
        try:
            # Inicializar retriever
            success = initialize_retriever(force_cpu=self.force_cpu)
            
            if not success:
                duration = time.time() - start_time
                self.log_test(
                    "Retrieval", 
                    False, 
                    "Falha na inicialização do retriever", 
                    duration
                )
                return False
            
            retriever = get_retriever()
            
            # Teste de consultas
            test_queries = [
                "Como implementar autenticação no FastAPI?",
                "Arquitetura do sistema Recoloca.ai",
                "Requisitos funcionais do projeto",
                "Agentes de IA e mentores"
            ]
            
            total_results = 0
            successful_queries = 0
            
            for query in test_queries:
                try:
                    results = retriever.search(query, top_k=3)
                    if results:
                        total_results += len(results)
                        successful_queries += 1
                except Exception as e:
                    print(f"   [WARNING] Erro na consulta '{query}': {e}")
            
            # Teste de busca por documento
            doc_results = retriever.search_by_document("README", top_k=5)
            
            # Teste de listagem de documentos
            doc_list = retriever.get_document_list()
            
            duration = time.time() - start_time
            
            if successful_queries > 0 and total_results > 0:
                self.log_test(
                    "Retrieval", 
                    True, 
                    f"Consultas: {successful_queries}/{len(test_queries)}, Resultados: {total_results}, Documentos: {len(doc_list)}", 
                    duration
                )
                return True
            else:
                self.log_test(
                    "Retrieval", 
                    False, 
                    "Nenhum resultado encontrado nas consultas", 
                    duration
                )
                return False
                
        except Exception as e:
            duration = time.time() - start_time
            self.log_test(
                "Retrieval", 
                False, 
                f"Erro: {e}", 
                duration
            )
            return False
    
    def test_mcp_server_import(self) -> bool:
        """
        Testa a importação do servidor MCP.
        
        Returns:
            bool: True se o servidor pode ser importado
        """
        print("\n[EMOJI] Testando MCP Server...")
        start_time = time.time()
        
        try:
            # Tentar importar o servidor MCP
            import mcp_server
            
            # Verificar se as funções principais existem
            required_functions = [
                'handle_list_tools',
                'handle_call_tool',
                'main'
            ]
            
            missing_functions = []
            for func_name in required_functions:
                if not hasattr(mcp_server, func_name) and not hasattr(mcp_server.server, func_name):
                    missing_functions.append(func_name)
            
            duration = time.time() - start_time
            
            if not missing_functions:
                self.log_test(
                    "MCP Server", 
                    True, 
                    "Importação e estrutura OK", 
                    duration
                )
                return True
            else:
                self.log_test(
                    "MCP Server", 
                    False, 
                    f"Funções faltando: {missing_functions}", 
                    duration
                )
                return False
                
        except ImportError as e:
            duration = time.time() - start_time
            self.log_test(
                "MCP Server", 
                False, 
                f"Erro de importação: {e}", 
                duration
            )
            return False
        except Exception as e:
            duration = time.time() - start_time
            self.log_test(
                "MCP Server", 
                False, 
                f"Erro: {e}", 
                duration
            )
            return False
    
    def run_all_tests(self) -> Dict[str, Any]:
        """
        Executa todos os testes.
        
        Returns:
            Dict: Relatório completo dos testes
        """
        print("🧪 Iniciando Testes do Sistema RAG Recoloca.ai")
        print("=" * 60)
        
        # Executar testes em ordem
        tests = [
            ("Ambiente", self.test_environment),
            ("Modelo de Embedding", self.test_embedding_model),
            ("Indexação", self.test_indexing),
            ("Retrieval", self.test_retrieval),
            ("MCP Server", self.test_mcp_server_import)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            try:
                success = test_func()
                if success:
                    passed += 1
            except Exception as e:
                self.log_test(test_name, False, f"Erro inesperado: {e}")
        
        # Relatório final
        total_duration = time.time() - self.start_time
        
        print("\n" + "=" * 60)
        print(f"[EMOJI] RELATÓRIO FINAL: {passed}/{total} testes passaram")
        print(f"⏱[EMOJI] Tempo total: {total_duration:.2f}s")
        
        if passed == total:
            print("[EMOJI] Todos os testes passaram! Sistema RAG está funcionando.")
        else:
            print(f"[WARNING] {total - passed} teste(s) falharam. Verifique os logs acima.")
        
        # Retornar relatório
        return {
            "total_tests": total,
            "passed_tests": passed,
            "failed_tests": total - passed,
            "success_rate": (passed / total) * 100,
            "total_duration": total_duration,
            "all_passed": passed == total,
            "detailed_results": self.test_results
        }

def main():
    """
    Função principal do script de teste.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Teste do Sistema RAG Recoloca.ai")
    parser.add_argument(
        "--force-cpu", 
        action="store_true", 
        help="Força o uso de CPU em vez de GPU"
    )
    parser.add_argument(
        "--save-report", 
        type=str, 
        help="Salva o relatório em arquivo JSON"
    )
    
    args = parser.parse_args()
    
    # Executar testes
    tester = RAGSystemTester(force_cpu=args.force_cpu)
    report = tester.run_all_tests()
    
    # Salvar relatório se solicitado
    if args.save_report:
        try:
            with open(args.save_report, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            print(f"\n[SAVE] Relatório salvo em: {args.save_report}")
        except Exception as e:
            print(f"\n[ERROR] Erro ao salvar relatório: {e}")
    
    # Código de saída
    sys.exit(0 if report["all_passed"] else 1)

if __name__ == "__main__":
    main()