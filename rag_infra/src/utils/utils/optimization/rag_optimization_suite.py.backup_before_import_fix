# -*- coding: utf-8 -*-
"""
Suíte de Otimização RAG - Recoloca.ai

Este módulo consolida todas as funcionalidades de configuração, otimização,
benchmark e conversão do sistema RAG.

Funcionalidades consolidadas:
- setup_rtx2060_optimizations.py
- start_rtx2060_optimized.py
- benchmark_pytorch_performance.py
- convert_embeddings.py
- convert_faiss_to_pytorch.py

Autor: @AgenteM_DevFastAPI
Versão: 2.0 (Consolidado)
Data: Junho 2025
"""

import argparse
import json
import logging
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union

# Adicionar o diretório core_logic ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "core_logic"))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rag_optimization.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class OptimizationResult:
    """Resultado de uma operação de otimização."""
    operation_name: str
    success: bool
    message: str
    details: Dict[str, Any] = None
    execution_time: float = 0.0
    metrics: Dict[str, float] = None
    
    def __post_init__(self):
        if self.details is None:
            self.details = {}
        if self.metrics is None:
            self.metrics = {}

@dataclass
class BenchmarkResult:
    """Resultado de um benchmark."""
    test_name: str
    duration: float
    queries_per_second: float
    memory_used_mb: float
    gpu_utilization: float
    success_rate: float
    additional_metrics: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.additional_metrics is None:
            self.additional_metrics = {}

class GPUDetector:
    """Detector de informações da GPU."""
    
    @staticmethod
    def detect_gpu_info() -> Dict[str, Any]:
        """Detecta informações da GPU disponível."""
        gpu_info = {
            'cuda_available': False,
            'device_count': 0,
            'devices': [],
            'recommended_config': {}
        }
        
        try:
            import torch
            
            gpu_info['cuda_available'] = torch.cuda.is_available()
            
            if torch.cuda.is_available():
                gpu_info['device_count'] = torch.cuda.device_count()
                
                for i in range(torch.cuda.device_count()):
                    device_name = torch.cuda.get_device_name(i)
                    device_props = torch.cuda.get_device_properties(i)
                    
                    device_info = {
                        'id': i,
                        'name': device_name,
                        'total_memory': device_props.total_memory,
                        'major': device_props.major,
                        'minor': device_props.minor,
                        'multi_processor_count': device_props.multi_processor_count
                    }
                    
                    gpu_info['devices'].append(device_info)
                    
                    # Configurações recomendadas baseadas no hardware
                    if 'RTX 2060' in device_name or 'GTX 1660' in device_name:
                        gpu_info['recommended_config'] = {
                            'batch_size': 6,
                            'max_memory_mb': 4096,
                            'cache_enabled': True,
                            'use_optimizations': True,
                            'pytorch_cuda_alloc_conf': 'max_split_size_mb:512',
                            'omp_num_threads': '2'
                        }
                    elif 'RTX 3060' in device_name or 'RTX 3070' in device_name:
                        gpu_info['recommended_config'] = {
                            'batch_size': 8,
                            'max_memory_mb': 6144,
                            'cache_enabled': True,
                            'use_optimizations': True,
                            'pytorch_cuda_alloc_conf': 'max_split_size_mb:1024',
                            'omp_num_threads': '4'
                        }
                    else:
                        gpu_info['recommended_config'] = {
                            'batch_size': 4,
                            'max_memory_mb': 2048,
                            'cache_enabled': True,
                            'use_optimizations': False,
                            'pytorch_cuda_alloc_conf': 'max_split_size_mb:256',
                            'omp_num_threads': '2'
                        }
                        
        except ImportError:
            logger.warning("PyTorch não disponível para detecção de GPU")
        except Exception as e:
            logger.error(f"Erro na detecção de GPU: {e}")
        
        return gpu_info

