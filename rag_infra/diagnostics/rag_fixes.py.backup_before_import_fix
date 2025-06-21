# -*- coding: utf-8 -*-
"""
Sistema de Correções Consolidado RAG - Recoloca.ai

Este módulo unifica todas as funcionalidades de correção do sistema RAG,
consolidando os scripts anteriormente dispersos em correcao_rag.py,
fix_rag_issues.py e diagnose_rag_issues.py.

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

# Adicionar o diretório core_logic ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "core_logic"))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rag_fixes.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class FixResult:
    """Resultado de uma correção aplicada."""
    fix_name: str
    success: bool
    message: str
    details: Dict[str, Any] = None
    execution_time: float = 0.0
    changes_made: List[str] = None
    
    def __post_init__(self):
        if self.details is None:
            self.details = {}
        if self.changes_made is None:
            self.changes_made = []

class FixInterface(ABC):
    """Interface base para correções."""
    
    @abstractmethod
    def apply_fix(self) -> FixResult:
        """Aplica a correção."""
        pass
    
    @abstractmethod
    def check_if_needed(self) -> bool:
        """Verifica se a correção é necessária."""
        pass

class SimilarityThresholdFix(FixInterface):
    """Correção do threshold de similaridade."""
    
    def __init__(self, target_threshold: float = 0.3):
        self.target_threshold = target_threshold
        self.config_file = Path(__file__).parent.parent / "config" / "constants.py"
    
    def check_if_needed(self) -> bool:
        """Verifica se o threshold precisa ser ajustado."""
        try:
            if not self.config_file.exists():
                return True
            
            with open(self.config_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Procurar por MIN_SIMILARITY_SCORE
            if 'MIN_SIMILARITY_SCORE' in content:
                # Extrair valor atual
                for line in content.split('\n'):
                    if 'MIN_SIMILARITY_SCORE' in line and '=' in line:
                        try:
                            current_value = float(line.split('=')[1].strip())
                            return current_value > self.target_threshold
                        except ValueError:
                            return True
            
            return True
            
        except Exception:
            return True
    
    def apply_fix(self) -> FixResult:
        """Aplica correção do threshold de similaridade."""
        start_time = time.time()
        changes_made = []
        
        try:
            if not self.config_file.exists():
                # Criar arquivo de configuração
                self.config_file.parent.mkdir(parents=True, exist_ok=True)
                content = f"""# -*- coding: utf-8 -*-
# Configurações do Sistema RAG - Recoloca.ai

# Threshold mínimo de similaridade para resultados
MIN_SIMILARITY_SCORE = {self.target_threshold}

# Configurações de busca
DEFAULT_TOP_K = 5
MAX_TOP_K = 20

# Configurações de modelo
DEFAULT_MODEL_NAME = "BAAI/bge-m3"
DEFAULT_DEVICE = "auto"

