# -*- coding: utf-8 -*-
"""
Sistema de Diagnóstico Consolidado RAG - Recoloca.ai

Este módulo unifica todas as funcionalidades de diagnóstico do sistema RAG,
consolidando os scripts anteriormente dispersos em diagnostico_rag.py,
diagnostico_simples.py e diagnose_rag_issues.py.

Autor: @AgenteM_DevFastAPI
Versão: 2.0 (Consolidado)
Data: Junho 2025
"""

import sys
import os
import json
import logging
import time
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Adicionar o diretório src ao path para permitir imports de pacotes
project_root = Path(__file__).resolve().parent.parent # rag_infra
src_path = project_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rag_diagnostics.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class DiagnosticResult:
    """Resultado de um teste de diagnóstico."""
    test_name: str
    success: bool
    message: str
    details: Dict[str, Any] = None
    execution_time: float = 0.0
    
    def __post_init__(self):
        if self.details is None:
            self.details = {}

class DiagnosticInterface(ABC):
    """Interface base para testes de diagnóstico."""
    
    @abstractmethod
    def run_test(self) -> DiagnosticResult:
        """Executa o teste de diagnóstico."""
        pass

class ImportDiagnostic(DiagnosticInterface):
    """Diagnóstico de imports e dependências."""
    
    def run_test(self) -> DiagnosticResult:
        """Testa se todos os imports necessários estão funcionando."""
        start_time = time.time()
        details = {}
        issues = []
        
        try:
            # Teste PyTorch
            try:
                import torch
                details['pytorch'] = {
                    'version': torch.__version__,
                    'cuda_available': torch.cuda.is_available(),
                    'gpu_name': torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
                    'gpu_count': torch.cuda.device_count() if torch.cuda.is_available() else 0
                }
            except ImportError as e:
                issues.append(f"PyTorch: {e}")
                details['pytorch'] = {'error': str(e)}
            
            # Teste FAISS
            try:
                import faiss
                details['faiss'] = {
                    'version': getattr(faiss, '__version__', 'unknown'),
                    'gpu_available': hasattr(faiss, 'StandardGpuResources')
                }
            except ImportError as e:
                issues.append(f"FAISS: {e}")
                details['faiss'] = {'error': str(e)}
            
            # Teste Transformers
            try:
                import transformers
                details['transformers'] = {
                    'version': transformers.__version__
                }
            except ImportError as e:
                issues.append(f"Transformers: {e}")
                details['transformers'] = {'error': str(e)}
            
            # Teste NumPy
            try:
                import numpy as np
                details['numpy'] = {
                    'version': np.__version__
                }
            except ImportError as e:
                issues.append(f"NumPy: {e}")
                details['numpy'] = {'error': str(e)}
            
            execution_time = time.time() - start_time
            
            if issues:
                return DiagnosticResult(
                    test_name="Import Test",
                    success=False,
                    message=f"Falhas encontradas: {'; '.join(issues)}",
                    details=details,
                    execution_time=execution_time
                )
            else:
                return DiagnosticResult(
                    test_name="Import Test",
                    success=True,
                    message="Todos os imports necessários estão funcionando",
                    details=details,
                    execution_time=execution_time
                )
                
        except Exception as e:
            return DiagnosticResult(
                test_name="Import Test",
                success=False,
                message=f"Erro inesperado: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class GPUCompatibilityDiagnostic(DiagnosticInterface):
    """Diagnóstico de compatibilidade GPU."""
    
    def run_test(self) -> DiagnosticResult:
        """Testa compatibilidade e configuração da GPU."""
        start_time = time.time()
        details = {}
        
        try:
            import torch
            
            # Informações básicas da GPU
            cuda_available = torch.cuda.is_available()
            details['cuda_available'] = cuda_available
            
            if cuda_available:
                details['gpu_count'] = torch.cuda.device_count()
                details['current_device'] = torch.cuda.current_device()
                details['gpu_name'] = torch.cuda.get_device_name(0)
                details['gpu_memory'] = {
                    'total': torch.cuda.get_device_properties(0).total_memory,
                    'allocated': torch.cuda.memory_allocated(0),
                    'cached': torch.cuda.memory_reserved(0)
                }
                
                # Teste de operação simples na GPU
                try:
                    test_tensor = torch.randn(100, 100).cuda()
                    result = torch.matmul(test_tensor, test_tensor.t())
                    details['gpu_operation_test'] = 'success'
                except Exception as e:
                    details['gpu_operation_test'] = f'failed: {e}'
            
            execution_time = time.time() - start_time
            
            if cuda_available:
                return DiagnosticResult(
                    test_name="GPU Compatibility Test",
                    success=True,
                    message=f"GPU {details['gpu_name']} disponível e funcional",
                    details=details,
                    execution_time=execution_time
                )
            else:
                return DiagnosticResult(
                    test_name="GPU Compatibility Test",
                    success=False,
                    message="CUDA não disponível - executando em CPU",
                    details=details,
                    execution_time=execution_time
                )
                
        except Exception as e:
            return DiagnosticResult(
                test_name="GPU Compatibility Test",
                success=False,
                message=f"Erro no teste de GPU: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class IndexFilesDiagnostic(DiagnosticInterface):
    """Diagnóstico de arquivos de índice."""
    
    def run_test(self) -> DiagnosticResult:
        """Verifica a existência e integridade dos arquivos de índice."""
        start_time = time.time()
        details = {}
        issues = []
        
        try:
            from core.core_logic.constants import FAISS_INDEX_DIR, PYTORCH_INDEX_DIR

            # Verificar diretórios de índice
            faiss_dir = FAISS_INDEX_DIR
            pytorch_dir = PYTORCH_INDEX_DIR
            
            # Verificar FAISS
            faiss_files = {
                'index': faiss_dir / "faiss_index.bin",
                'documents': faiss_dir / "documents.json",
                'metadata': faiss_dir / "metadata.json",
                'embeddings': faiss_dir / "embeddings.npy"
            }
            
            details['faiss_index'] = {}
            for name, file_path in faiss_files.items():
                exists = file_path.exists()
                details['faiss_index'][name] = {
                    'exists': exists,
                    'path': str(file_path),
                    'size': file_path.stat().st_size if exists else 0
                }
                if not exists:
                    issues.append(f"FAISS {name} não encontrado: {file_path}")
            
            # Verificar PyTorch
            pytorch_files = {
                'embeddings': pytorch_dir / "embeddings.pt",
                'documents': pytorch_dir / "documents.json",
                'metadata': pytorch_dir / "metadata.json",
                'mapping': pytorch_dir / "mapping.json"
            }
            
            details['pytorch_index'] = {}
            for name, file_path in pytorch_files.items():
                exists = file_path.exists()
                details['pytorch_index'][name] = {
                    'exists': exists,
                    'path': str(file_path),
                    'size': file_path.stat().st_size if exists else 0
                }
                if not exists:
                    issues.append(f"PyTorch {name} não encontrado: {file_path}")
            
            execution_time = time.time() - start_time
            
            if issues:
                return DiagnosticResult(
                    test_name="Index Files Test",
                    success=False,
                    message=f"Arquivos faltando: {'; '.join(issues)}",
                    details=details,
                    execution_time=execution_time
                )
            else:
                return DiagnosticResult(
                    test_name="Index Files Test",
                    success=True,
                    message="Todos os arquivos de índice estão presentes",
                    details=details,
                    execution_time=execution_time
                )
                
        except Exception as e:
            return DiagnosticResult(
                test_name="Index Files Test",
                success=False,
                message=f"Erro na verificação de arquivos: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class SearchFunctionalityDiagnostic(DiagnosticInterface):
    """Diagnóstico de funcionalidade de busca."""
    
    def run_test(self) -> DiagnosticResult:
        """Testa a funcionalidade de busca do RAG."""
        start_time = time.time()
        details = {}
        
        try:
            from core.core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever()
            
            if not retriever.initialize():
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=False,
                    message="Falha na inicialização do retriever",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            if not retriever.load_index():
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=False,
                    message="Falha no carregamento do índice",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            # Testes de busca
            test_queries = [
                "Recoloca.ai MVP",
                "desenvolvimento",
                "API",
                "arquitetura"
            ]
            
            search_results = {}
            for query in test_queries:
                query_start = time.time()
                try:
                    results = retriever.search(query, top_k=3)
                    query_time = time.time() - query_start
                    
                    search_results[query] = {
                        'success': True,
                        'results_count': len(results),
                        'execution_time': query_time,
                        'top_scores': [r.score for r in results[:3]] if results else []
                    }
                except Exception as e:
                    search_results[query] = {
                        'success': False,
                        'error': str(e),
                        'execution_time': time.time() - query_start
                    }
            
            details['search_results'] = search_results
            
            # Verificar se pelo menos uma busca foi bem-sucedida
            successful_searches = sum(1 for r in search_results.values() if r['success'])
            total_searches = len(search_results)
            
            execution_time = time.time() - start_time
            
            if successful_searches > 0:
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=True,
                    message=f"Busca funcional: {successful_searches}/{total_searches} consultas bem-sucedidas",
                    details=details,
                    execution_time=execution_time
                )
            else:
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=False,
                    message="Nenhuma busca foi bem-sucedida",
                    details=details,
                    execution_time=execution_time
                )
                
        except Exception as e:
            return DiagnosticResult(
                test_name="Search Functionality Test",
                success=False,
                message=f"Erro no teste de busca: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class RAGInitializationDiagnostic(DiagnosticInterface):
    """Diagnóstico de inicialização do RAG."""
    
    def run_test(self) -> DiagnosticResult:
        """Testa a inicialização do sistema RAG."""
        start_time = time.time()
        details = {}
        
        try:
            from core.core_logic.rag_retriever import RAGRetriever, _detect_gpu_compatibility
            
            retriever = RAGRetriever()
            details['retriever_created'] = True
            
            # Teste de inicialização
            init_success = retriever.initialize()
            details['initialization'] = init_success
            
            if init_success:
                # Teste de carregamento do índice
                load_success = retriever.load_index()
                details['index_loading'] = load_success
                
                if load_success:
                    details['backend'] = getattr(retriever, 'backend', 'unknown')
                    details['model_name'] = getattr(retriever, 'model_name', 'unknown')
                    
                    execution_time = time.time() - start_time
                    return DiagnosticResult(
                        test_name="RAG Initialization Test",
                        success=True,
                        message="RAG inicializado com sucesso",
                        details=details,
                        execution_time=execution_time
                    )
                else:
                    execution_time = time.time() - start_time
                    return DiagnosticResult(
                        test_name="RAG Initialization Test",
                        success=False,
                        message="Falha no carregamento do índice",
                        details=details,
                        execution_time=execution_time
                    )
            else:
                execution_time = time.time() - start_time
                return DiagnosticResult(
                    test_name="RAG Initialization Test",
                    success=False,
                    message="Falha na inicialização do RAG",
                    details=details,
                    execution_time=execution_time
                )
                
        except Exception as e:
            return DiagnosticResult(
                test_name="RAG Initialization Test",
                success=False,
                message=f"Erro na inicialização: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class SearchFunctionalityDiagnostic(DiagnosticInterface):
    """Diagnóstico de funcionalidade de busca."""
    
    def run_test(self) -> DiagnosticResult:
        """Testa a funcionalidade de busca do RAG."""
        start_time = time.time()
        details = {}
        
        try:
            from core.core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever()
            
            if not retriever.initialize():
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=False,
                    message="Falha na inicialização do retriever",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            if not retriever.load_index():
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=False,
                    message="Falha no carregamento do índice",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            # Testes de busca
            test_queries = [
                "Recoloca.ai MVP",
                "desenvolvimento",
                "API",
                "arquitetura"
            ]
            
            search_results = {}
            for query in test_queries:
                query_start = time.time()
                try:
                    results = retriever.search(query, top_k=3)
                    query_time = time.time() - query_start
                    
                    search_results[query] = {
                        'success': True,
                        'results_count': len(results),
                        'execution_time': query_time,
                        'top_scores': [r.score for r in results[:3]] if results else []
                    }
                except Exception as e:
                    search_results[query] = {
                        'success': False,
                        'error': str(e),
                        'execution_time': time.time() - query_start
                    }
            
            details['search_results'] = search_results
            
            # Verificar se pelo menos uma busca foi bem-sucedida
            successful_searches = sum(1 for r in search_results.values() if r['success'])
            total_searches = len(search_results)
            
            execution_time = time.time() - start_time
            
            if successful_searches > 0:
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=True,
                    message=f"Busca funcional: {successful_searches}/{total_searches} consultas bem-sucedidas",
                    details=details,
                    execution_time=execution_time
                )
            else:
                return DiagnosticResult(
                    test_name="Search Functionality Test",
                    success=False,
                    message="Nenhuma busca foi bem-sucedida",
                    details=details,
                    execution_time=execution_time
                )
                
        except Exception as e:
            return DiagnosticResult(
                test_name="Search Functionality Test",
                success=False,
                message=f"Erro no teste de busca: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class RAGDiagnosticsRunner:
    """Executor principal dos diagnósticos RAG."""
    
    def __init__(self):
        self.diagnostics = [
            ImportDiagnostic(),
            GPUCompatibilityDiagnostic(),
            IndexFilesDiagnostic(),
            RAGInitializationDiagnostic(),
            SearchFunctionalityDiagnostic()
        ]
        self.results = []
    
    def run_all_diagnostics(self) -> List[DiagnosticResult]:
        """Executa todos os diagnósticos."""
        print("[SEARCH] DIAGNÓSTICO COMPLETO DO SISTEMA RAG")
        print("=" * 50)
        
        self.results = []
        
        for diagnostic in self.diagnostics:
            print(f"\n[EMOJI] Executando: {diagnostic.__class__.__name__}")
            
            try:
                result = diagnostic.run_test()
                self.results.append(result)
                
                status = "[OK]" if result.success else "[ERROR]"
                print(f"{status} {result.test_name}: {result.message}")
                print(f"   Tempo: {result.execution_time:.3f}s")
                
                if result.details and logger.isEnabledFor(logging.DEBUG):
                    print(f"   Detalhes: {json.dumps(result.details, indent=2, ensure_ascii=False)}")
                    
            except Exception as e:
                error_result = DiagnosticResult(
                    test_name=diagnostic.__class__.__name__,
                    success=False,
                    message=f"Erro inesperado: {e}",
                    details={'exception': str(e), 'traceback': traceback.format_exc()}
                )
                self.results.append(error_result)
                print(f"[ERROR] {diagnostic.__class__.__name__}: Erro inesperado: {e}")
        
        self._print_summary()
        return self.results
    
    def _print_summary(self):
        """Imprime resumo dos resultados."""
        print("\n" + "=" * 50)
        print("[EMOJI] RESUMO DOS DIAGNÓSTICOS")
        print("=" * 50)
        
        successful = sum(1 for r in self.results if r.success)
        total = len(self.results)
        
        print(f"[OK] Sucessos: {successful}/{total}")
        print(f"[ERROR] Falhas: {total - successful}/{total}")
        print(f"⏱[EMOJI]  Tempo total: {sum(r.execution_time for r in self.results):.3f}s")
        
        if total - successful > 0:
            print("\n[EMOJI] PROBLEMAS ENCONTRADOS:")
            for result in self.results:
                if not result.success:
                    print(f"   • {result.test_name}: {result.message}")
        
        print("\n[EMOJI] DIAGNÓSTICO CONCLUÍDO")
    
    def save_report(self, filepath: str = "rag_diagnostic_report.json"):
        """Salva relatório detalhado em JSON."""
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'summary': {
                'total_tests': len(self.results),
                'successful_tests': sum(1 for r in self.results if r.success),
                'failed_tests': sum(1 for r in self.results if not r.success),
                'total_execution_time': sum(r.execution_time for r in self.results)
            },
            'results': [
                {
                    'test_name': r.test_name,
                    'success': r.success,
                    'message': r.message,
                    'execution_time': r.execution_time,
                    'details': r.details
                }
                for r in self.results
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n[EMOJI] Relatório salvo em: {filepath}")

def main():
    """Função principal para execução standalone."""
    runner = RAGDiagnosticsRunner()
    results = runner.run_all_diagnostics()
    runner.save_report()
    
    # Retornar código de saída baseado nos resultados
    failed_tests = sum(1 for r in results if not r.success)
    return 0 if failed_tests == 0 else 1

if __name__ == "__main__":
    sys.exit(main())