class EmbeddingConverter:
    """Conversor de embeddings entre formatos."""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path(__file__).parent.parent
        self.faiss_dir = self.base_dir / "data_index" / "faiss_index_bge_m3"
        self.pytorch_dir = self.base_dir / "data_index" / "pytorch_index_bge_m3"
    
    def convert_numpy_to_pytorch(self) -> OptimizationResult:
        """Converte embeddings de NumPy para PyTorch."""
        start_time = time.time()
        details = {}
        
        try:
            import numpy as np
            import torch
            
            # Verificar arquivo de origem
            embeddings_path = self.faiss_dir / "embeddings.npy"
            if not embeddings_path.exists():
                return OptimizationResult(
                    operation_name="NumPy to PyTorch Conversion",
                    success=False,
                    message=f"Arquivo não encontrado: {embeddings_path}",
                    execution_time=time.time() - start_time
                )
            
            # Criar diretório de destino
            self.pytorch_dir.mkdir(parents=True, exist_ok=True)
            
            # Carregar embeddings NumPy
            logger.info(f"Carregando embeddings de {embeddings_path}")
            embeddings_np = np.load(embeddings_path)
            details['original_shape'] = embeddings_np.shape
            details['original_dtype'] = str(embeddings_np.dtype)
            
            # Converter para PyTorch tensor
            embeddings_torch = torch.from_numpy(embeddings_np).float()
            details['converted_shape'] = list(embeddings_torch.shape)
            details['converted_dtype'] = str(embeddings_torch.dtype)
            
            # Salvar como arquivo PyTorch
            pytorch_embeddings_path = self.pytorch_dir / "embeddings.pt"
            torch.save(embeddings_torch, pytorch_embeddings_path)
            details['output_file'] = str(pytorch_embeddings_path)
            
            # Criar arquivo de mapeamento
            mapping_data = {
                "embedding_dim": embeddings_torch.shape[1],
                "num_embeddings": embeddings_torch.shape[0],
                "dtype": str(embeddings_torch.dtype),
                "device": "cpu",
                "conversion_timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            mapping_path = self.pytorch_dir / "mapping.json"
            with open(mapping_path, 'w', encoding='utf-8') as f:
                json.dump(mapping_data, f, indent=2, ensure_ascii=False)
            details['mapping_file'] = str(mapping_path)
            
            # Copiar outros arquivos necessários
            for filename in ['documents.json', 'metadata.json']:
                src_file = self.faiss_dir / filename
                dst_file = self.pytorch_dir / filename
                
                if src_file.exists():
                    import shutil
                    shutil.copy2(src_file, dst_file)
                    details[f'copied_{filename}'] = True
                else:
                    details[f'copied_{filename}'] = False
            
            execution_time = time.time() - start_time
            
            return OptimizationResult(
                operation_name="NumPy to PyTorch Conversion",
                success=True,
                message=f"Conversão concluída: {embeddings_torch.shape[0]} embeddings",
                details=details,
                execution_time=execution_time,
                metrics={
                    'embeddings_count': embeddings_torch.shape[0],
                    'embedding_dimension': embeddings_torch.shape[1],
                    'file_size_mb': pytorch_embeddings_path.stat().st_size / (1024 * 1024)
                }
            )
            
        except Exception as e:
            return OptimizationResult(
                operation_name="NumPy to PyTorch Conversion",
                success=False,
                message=f"Erro na conversão: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )
    
    def convert_faiss_to_pytorch(self) -> OptimizationResult:
        """Converte índice FAISS completo para PyTorch."""
        start_time = time.time()
        details = {}
        
        try:
            import faiss
            import numpy as np
            import torch
            
            # Verificar arquivo de índice FAISS
            faiss_index_path = self.faiss_dir / "faiss_index.bin"
            if not faiss_index_path.exists():
                return OptimizationResult(
                    operation_name="FAISS to PyTorch Conversion",
                    success=False,
                    message=f"Índice FAISS não encontrado: {faiss_index_path}",
                    execution_time=time.time() - start_time
                )
            
            # Criar diretório de destino
            self.pytorch_dir.mkdir(parents=True, exist_ok=True)
            
            # Carregar índice FAISS
            logger.info(f"Carregando índice FAISS de {faiss_index_path}")
            index = faiss.read_index(str(faiss_index_path))
            details['faiss_index_type'] = type(index).__name__
            details['faiss_ntotal'] = index.ntotal
            details['faiss_d'] = index.d
            
            # Extrair embeddings do índice FAISS
            if hasattr(index, 'reconstruct_n'):
                embeddings_np = np.zeros((index.ntotal, index.d), dtype=np.float32)
                for i in range(index.ntotal):
                    embeddings_np[i] = index.reconstruct(i)
            else:
                # Para índices que não suportam reconstruct, usar embeddings.npy
                embeddings_path = self.faiss_dir / "embeddings.npy"
                if embeddings_path.exists():
                    embeddings_np = np.load(embeddings_path)
                else:
                    return OptimizationResult(
                        operation_name="FAISS to PyTorch Conversion",
                        success=False,
                        message="Não foi possível extrair embeddings do índice FAISS",
                        execution_time=time.time() - start_time
                    )
            
            # Converter para PyTorch
            embeddings_torch = torch.from_numpy(embeddings_np).float()
            details['pytorch_shape'] = list(embeddings_torch.shape)
            
            # Salvar embeddings PyTorch
            pytorch_embeddings_path = self.pytorch_dir / "embeddings.pt"
            torch.save(embeddings_torch, pytorch_embeddings_path)
            details['pytorch_file'] = str(pytorch_embeddings_path)
            
            # Criar mapeamento detalhado
            mapping_data = {
                "source_index_type": type(index).__name__,
                "embedding_dim": embeddings_torch.shape[1],
                "num_embeddings": embeddings_torch.shape[0],
                "dtype": str(embeddings_torch.dtype),
                "device": "cpu",
                "conversion_method": "faiss_to_pytorch",
                "conversion_timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            mapping_path = self.pytorch_dir / "mapping.json"
            with open(mapping_path, 'w', encoding='utf-8') as f:
                json.dump(mapping_data, f, indent=2, ensure_ascii=False)
            details['mapping_file'] = str(mapping_path)
            
            execution_time = time.time() - start_time
            
            return OptimizationResult(
                operation_name="FAISS to PyTorch Conversion",
                success=True,
                message=f"Conversão FAISS->PyTorch concluída: {embeddings_torch.shape[0]} embeddings",
                details=details,
                execution_time=execution_time,
                metrics={
                    'embeddings_count': embeddings_torch.shape[0],
                    'embedding_dimension': embeddings_torch.shape[1],
                    'conversion_time': execution_time
                }
            )
            
        except Exception as e:
            return OptimizationResult(
                operation_name="FAISS to PyTorch Conversion",
                success=False,
                message=f"Erro na conversão FAISS->PyTorch: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )

class RAGBenchmark:
    """Sistema de benchmark para RAG."""
    
    def __init__(self):
        self.test_queries = [
            "Como implementar autenticação JWT no FastAPI?",
            "Configurar banco de dados PostgreSQL com SQLAlchemy",
            "Implementar sistema de cache Redis distribuído",
            "Deploy de aplicação Python com Docker",
            "Monitoramento e logging estruturado",
            "Testes automatizados com pytest",
            "Configuração de CI/CD com GitHub Actions",
            "Otimização de performance em APIs REST",
            "Implementação de WebSockets em tempo real",
            "Segurança e validação de dados com Pydantic"
        ]
    
    def run_performance_benchmark(self, retriever_config: Dict[str, Any] = None) -> BenchmarkResult:
        """Executa benchmark de performance do retriever."""
        start_time = time.time()
        
        try:
            from rag_retriever import get_retriever
            
            # Configurar retriever
            if retriever_config:
                os.environ.update({
                    'RAG_USE_OPTIMIZATIONS': str(retriever_config.get('use_optimizations', True)).lower(),
                    'RAG_CACHE_ENABLED': str(retriever_config.get('cache_enabled', True)).lower(),
                    'RAG_FORCE_PYTORCH': str(retriever_config.get('force_pytorch', True)).lower()
                })
            
            retriever = get_retriever()
            
            # Métricas de benchmark
            successful_queries = 0
            total_queries = len(self.test_queries)
            query_times = []
            memory_usage = []
            
            # Executar queries de teste
            for i, query in enumerate(self.test_queries):
                try:
                    query_start = time.time()
                    
                    # Executar busca
                    results = retriever.search(query, top_k=5)
                    
                    query_time = time.time() - query_start
                    query_times.append(query_time)
                    
                    if results and len(results) > 0:
                        successful_queries += 1
                    
                    # Monitorar uso de memória (se PyTorch disponível)
                    try:
                        import torch
                        if torch.cuda.is_available():
                            memory_usage.append(torch.cuda.memory_allocated() / 1024 / 1024)  # MB
                    except:
                        pass
                    
                    logger.info(f"Query {i+1}/{total_queries}: {query_time:.3f}s")
                    
                except Exception as e:
                    logger.error(f"Erro na query {i+1}: {e}")
                    query_times.append(float('inf'))
            
            # Calcular métricas
            total_time = time.time() - start_time
            valid_times = [t for t in query_times if t != float('inf')]
            
            avg_query_time = sum(valid_times) / len(valid_times) if valid_times else 0
            queries_per_second = len(valid_times) / sum(valid_times) if valid_times else 0
            success_rate = successful_queries / total_queries
            avg_memory = sum(memory_usage) / len(memory_usage) if memory_usage else 0
            
            return BenchmarkResult(
                test_name="Performance Benchmark",
                duration=total_time,
                queries_per_second=queries_per_second,
                memory_used_mb=avg_memory,
                gpu_utilization=0.0,  # Placeholder
                success_rate=success_rate,
                additional_metrics={
                    'total_queries': total_queries,
                    'successful_queries': successful_queries,
                    'avg_query_time': avg_query_time,
                    'min_query_time': min(valid_times) if valid_times else 0,
                    'max_query_time': max(valid_times) if valid_times else 0,
                    'query_times': valid_times
                }
            )
            
        except Exception as e:
            return BenchmarkResult(
                test_name="Performance Benchmark",
                duration=time.time() - start_time,
                queries_per_second=0.0,
                memory_used_mb=0.0,
                gpu_utilization=0.0,
                success_rate=0.0,
                additional_metrics={
                    'error': str(e),
                    'traceback': traceback.format_exc()
                }
            )

class RAGOptimizationSuite:
    """Suíte principal de otimização RAG."""
    
    def __init__(self, project_root: Path = None):
        self.project_root = project_root or Path(__file__).parent.parent.parent
        self.config_dir = self.project_root / "rag_infra" / "config"
        self.config_file = self.config_dir / "rag_optimization_config.json"
        
        self.gpu_detector = GPUDetector()
        self.converter = EmbeddingConverter(self.project_root / "rag_infra")
        self.benchmark = RAGBenchmark()
        
        # Criar diretório de configuração
        self.config_dir.mkdir(parents=True, exist_ok=True)
    
    def setup_optimizations(self, force: bool = False) -> OptimizationResult:
        """Configura otimizações baseadas no hardware detectado."""
        start_time = time.time()
        
        try:
            # Detectar GPU
            gpu_info = self.gpu_detector.detect_gpu_info()
            
            if not gpu_info['cuda_available']:
                return OptimizationResult(
                    operation_name="Setup Optimizations",
                    success=False,
                    message="CUDA não disponível - otimizações limitadas",
                    details=gpu_info,
                    execution_time=time.time() - start_time
                )
            
            # Configuração baseada no hardware
            config = gpu_info['recommended_config'].copy()
            config.update({
                'gpu_info': gpu_info,
                'setup_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'force_setup': force
            })
            
            # Salvar configuração
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False, default=str)
            
            # Configurar variáveis de ambiente
            env_vars = {
                'RAG_USE_OPTIMIZATIONS': 'true',
                'RAG_CACHE_ENABLED': str(config['cache_enabled']).lower(),
                'RAG_FORCE_PYTORCH': 'true',
                'PYTORCH_CUDA_ALLOC_CONF': config['pytorch_cuda_alloc_conf'],
                'OMP_NUM_THREADS': config['omp_num_threads']
            }
            
            for key, value in env_vars.items():
                os.environ[key] = value
            
            execution_time = time.time() - start_time
            
            return OptimizationResult(
                operation_name="Setup Optimizations",
                success=True,
                message=f"Otimizações configuradas para {gpu_info['devices'][0]['name'] if gpu_info['devices'] else 'GPU'}",
                details={
                    'config_file': str(self.config_file),
                    'gpu_info': gpu_info,
                    'env_vars': env_vars,
                    'config': config
                },
                execution_time=execution_time,
                metrics={
                    'batch_size': config['batch_size'],
                    'max_memory_mb': config['max_memory_mb']
                }
            )
            
        except Exception as e:
            return OptimizationResult(
                operation_name="Setup Optimizations",
                success=False,
                message=f"Erro na configuração: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time
            )
    
    def run_full_optimization(self) -> Dict[str, OptimizationResult]:
        """Executa otimização completa do sistema."""
        results = {}
        
        print("🚀 SUÍTE DE OTIMIZAÇÃO RAG - EXECUÇÃO COMPLETA")
        print("=" * 60)
        
        # 1. Setup de otimizações
        print("\n1️⃣ Configurando otimizações...")
        results['setup'] = self.setup_optimizations()
        
        # 2. Conversão de embeddings
        print("\n2️⃣ Convertendo embeddings...")
        results['conversion'] = self.converter.convert_numpy_to_pytorch()
        
        # 3. Benchmark de performance
        print("\n3️⃣ Executando benchmark...")
        if results['setup'].success:
            config = results['setup'].details.get('config', {})
            benchmark_result = self.benchmark.run_performance_benchmark(config)
            results['benchmark'] = OptimizationResult(
                operation_name="Performance Benchmark",
                success=benchmark_result.success_rate > 0.8,
                message=f"Benchmark concluído - {benchmark_result.queries_per_second:.2f} QPS",
                details=asdict(benchmark_result),
                execution_time=benchmark_result.duration,
                metrics={
                    'queries_per_second': benchmark_result.queries_per_second,
                    'success_rate': benchmark_result.success_rate,
                    'avg_memory_mb': benchmark_result.memory_used_mb
                }
            )
        
        self._print_optimization_summary(results)
        return results
    
    def _print_optimization_summary(self, results: Dict[str, OptimizationResult]):
        """Imprime resumo da otimização."""
        print("\n" + "=" * 60)
        print("📊 RESUMO DA OTIMIZAÇÃO")
        print("=" * 60)
        
        successful = sum(1 for r in results.values() if r.success)
        total = len(results)
        
        print(f"✅ Operações bem-sucedidas: {successful}/{total}")
        print(f"❌ Operações com falha: {total - successful}/{total}")
        print(f"⏱️  Tempo total: {sum(r.execution_time for r in results.values()):.3f}s")
        
        for name, result in results.items():
            status = "✅" if result.success else "❌"
            print(f"   {status} {result.operation_name}: {result.message}")
        
        if 'benchmark' in results and results['benchmark'].success:
            metrics = results['benchmark'].metrics
            print(f"\n🏆 MÉTRICAS DE PERFORMANCE:")
            print(f"   • Queries por segundo: {metrics.get('queries_per_second', 0):.2f}")
            print(f"   • Taxa de sucesso: {metrics.get('success_rate', 0):.1%}")
            print(f"   • Memória média: {metrics.get('avg_memory_mb', 0):.1f}MB")
        
        print("\n🏁 OTIMIZAÇÃO CONCLUÍDA")
    
    def save_optimization_report(self, results: Dict[str, OptimizationResult], filepath: str = "rag_optimization_report.json"):
        """Salva relatório detalhado da otimização."""
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'summary': {
                'total_operations': len(results),
                'successful_operations': sum(1 for r in results.values() if r.success),
                'failed_operations': sum(1 for r in results.values() if not r.success),
                'total_execution_time': sum(r.execution_time for r in results.values())
            },
            'results': {
                name: {
                    'operation_name': result.operation_name,
                    'success': result.success,
                    'message': result.message,
                    'execution_time': result.execution_time,
                    'details': result.details,
                    'metrics': result.metrics
                }
                for name, result in results.items()
            }
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n📄 Relatório salvo em: {filepath}")

def main():
    """Função principal para execução standalone."""
    parser = argparse.ArgumentParser(description='Suíte de Otimização RAG')
    parser.add_argument('--operation', type=str, 
                       choices=['setup', 'convert', 'benchmark', 'full'],
                       default='full', help='Operação específica para executar')
    parser.add_argument('--force', action='store_true',
                       help='Forçar reconfiguração')
    parser.add_argument('--report', type=str, default='rag_optimization_report.json',
                       help='Arquivo para salvar relatório')
    
    args = parser.parse_args()
    
    suite = RAGOptimizationSuite()
    
    if args.operation == 'setup':
        result = suite.setup_optimizations(force=args.force)
        results = {'setup': result}
    elif args.operation == 'convert':
        result = suite.converter.convert_numpy_to_pytorch()
        results = {'conversion': result}
    elif args.operation == 'benchmark':
        benchmark_result = suite.benchmark.run_performance_benchmark()
        result = OptimizationResult(
            operation_name="Performance Benchmark",
            success=benchmark_result.success_rate > 0.8,
            message=f"Benchmark concluído - {benchmark_result.queries_per_second:.2f} QPS",
            details=asdict(benchmark_result),
            execution_time=benchmark_result.duration
        )
        results = {'benchmark': result}
    else:  # full
        results = suite.run_full_optimization()
    
    suite.save_optimization_report(results, args.report)
    
    # Retornar código de saída baseado nos resultados
    failed_operations = sum(1 for r in results.values() if not r.success)
    return 0 if failed_operations == 0 else 1

if __name__ == "__main__":
    sys.exit(main())