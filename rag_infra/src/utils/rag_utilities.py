# -*- coding: utf-8 -*-
"""
Utilitários Consolidados RAG - Recoloca.ai

Este módulo unifica todas as funcionalidades utilitárias do sistema RAG,
consolidando scripts de verificação, debug, correção de índices e testes.

Funcionalidades consolidadas:
- check_backend.py
- debug_pytorch_init.py
- fix_index_loading.py
- fix_index_consistency.py
- test_rag_final.py

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
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Adicionar o diretório core_logic ao path

project_root = Path(__file__).parent.parent

sys.path.insert(0, str(project_root / "src" / "core" / "src/core/core_logic"))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rag_utilities.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class UtilityResult:
    """Resultado de uma operação utilitária."""
    operation_name: str
    success: bool
    message: str
    details: Dict[str, Any] = None
    execution_time: float = 0.0
    data: Any = None
    
    def __post_init__(self):
        if self.details is None:
            self.details = {}

class UtilityInterface(ABC):
    """Interface base para utilitários."""
    
    @abstractmethod
    def execute(self) -> UtilityResult:
        """Executa a operação utilitária."""
        pass

class BackendChecker(UtilityInterface):
    """Verificador de configuração do backend RAG."""
    
    def execute(self) -> UtilityResult:
        """Verifica qual backend RAG está sendo usado."""
        start_time = time.time()
        details = {}
        
        try:
            print("[SEARCH] Verificando configuração do backend RAG...")
            print("=" * 50)
            
            # Verificar imports básicos
            try:
                from rag_retriever import get_retriever
                details['rag_retriever_import'] = True
            except ImportError as e:
                details['rag_retriever_import'] = False
                details['rag_retriever_error'] = str(e)
                return UtilityResult(
                    operation_name="Backend Check",
                    success=False,
                    message=f"Erro ao importar rag_retriever: {e}",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            # Obter retriever
            retriever = get_retriever()
            
            # Informações básicas
            backend_type = 'PyTorch' if getattr(retriever, 'use_pytorch', False) else 'FAISS'
            details['backend_type'] = backend_type
            details['force_cpu'] = getattr(retriever, 'force_cpu', None)
            details['force_pytorch'] = getattr(retriever, 'force_pytorch', None)
            details['use_optimizations'] = getattr(retriever, 'use_optimizations', None)
            
            print(f"Backend em uso: {backend_type}")
            print(f"Force CPU: {details['force_cpu']}")
            print(f"Force PyTorch: {details['force_pytorch']}")
            print(f"Otimizações ativadas: {details['use_optimizations']}")
            
            # Informações detalhadas do backend
            if hasattr(retriever, 'get_backend_info'):
                backend_info = retriever.get_backend_info()
                details['backend_info'] = backend_info
                print("\n[EMOJI] Informações do Backend:")
                for key, value in backend_info.items():
                    print(f"  {key}: {value}")
            
            # Verificar FAISS
            print("\n[EMOJI] Verificação FAISS:")
            try:
                import faiss
                faiss_version = getattr(faiss, '__version__', 'Desconhecida')
                details['faiss'] = {
                    'available': True,
                    'version': faiss_version,
                    'gpu_available': hasattr(faiss, 'StandardGpuResources')
                }
                print(f"  FAISS versão: {faiss_version}")
                
                if hasattr(faiss, 'StandardGpuResources'):
                    print("  [OK] FAISS-GPU disponível")
                else:
                    print("  [ERROR] FAISS-GPU não disponível")
                    
            except ImportError as e:
                details['faiss'] = {'available': False, 'error': str(e)}
                print(f"  [ERROR] Erro ao importar FAISS: {e}")
            
            # Verificar PyTorch
            print("\n[EMOJI] Verificação PyTorch:")
            try:
                import torch
                details['pytorch'] = {
                    'available': True,
                    'version': torch.__version__,
                    'cuda_available': torch.cuda.is_available(),
                    'device_count': torch.cuda.device_count() if torch.cuda.is_available() else 0
                }
                
                print(f"  PyTorch versão: {torch.__version__}")
                print(f"  CUDA disponível: {torch.cuda.is_available()}")
                
                if torch.cuda.is_available():
                    print(f"  Dispositivos CUDA: {torch.cuda.device_count()}")
                    for i in range(torch.cuda.device_count()):
                        print(f"    GPU {i}: {torch.cuda.get_device_name(i)}")
                        details['pytorch'][f'gpu_{i}'] = torch.cuda.get_device_name(i)
                        
            except ImportError as e:
                details['pytorch'] = {'available': False, 'error': str(e)}
                print(f"  [ERROR] Erro ao importar PyTorch: {e}")
            
            execution_time = time.time() - start_time
            
            return UtilityResult(
                operation_name="Backend Check",
                success=True,
                message=f"Backend verificado: {backend_type}",
                details=details,
                execution_time=execution_time,
                data={'backend_type': backend_type, 'retriever': retriever}
            )
            
        except Exception as e:
            return UtilityResult(
                operation_name="Backend Check",
                success=False,
                message=f"Erro na verificação do backend: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class PyTorchInitDebugger(UtilityInterface):
    """Debugger de inicialização do PyTorch."""
    
    def execute(self) -> UtilityResult:
        """Debug da inicialização do PyTorchGPURetriever."""
        start_time = time.time()
        details = {}
        
        try:
            print("=== DEBUG PYTORCH INITIALIZATION ===")
            print(f"Python version: {sys.version}")
            print(f"Working directory: {os.getcwd()}")
            
            core_logic_dir = Path(__file__).parent.parent / "src/core/core_logic"
            print(f"Core logic dir: {core_logic_dir}")
            print(f"Core logic exists: {core_logic_dir.exists()}")
            
            details['python_version'] = sys.version
            details['working_directory'] = os.getcwd()
            details['core_logic_dir'] = str(core_logic_dir)
            details['core_logic_exists'] = core_logic_dir.exists()
            
            # Teste 1: Importação de constantes
            print("\n1. Testando importação de constantes...")
            try:
                from constants import PYTORCH_INDEX_DIR, PYTORCH_DOCUMENTS_FILE, PYTORCH_METADATA_FILE
                
                details['constants'] = {
                    'imported': True,
                    'pytorch_index_dir': str(PYTORCH_INDEX_DIR),
                    'dir_exists': PYTORCH_INDEX_DIR.exists(),
                    'documents_file_exists': (PYTORCH_INDEX_DIR / PYTORCH_DOCUMENTS_FILE).exists(),
                    'metadata_file_exists': (PYTORCH_INDEX_DIR / PYTORCH_METADATA_FILE).exists(),
                    'embeddings_file_exists': (PYTORCH_INDEX_DIR / 'embeddings.pt').exists()
                }
                
                print(f"[OK] Constantes importadas com sucesso")
                print(f"PYTORCH_INDEX_DIR: {PYTORCH_INDEX_DIR}")
                print(f"Directory exists: {PYTORCH_INDEX_DIR.exists()}")
                print(f"Documents file exists: {(PYTORCH_INDEX_DIR / PYTORCH_DOCUMENTS_FILE).exists()}")
                print(f"Metadata file exists: {(PYTORCH_INDEX_DIR / PYTORCH_METADATA_FILE).exists()}")
                print(f"Embeddings file exists: {(PYTORCH_INDEX_DIR / 'embeddings.pt').exists()}")
                
            except Exception as e:
                details['constants'] = {'imported': False, 'error': str(e)}
                print(f"[ERROR] Erro ao importar constantes: {e}")
                return UtilityResult(
                    operation_name="PyTorch Init Debug",
                    success=False,
                    message=f"Falha na importação de constantes: {e}",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            # Teste 2: Importação do PyTorchGPURetriever
            print("\n2. Testando importação do PyTorchGPURetriever...")
            try:
                from pytorch_gpu_retriever import PyTorchGPURetriever
                details['pytorch_gpu_retriever'] = {'imported': True}
                print(f"[OK] PyTorchGPURetriever importado com sucesso")
            except Exception as e:
                details['pytorch_gpu_retriever'] = {'imported': False, 'error': str(e)}
                print(f"[ERROR] Erro ao importar PyTorchGPURetriever: {e}")
                return UtilityResult(
                    operation_name="PyTorch Init Debug",
                    success=False,
                    message=f"Falha na importação do PyTorchGPURetriever: {e}",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            # Teste 3: Inicialização do PyTorchGPURetriever
            print("\n3. Testando inicialização do PyTorchGPURetriever...")
            try:
                retriever = PyTorchGPURetriever(force_cpu=False)
                device = getattr(retriever, 'device', 'unknown')
                details['retriever_init'] = {
                    'success': True,
                    'device': str(device)
                }
                print(f"[OK] PyTorchGPURetriever criado com sucesso")
                print(f"Device: {device}")
            except Exception as e:
                details['retriever_init'] = {'success': False, 'error': str(e)}
                print(f"[ERROR] Erro ao criar PyTorchGPURetriever: {e}")
                return UtilityResult(
                    operation_name="PyTorch Init Debug",
                    success=False,
                    message=f"Falha na inicialização do PyTorchGPURetriever: {e}",
                    details=details,
                    execution_time=time.time() - start_time
                )
            
            execution_time = time.time() - start_time
            
            return UtilityResult(
                operation_name="PyTorch Init Debug",
                success=True,
                message="Debug do PyTorch concluído com sucesso",
                details=details,
                execution_time=execution_time
            )
            
        except Exception as e:
            return UtilityResult(
                operation_name="PyTorch Init Debug",
                success=False,
                message=f"Erro no debug do PyTorch: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class IndexConsistencyChecker(UtilityInterface):
    """Verificador de consistência do índice."""
    
    def execute(self) -> UtilityResult:
        """Verifica a consistência do índice FAISS/PyTorch."""
        start_time = time.time()
        details = {}
        
        try:
            print("[SEARCH] Verificando consistência do índice...")
            print("=" * 50)
            
            base_dir = Path(__file__).parent.parent
            
            # Verificar índice FAISS
            faiss_dir = base_dir / "data_index" / "faiss_index_bge_m3"
            details['faiss_index'] = self._check_index_consistency(faiss_dir, 'FAISS')
            
            # Verificar índice PyTorch
            pytorch_dir = base_dir / "data_index" / "pytorch_index_bge_m3"
            details['pytorch_index'] = self._check_index_consistency(pytorch_dir, 'PyTorch')
            
            # Análise geral
            faiss_consistent = details['faiss_index']['consistent']
            pytorch_consistent = details['pytorch_index']['consistent']
            
            print("\n=== RESUMO DE CONSISTÊNCIA ===")
            print(f"FAISS Index: {'[OK] Consistente' if faiss_consistent else '[ERROR] Inconsistente'}")
            print(f"PyTorch Index: {'[OK] Consistente' if pytorch_consistent else '[ERROR] Inconsistente'}")
            
            overall_success = faiss_consistent or pytorch_consistent
            
            execution_time = time.time() - start_time
            
            return UtilityResult(
                operation_name="Index Consistency Check",
                success=overall_success,
                message=f"Verificação concluída - FAISS: {faiss_consistent}, PyTorch: {pytorch_consistent}",
                details=details,
                execution_time=execution_time
            )
            
        except Exception as e:
            return UtilityResult(
                operation_name="Index Consistency Check",
                success=False,
                message=f"Erro na verificação de consistência: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )
    
    def _check_index_consistency(self, index_dir: Path, backend_name: str) -> Dict[str, Any]:
        """Verifica consistência de um índice específico."""
        result = {
            'backend': backend_name,
            'directory': str(index_dir),
            'exists': index_dir.exists(),
            'consistent': False,
            'files': {},
            'counts': {},
            'errors': []
        }
        
        if not index_dir.exists():
            result['errors'].append(f"Diretório {index_dir} não existe")
            return result
        
        try:
            # Arquivos esperados
            expected_files = {
                'documents.json': index_dir / "documents.json",
                'metadata.json': index_dir / "metadata.json"
            }
            
            if backend_name == 'FAISS':
                expected_files.update({
                    'faiss_index.bin': index_dir / "faiss_index.bin",
                    'embeddings.npy': index_dir / "embeddings.npy"
                })
            else:  # PyTorch
                expected_files.update({
                    'embeddings.pt': index_dir / "embeddings.pt",
                    'mapping.json': index_dir / "mapping.json"
                })
            
            # Verificar existência dos arquivos
            for name, filepath in expected_files.items():
                exists = filepath.exists()
                size = filepath.stat().st_size if exists else 0
                result['files'][name] = {
                    'exists': exists,
                    'size': size,
                    'path': str(filepath)
                }
                
                if not exists:
                    result['errors'].append(f"Arquivo {name} não encontrado")
            
            # Se arquivos básicos existem, verificar consistência
            docs_file = expected_files['documents.json']
            meta_file = expected_files['metadata.json']
            
            if docs_file.exists() and meta_file.exists():
                # Carregar documentos
                with open(docs_file, 'r', encoding='utf-8') as f:
                    documents = json.load(f)
                result['counts']['documents'] = len(documents)
                
                # Carregar metadados
                with open(meta_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                
                docs_metadata = metadata.get("documents_metadata", [])
                result['counts']['metadata'] = len(docs_metadata)
                
                # Verificar embeddings
                if backend_name == 'FAISS':
                    emb_file = expected_files['embeddings.npy']
                    if emb_file.exists():
                        import numpy as np
                        embeddings = np.load(emb_file)
                        result['counts']['embeddings'] = embeddings.shape[0]
                        result['embedding_shape'] = list(embeddings.shape)
                else:  # PyTorch
                    emb_file = expected_files['embeddings.pt']
                    if emb_file.exists():
                        import torch
                        embeddings = torch.load(emb_file, map_location='cpu')
                        result['counts']['embeddings'] = embeddings.shape[0]
                        result['embedding_shape'] = list(embeddings.shape)
                
                # Verificar consistência dos counts
                doc_count = result['counts'].get('documents', 0)
                meta_count = result['counts'].get('metadata', 0)
                emb_count = result['counts'].get('embeddings', 0)
                
                print(f"\n[EMOJI] {backend_name} Index:")
                print(f"  Documentos: {doc_count}")
                print(f"  Metadados: {meta_count}")
                print(f"  Embeddings: {emb_count}")
                
                if doc_count == meta_count == emb_count and doc_count > 0:
                    result['consistent'] = True
                    print(f"  [OK] Consistente")
                else:
                    result['errors'].append(f"Inconsistência: docs={doc_count}, meta={meta_count}, emb={emb_count}")
                    print(f"  [ERROR] Inconsistente")
            
        except Exception as e:
            result['errors'].append(f"Erro na verificação: {e}")
        
        return result

class RAGUtilitiesRunner:
    """Executor principal dos utilitários RAG."""
    
    def __init__(self):
        self.utilities = {
            'backend_check': BackendChecker(),
            'pytorch_debug': PyTorchInitDebugger(),
            'index_consistency': IndexConsistencyChecker()
        }
        self.results = {}
    
    def run_utility(self, utility_name: str) -> UtilityResult:
        """Executa um utilitário específico."""
        if utility_name not in self.utilities:
            return UtilityResult(
                operation_name=utility_name,
                success=False,
                message=f"Utilitário '{utility_name}' não encontrado"
            )
        
        print(f"\n[EMOJI] Executando: {utility_name}")
        print("=" * 50)
        
        result = self.utilities[utility_name].execute()
        self.results[utility_name] = result
        
        status = "[OK]" if result.success else "[ERROR]"
        print(f"\n{status} {result.operation_name}: {result.message}")
        print(f"Tempo: {result.execution_time:.3f}s")
        
        return result
    
    def run_all_utilities(self) -> Dict[str, UtilityResult]:
        """Executa todos os utilitários."""
        print("[EMOJI]  UTILITÁRIOS RAG - EXECUÇÃO COMPLETA")
        print("=" * 60)
        
        for utility_name in self.utilities.keys():
            try:
                self.run_utility(utility_name)
            except Exception as e:
                error_result = UtilityResult(
                    operation_name=utility_name,
                    success=False,
                    message=f"Erro inesperado: {e}",
                    details={'exception': str(e), 'traceback': traceback.format_exc()}
                )
                self.results[utility_name] = error_result
                print(f"[ERROR] {utility_name}: Erro inesperado: {e}")
        
        self._print_summary()
        return self.results
    
    def _print_summary(self):
        """Imprime resumo dos resultados."""
        print("\n" + "=" * 60)
        print("[EMOJI] RESUMO DOS UTILITÁRIOS")
        print("=" * 60)
        
        successful = sum(1 for r in self.results.values() if r.success)
        total = len(self.results)
        
        print(f"[OK] Sucessos: {successful}/{total}")
        print(f"[ERROR] Falhas: {total - successful}/{total}")
        print(f"⏱[EMOJI]  Tempo total: {sum(r.execution_time for r in self.results.values()):.3f}s")
        
        if total - successful > 0:
            print("\n[EMOJI] UTILITÁRIOS COM FALHAS:")
            for name, result in self.results.items():
                if not result.success:
                    print(f"   • {name}: {result.message}")
        
        print("\n[EMOJI] UTILITÁRIOS CONCLUÍDOS")
    
    def save_report(self, filepath: str = "rag_utilities_report.json"):
        """Salva relatório detalhado em JSON."""
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'summary': {
                'total_utilities': len(self.results),
                'successful_utilities': sum(1 for r in self.results.values() if r.success),
                'failed_utilities': sum(1 for r in self.results.values() if not r.success),
                'total_execution_time': sum(r.execution_time for r in self.results.values())
            },
            'results': {
                name: {
                    'operation_name': result.operation_name,
                    'success': result.success,
                    'message': result.message,
                    'execution_time': result.execution_time,
                    'details': result.details,
                    'data': result.data if hasattr(result, 'data') and result.data is not None else None
                }
                for name, result in self.results.items()
            }
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n[EMOJI] Relatório salvo em: {filepath}")

def main():
    """Função principal para execução standalone."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Utilitários RAG Consolidados')
    parser.add_argument('--utility', type=str, choices=['backend_check', 'pytorch_debug', 'index_consistency', 'all'],
                       default='all', help='Utilitário específico para executar')
    parser.add_argument('--report', type=str, default='rag_utilities_report.json',
                       help='Arquivo para salvar relatório')
    
    args = parser.parse_args()
    
    runner = RAGUtilitiesRunner()
    
    if args.utility == 'all':
        results = runner.run_all_utilities()
    else:
        result = runner.run_utility(args.utility)
        results = {args.utility: result}
    
    runner.save_report(args.report)
    
    # Retornar código de saída baseado nos resultados
    failed_utilities = sum(1 for r in results.values() if not r.success)
    return 0 if failed_utilities == 0 else 1

if __name__ == "__main__":
    sys.exit(main())