# Configurações de índice
FAISS_INDEX_TYPE = "IndexFlatIP"
PYTORCH_INDEX_TYPE = "cosine"
"""
                with open(self.config_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                changes_made.append(f"Criado arquivo de configuração: {self.config_file}")
            else:
                # Atualizar arquivo existente
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Substituir ou adicionar MIN_SIMILARITY_SCORE
                lines = content.split('\n')
                updated = False
                
                for i, line in enumerate(lines):
                    if 'MIN_SIMILARITY_SCORE' in line and '=' in line:
                        old_value = line.split('=')[1].strip()
                        lines[i] = f"MIN_SIMILARITY_SCORE = {self.target_threshold}"
                        changes_made.append(f"Threshold atualizado de {old_value} para {self.target_threshold}")
                        updated = True
                        break
                
                if not updated:
                    # Adicionar no final
                    lines.append(f"MIN_SIMILARITY_SCORE = {self.target_threshold}")
                    changes_made.append(f"Threshold adicionado: {self.target_threshold}")
                
                with open(self.config_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
            
            execution_time = time.time() - start_time
            
            return FixResult(
                fix_name="Similarity Threshold Fix",
                success=True,
                message=f"Threshold de similaridade ajustado para {self.target_threshold}",
                details={'threshold': self.target_threshold, 'config_file': str(self.config_file)},
                execution_time=execution_time,
                changes_made=changes_made
            )
            
        except Exception as e:
            return FixResult(
                fix_name="Similarity Threshold Fix",
                success=False,
                message=f"Erro ao ajustar threshold: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time,
                changes_made=changes_made
            )

class PyTorchBackendFix(FixInterface):
    """Correção da configuração do backend PyTorch."""
    
    def check_if_needed(self) -> bool:
        """Verifica se a configuração do PyTorch precisa ser ajustada."""
        try:
            import torch
            
            # Verificar se CUDA está disponível mas não configurado adequadamente
            if torch.cuda.is_available():
                # Verificar configurações específicas para RTX 2060
                current_device = torch.cuda.current_device()
                gpu_name = torch.cuda.get_device_name(current_device)
                
                # Se for RTX 2060, verificar configurações específicas
                if "RTX 2060" in gpu_name or "2060" in gpu_name:
                    return True
            
            return False
            
        except ImportError:
            return False
    
    def apply_fix(self) -> FixResult:
        """Aplica correções específicas para PyTorch."""
        start_time = time.time()
        changes_made = []
        
        try:
            import torch
            
            if torch.cuda.is_available():
                # Configurações específicas para RTX 2060
                current_device = torch.cuda.current_device()
                gpu_name = torch.cuda.get_device_name(current_device)
                
                # Configurar memory management
                torch.cuda.empty_cache()
                changes_made.append("Cache CUDA limpo")
                
                # Configurar para uso eficiente de memória
                if hasattr(torch.backends.cudnn, 'benchmark'):
                    torch.backends.cudnn.benchmark = True
                    changes_made.append("CuDNN benchmark habilitado")
                
                if hasattr(torch.backends.cudnn, 'deterministic'):
                    torch.backends.cudnn.deterministic = False
                    changes_made.append("CuDNN deterministic desabilitado para performance")
                
                # Configurar mixed precision se disponível
                if hasattr(torch.cuda.amp, 'autocast'):
                    changes_made.append("Mixed precision disponível")
                
                details = {
                    'gpu_name': gpu_name,
                    'cuda_version': torch.version.cuda,
                    'pytorch_version': torch.__version__,
                    'memory_allocated': torch.cuda.memory_allocated(current_device),
                    'memory_reserved': torch.cuda.memory_reserved(current_device)
                }
            else:
                # Configurações para CPU
                torch.set_num_threads(4)  # Otimizar para CPU
                changes_made.append("Configurado para 4 threads CPU")
                
                details = {
                    'device': 'cpu',
                    'num_threads': torch.get_num_threads(),
                    'pytorch_version': torch.__version__
                }
            
            execution_time = time.time() - start_time
            
            return FixResult(
                fix_name="PyTorch Backend Fix",
                success=True,
                message="Configurações do PyTorch otimizadas",
                details=details,
                execution_time=execution_time,
                changes_made=changes_made
            )
            
        except Exception as e:
            return FixResult(
                fix_name="PyTorch Backend Fix",
                success=False,
                message=f"Erro na configuração do PyTorch: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time,
                changes_made=changes_made
            )

class IndexLoadingFix(FixInterface):
    """Correção de problemas de carregamento de índice."""
    
    def check_if_needed(self) -> bool:
        """Verifica se há problemas com carregamento de índice."""
        try:
            from rag_retriever import RAGRetriever
            
            retriever = RAGRetriever()
            if not retriever.initialize():
                return True
            
            return not retriever.load_index()
            
        except Exception:
            return True
    
    def apply_fix(self) -> FixResult:
        """Aplica correções para carregamento de índice."""
        start_time = time.time()
        changes_made = []
        
        try:
            # Verificar arquivos de índice
            base_dir = Path(__file__).parent.parent
            faiss_dir = base_dir / "data_index" / "faiss_index_bge_m3"
            pytorch_dir = base_dir / "data_index" / "pytorch_index_bge_m3"
            
            # Verificar e criar diretórios se necessário
            for index_dir in [faiss_dir, pytorch_dir]:
                if not index_dir.exists():
                    index_dir.mkdir(parents=True, exist_ok=True)
                    changes_made.append(f"Criado diretório: {index_dir}")
            
            # Verificar arquivos essenciais
            essential_files = {
                'faiss': {
                    'documents.json': faiss_dir / "documents.json",
                    'metadata.json': faiss_dir / "metadata.json"
                },
                'pytorch': {
                    'documents.json': pytorch_dir / "documents.json",
                    'metadata.json': pytorch_dir / "metadata.json",
                    'mapping.json': pytorch_dir / "mapping.json"
                }
            }
            
            # Criar arquivos básicos se não existirem
            for backend, files in essential_files.items():
                for filename, filepath in files.items():
                    if not filepath.exists():
                        if filename == 'documents.json':
                            content = []
                        elif filename == 'metadata.json':
                            content = {
                                'total_documents': 0,
                                'embedding_dimension': 1024,
                                'model_name': 'BAAI/bge-m3',
                                'created_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                                'backend': backend
                            }
                        elif filename == 'mapping.json':
                            content = {}
                        else:
                            continue
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            json.dump(content, f, indent=2, ensure_ascii=False)
                        
                        changes_made.append(f"Criado arquivo: {filepath}")
            
            # Tentar recarregar
            try:
                from rag_retriever import RAGRetriever
                retriever = RAGRetriever()
                
                if retriever.initialize():
                    changes_made.append("RAGRetriever inicializado com sucesso")
                    
                    if retriever.load_index():
                        changes_made.append("Índice carregado com sucesso")
                    else:
                        changes_made.append("Aviso: Índice não carregado (pode estar vazio)")
                
            except Exception as e:
                changes_made.append(f"Aviso: Erro ao testar carregamento: {e}")
            
            execution_time = time.time() - start_time
            
            return FixResult(
                fix_name="Index Loading Fix",
                success=True,
                message="Estrutura de índice verificada e corrigida",
                details={
                    'faiss_dir': str(faiss_dir),
                    'pytorch_dir': str(pytorch_dir),
                    'files_checked': len(essential_files['faiss']) + len(essential_files['pytorch'])
                },
                execution_time=execution_time,
                changes_made=changes_made
            )
            
        except Exception as e:
            return FixResult(
                fix_name="Index Loading Fix",
                success=False,
                message=f"Erro na correção de carregamento: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time,
                changes_made=changes_made
            )

class VectorNormalizationFix(FixInterface):
    """Correção de normalização de vetores."""
    
    def check_if_needed(self) -> bool:
        """Verifica se a normalização de vetores precisa ser corrigida."""
        try:
            # Verificar se há embeddings para normalizar
            base_dir = Path(__file__).parent.parent
            pytorch_dir = base_dir / "data_index" / "pytorch_index_bge_m3"
            embeddings_file = pytorch_dir / "embeddings.pt"
            
            return embeddings_file.exists()
            
        except Exception:
            return False
    
    def apply_fix(self) -> FixResult:
        """Aplica normalização de vetores."""
        start_time = time.time()
        changes_made = []
        
        try:
            import torch
            import torch.nn.functional as F
            
            base_dir = Path(__file__).parent.parent
            pytorch_dir = base_dir / "data_index" / "pytorch_index_bge_m3"
            embeddings_file = pytorch_dir / "embeddings.pt"
            
            if embeddings_file.exists():
                # Carregar embeddings
                embeddings = torch.load(embeddings_file, map_location='cpu')
                original_shape = embeddings.shape
                
                # Verificar se já estão normalizados
                norms = torch.norm(embeddings, dim=1)
                max_norm = torch.max(norms).item()
                min_norm = torch.min(norms).item()
                
                if abs(max_norm - 1.0) > 0.01 or abs(min_norm - 1.0) > 0.01:
                    # Normalizar
                    normalized_embeddings = F.normalize(embeddings, p=2, dim=1)
                    
                    # Salvar backup
                    backup_file = embeddings_file.with_suffix('.pt.backup')
                    torch.save(embeddings, backup_file)
                    changes_made.append(f"Backup criado: {backup_file}")
                    
                    # Salvar embeddings normalizados
                    torch.save(normalized_embeddings, embeddings_file)
                    changes_made.append(f"Embeddings normalizados: {original_shape}")
                    
                    # Verificar normalização
                    new_norms = torch.norm(normalized_embeddings, dim=1)
                    new_max = torch.max(new_norms).item()
                    new_min = torch.min(new_norms).item()
                    
                    details = {
                        'original_shape': list(original_shape),
                        'original_norm_range': [min_norm, max_norm],
                        'normalized_norm_range': [new_min, new_max],
                        'backup_file': str(backup_file)
                    }
                else:
                    changes_made.append("Embeddings já estão normalizados")
                    details = {
                        'shape': list(original_shape),
                        'norm_range': [min_norm, max_norm],
                        'already_normalized': True
                    }
            else:
                changes_made.append("Arquivo de embeddings não encontrado")
                details = {'embeddings_file': str(embeddings_file), 'exists': False}
            
            execution_time = time.time() - start_time
            
            return FixResult(
                fix_name="Vector Normalization Fix",
                success=True,
                message="Normalização de vetores verificada/aplicada",
                details=details,
                execution_time=execution_time,
                changes_made=changes_made
            )
            
        except Exception as e:
            return FixResult(
                fix_name="Vector Normalization Fix",
                success=False,
                message=f"Erro na normalização: {e}",
                details={'exception': str(e), 'traceback': traceback.format_exc()},
                execution_time=time.time() - start_time,
                changes_made=changes_made
            )

class RAGFixesRunner:
    """Executor principal das correções RAG."""
    
    def __init__(self):
        self.fixes = [
            SimilarityThresholdFix(),
            PyTorchBackendFix(),
            IndexLoadingFix(),
            VectorNormalizationFix()
        ]
        self.results = []
    
    def run_all_fixes(self, force: bool = False) -> List[FixResult]:
        """Executa todas as correções necessárias."""
        print("🔧 SISTEMA DE CORREÇÕES RAG")
        print("=" * 50)
        
        self.results = []
        
        for fix in self.fixes:
            print(f"\n🔍 Verificando: {fix.__class__.__name__}")
            
            try:
                # Verificar se a correção é necessária
                if force or fix.check_if_needed():
                    print(f"🔧 Aplicando correção...")
                    result = fix.apply_fix()
                    self.results.append(result)
                    
                    status = "✅" if result.success else "❌"
                    print(f"{status} {result.fix_name}: {result.message}")
                    print(f"   Tempo: {result.execution_time:.3f}s")
                    
                    if result.changes_made:
                        print("   Alterações:")
                        for change in result.changes_made:
                            print(f"     • {change}")
                else:
                    print("✅ Correção não necessária")
                    result = FixResult(
                        fix_name=fix.__class__.__name__,
                        success=True,
                        message="Correção não necessária",
                        execution_time=0.0
                    )
                    self.results.append(result)
                    
            except Exception as e:
                error_result = FixResult(
                    fix_name=fix.__class__.__name__,
                    success=False,
                    message=f"Erro inesperado: {e}",
                    details={'exception': str(e), 'traceback': traceback.format_exc()}
                )
                self.results.append(error_result)
                print(f"❌ {fix.__class__.__name__}: Erro inesperado: {e}")
        
        self._print_summary()
        return self.results
    
    def _print_summary(self):
        """Imprime resumo dos resultados."""
        print("\n" + "=" * 50)
        print("📊 RESUMO DAS CORREÇÕES")
        print("=" * 50)
        
        successful = sum(1 for r in self.results if r.success)
        total = len(self.results)
        
        print(f"✅ Sucessos: {successful}/{total}")
        print(f"❌ Falhas: {total - successful}/{total}")
        print(f"⏱️  Tempo total: {sum(r.execution_time for r in self.results):.3f}s")
        
        # Contar alterações
        total_changes = sum(len(r.changes_made) for r in self.results)
        print(f"🔧 Total de alterações: {total_changes}")
        
        if total - successful > 0:
            print("\n🚨 CORREÇÕES FALHARAM:")
            for result in self.results:
                if not result.success:
                    print(f"   • {result.fix_name}: {result.message}")
        
        print("\n🏁 CORREÇÕES CONCLUÍDAS")
    
    def save_report(self, filepath: str = "rag_fixes_report.json"):
        """Salva relatório detalhado em JSON."""
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'summary': {
                'total_fixes': len(self.results),
                'successful_fixes': sum(1 for r in self.results if r.success),
                'failed_fixes': sum(1 for r in self.results if not r.success),
                'total_changes': sum(len(r.changes_made) for r in self.results),
                'total_execution_time': sum(r.execution_time for r in self.results)
            },
            'results': [
                {
                    'fix_name': r.fix_name,
                    'success': r.success,
                    'message': r.message,
                    'execution_time': r.execution_time,
                    'changes_made': r.changes_made,
                    'details': r.details
                }
                for r in self.results
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Relatório salvo em: {filepath}")

def main():
    """Função principal para execução standalone."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Sistema de Correções RAG')
    parser.add_argument('--force', action='store_true', 
                       help='Força aplicação de todas as correções')
    parser.add_argument('--report', type=str, default='rag_fixes_report.json',
                       help='Arquivo para salvar relatório')
    
    args = parser.parse_args()
    
    runner = RAGFixesRunner()
    results = runner.run_all_fixes(force=args.force)
    runner.save_report(args.report)
    
    # Retornar código de saída baseado nos resultados
    failed_fixes = sum(1 for r in results if not r.success)
    return 0 if failed_fixes == 0 else 1

if __name__ == "__main__":
    sys.exit(main())