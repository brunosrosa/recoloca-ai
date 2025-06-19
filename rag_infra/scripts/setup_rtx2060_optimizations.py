#!/usr/bin/env python3
"""
Script de Configuração Rápida - Otimizações RTX 2060

Este script configura automaticamente o sistema RAG com otimizações
específicas para placas RTX 2060, incluindo:
- Detecção automática de hardware
- Configuração de cache otimizada
- Habilitação de métricas
- Validação de configuração

Uso:
    python setup_rtx2060_optimizations.py [--validate] [--force]

Autor: Agente Backend Sênior
Data: 2024
"""

import argparse
import json
import logging
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RTX2060SetupManager:
    """
    Gerenciador de configuração para otimizações RTX 2060.
    """
    
    def __init__(self, force: bool = False):
        self.force = force
        self.project_root = Path(__file__).parent.parent.parent
        self.config_dir = self.project_root / "rag_infra" / "config"
        self.config_file = self.config_dir / "rag_optimization_config.json"
        
        # Criar diretório se não existir
        self.config_dir.mkdir(parents=True, exist_ok=True)
    
    def detect_gpu_info(self) -> Dict[str, Any]:
        """
        Detecta informações da GPU.
        """
        logger.info("🔍 Detectando informações da GPU...")
        
        gpu_info = {
            'cuda_available': False,
            'gpu_name': None,
            'gpu_count': 0,
            'is_rtx2060': False,
            'faiss_gpu_available': False
        }
        
        try:
            import torch
            gpu_info['cuda_available'] = torch.cuda.is_available()
            
            if gpu_info['cuda_available']:
                gpu_info['gpu_count'] = torch.cuda.device_count()
                gpu_info['gpu_name'] = torch.cuda.get_device_name(0)
                
                # Verificar se é RTX 2060
                if 'RTX 2060' in gpu_info['gpu_name']:
                    gpu_info['is_rtx2060'] = True
                    logger.info(f"✅ RTX 2060 detectada: {gpu_info['gpu_name']}")
                else:
                    logger.warning(f"⚠️  GPU detectada não é RTX 2060: {gpu_info['gpu_name']}")
            
            # Testar FAISS-GPU
            try:
                import faiss
                # Tentar criar um índice GPU simples
                test_index = faiss.IndexFlatL2(128)
                gpu_index = faiss.index_cpu_to_gpu(faiss.StandardGpuResources(), 0, test_index)
                gpu_info['faiss_gpu_available'] = True
                logger.info("✅ FAISS-GPU disponível")
            except Exception as e:
                logger.warning(f"⚠️  FAISS-GPU não disponível: {e}")
                gpu_info['faiss_gpu_available'] = False
        
        except ImportError as e:
            logger.error(f"❌ Erro ao importar PyTorch: {e}")
        
        return gpu_info
    
    def create_rtx2060_config(self, gpu_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria configuração otimizada para RTX 2060.
        """
        logger.info("⚙️  Criando configuração RTX 2060...")
        
        config = {
            "metadata": {
                "created_at": time.time(),
                "gpu_info": gpu_info,
                "optimized_for": "RTX 2060",
                "version": "1.0"
            },
            "cache": {
                "enabled": True,
                "ttl_seconds": 1800,  # 30 minutos
                "max_entries": 1000,
                "memory_limit_mb": 512,  # Conservador para RTX 2060
                "cleanup_interval": 300,
                "persistence_enabled": True,
                "persistence_file": "rag_cache_rtx2060.pkl"
            },
            "batch": {
                "enabled": True,
                "size": 8,  # Otimizado para RTX 2060
                "max_workers": 2,
                "timeout_seconds": 30,
                "auto_scaling": True,
                "min_batch_size": 2,
                "max_batch_size": 16
            },
            "monitoring": {
                "enabled": True,
                "metrics_collection": True,
                "alert_thresholds": {
                    "response_time_p95": 2.0,  # 2s para RTX 2060
                    "cache_hit_rate": 0.3,     # 30% mínimo
                    "error_rate": 0.05,        # 5% máximo
                    "memory_usage": 0.8        # 80% máximo
                },
                "export_interval": 60,
                "retention_days": 7
            },
            "gpu": {
                "force_pytorch": not gpu_info['faiss_gpu_available'],
                "use_optimizations": True,
                "memory_fraction": 0.7,  # Usar 70% da VRAM
                "enable_fallback": True,
                "vram_limit_mb": 4096,  # RTX 2060 tem 6GB, usar 4GB
                "batch_processing": True
            },
            "load_testing": {
                "concurrent_users": 5,  # Conservador para RTX 2060
                "queries_per_user": 10,
                "ramp_up_time": 30,
                "test_duration": 300,
                "target_qps": 15,
                "max_response_time": 3.0
            }
        }
        
        # Ajustar configurações baseado na disponibilidade de FAISS-GPU
        if not gpu_info['faiss_gpu_available']:
            logger.info("🔄 FAISS-GPU não disponível, otimizando para PyTorch")
            config["gpu"]["force_pytorch"] = True
            config["batch"]["size"] = 6  # Menor para PyTorch
            config["cache"]["memory_limit_mb"] = 256  # Mais conservador
        
        return config
    
    def save_config(self, config: Dict[str, Any]) -> bool:
        """
        Salva configuração no arquivo.
        """
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            logger.info(f"💾 Configuração salva em: {self.config_file}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar configuração: {e}")
            return False
    
    def load_existing_config(self) -> Optional[Dict[str, Any]]:
        """
        Carrega configuração existente se disponível.
        """
        if not self.config_file.exists():
            return None
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            logger.info(f"📂 Configuração existente carregada: {self.config_file}")
            return config
            
        except Exception as e:
            logger.error(f"❌ Erro ao carregar configuração: {e}")
            return None
    
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Valida a configuração criada.
        """
        logger.info("✅ Validando configuração...")
        
        required_sections = ['cache', 'batch', 'monitoring', 'gpu', 'load_testing']
        
        for section in required_sections:
            if section not in config:
                logger.error(f"❌ Seção obrigatória ausente: {section}")
                return False
        
        # Validações específicas
        cache_config = config['cache']
        if cache_config['memory_limit_mb'] > 1024:
            logger.warning("⚠️  Limite de memória cache pode ser alto para RTX 2060")
        
        batch_config = config['batch']
        if batch_config['size'] > 16:
            logger.warning("⚠️  Tamanho do lote pode ser alto para RTX 2060")
        
        gpu_config = config['gpu']
        if gpu_config['vram_limit_mb'] > 5000:
            logger.warning("⚠️  Limite de VRAM pode ser alto para RTX 2060")
        
        logger.info("✅ Configuração validada com sucesso")
        return True
    
    def setup_environment_variables(self, config: Dict[str, Any]):
        """
        Configura variáveis de ambiente para otimizações.
        """
        logger.info("🌍 Configurando variáveis de ambiente...")
        
        import os
        
        # PyTorch otimizações
        os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:512'
        os.environ['CUDA_LAUNCH_BLOCKING'] = '0'
        
        # FAISS otimizações
        os.environ['OMP_NUM_THREADS'] = str(config['batch']['max_workers'])
        
        # RAG específico
        os.environ['RAG_USE_OPTIMIZATIONS'] = 'true'
        os.environ['RAG_CACHE_ENABLED'] = 'true'
        os.environ['RAG_FORCE_PYTORCH'] = str(config['gpu']['force_pytorch']).lower()
        
        logger.info("✅ Variáveis de ambiente configuradas")
    
    def create_startup_script(self, config: Dict[str, Any]):
        """
        Cria script de inicialização com configurações.
        """
        startup_script = self.project_root / "rag_infra" / "scripts" / "start_rtx2060_optimized.py"
        
        script_content = f'''#!/usr/bin/env python3
"""
Script de Inicialização RAG - RTX 2060 Otimizado
Gerado automaticamente em {time.strftime('%Y-%m-%d %H:%M:%S')}
"""

import os
import sys
from pathlib import Path

# Adicionar diretório do projeto ao path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Configurar variáveis de ambiente
os.environ['RAG_USE_OPTIMIZATIONS'] = 'true'
os.environ['RAG_CACHE_ENABLED'] = 'true'
os.environ['RAG_FORCE_PYTORCH'] = '{str(config['gpu']['force_pytorch']).lower()}'
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:512'
os.environ['OMP_NUM_THREADS'] = '{config['batch']['max_workers']}'

def main():
    """Inicializa RAG com configurações RTX 2060."""
    try:
        from rag_infra.core_logic.rag_retriever import RAGRetriever
        
        print("🚀 Inicializando RAG com otimizações RTX 2060...")
        
        retriever = RAGRetriever(
            use_optimizations=True,
            cache_enabled=True,
            batch_size={config['batch']['size']},
            force_pytorch={config['gpu']['force_pytorch']}
        )
        
        print("✅ RAG inicializado com sucesso!")
        print(f"📊 Configurações aplicadas:")
        print(f"   • Cache: {config['cache']['enabled']}")
        print(f"   • Lote: {config['batch']['size']}")
        print(f"   • PyTorch forçado: {config['gpu']['force_pytorch']}")
        print(f"   • Limite VRAM: {config['gpu']['vram_limit_mb']}MB")
        
        return retriever
        
    except Exception as e:
        print(f"❌ Erro ao inicializar RAG: {{e}}")
        return None

if __name__ == "__main__":
    retriever = main()
    if retriever:
        print("\n🎯 RAG pronto para uso!")
        print("Use retriever.search('sua consulta') para buscar")
    else:
        sys.exit(1)
'''
        
        try:
            with open(startup_script, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            logger.info(f"📝 Script de inicialização criado: {startup_script}")
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar script de inicialização: {e}")
    
    def run_setup(self, validate_only: bool = False) -> bool:
        """
        Executa configuração completa.
        """
        logger.info("🎯 Iniciando configuração RTX 2060...")
        
        try:
            # 1. Verificar configuração existente
            existing_config = self.load_existing_config()
            
            if existing_config and not self.force:
                logger.info("📋 Configuração existente encontrada")
                
                if validate_only:
                    return self.validate_config(existing_config)
                
                response = input("Sobrescrever configuração existente? (s/N): ")
                if response.lower() not in ['s', 'sim', 'y', 'yes']:
                    logger.info("⏭️  Mantendo configuração existente")
                    return True
            
            # 2. Detectar GPU
            gpu_info = self.detect_gpu_info()
            
            if not gpu_info['cuda_available']:
                logger.warning("⚠️  CUDA não disponível, configuração pode não ser otimizada")
            
            # 3. Criar configuração
            config = self.create_rtx2060_config(gpu_info)
            
            # 4. Validar
            if not self.validate_config(config):
                logger.error("❌ Configuração inválida")
                return False
            
            if validate_only:
                logger.info("✅ Configuração válida")
                return True
            
            # 5. Salvar
            if not self.save_config(config):
                return False
            
            # 6. Configurar ambiente
            self.setup_environment_variables(config)
            
            # 7. Criar script de inicialização
            self.create_startup_script(config)
            
            logger.info("🎉 Configuração RTX 2060 concluída com sucesso!")
            logger.info(f"📁 Arquivo de configuração: {self.config_file}")
            logger.info("🚀 Use o script start_rtx2060_optimized.py para inicializar")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro durante configuração: {e}")
            return False


def main():
    """
    Função principal.
    """
    parser = argparse.ArgumentParser(
        description="Configuração de otimizações RAG para RTX 2060"
    )
    parser.add_argument(
        '--validate', 
        action='store_true',
        help="Apenas validar configuração existente"
    )
    parser.add_argument(
        '--force', 
        action='store_true',
        help="Forçar sobrescrita de configuração existente"
    )
    
    args = parser.parse_args()
    
    print("🔧 Configurador de Otimizações RTX 2060")
    print("=" * 40)
    
    setup_manager = RTX2060SetupManager(force=args.force)
    
    try:
        success = setup_manager.run_setup(validate_only=args.validate)
        
        if success:
            if args.validate:
                print("\n✅ Validação concluída com sucesso!")
            else:
                print("\n🎉 Configuração RTX 2060 aplicada com sucesso!")
                print("\n📋 Próximos passos:")
                print("   1. Execute: python rag_infra/scripts/start_rtx2060_optimized.py")
                print("   2. Teste: python rag_infra/examples/rtx2060_optimization_example.py")
                print("   3. Monitore: verifique logs e métricas")
        else:
            print("\n❌ Configuração falhou!")
            return False
        
        return True
        
    except KeyboardInterrupt:
        print("\n⏹️  Configuração cancelada pelo usuário")
        return False
    except Exception as e:
        print(f"\n💥 Erro inesperado: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)