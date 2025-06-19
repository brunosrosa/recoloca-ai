#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correção do Carregamento do Índice RAG

Este script diagnostica e corrige problemas específicos no carregamento
do índice FAISS/PyTorch, focando nos erros identificados nos testes.

Problemas identificados:
- Índice existe mas não carrega
- Backend PyTorch não detecta GPU corretamente
- Falha na inicialização do retriever

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import sys
import os
import json
import logging
import time
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core_logic'))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class IndexLoadingFixer:
    """
    Classe para diagnosticar e corrigir problemas de carregamento do índice.
    """
    
    def __init__(self):
        self.fixes_applied = []
        self.errors_found = []
        self.test_results = {}
        
    def run_comprehensive_fix(self) -> Dict[str, Any]:
        """
        Executa correção abrangente dos problemas de carregamento.
        
        Returns:
            Dict: Relatório das correções aplicadas
        """
        logger.info("🔧 Iniciando correção do carregamento do índice...")
        
        report = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "system_check": self._check_system_requirements(),
            "index_integrity": self._check_index_integrity(),
            "faiss_loading_test": self._test_faiss_loading(),
            "pytorch_loading_test": self._test_pytorch_loading(),
            "embedding_model_test": self._test_embedding_model(),
            "gpu_configuration_fix": self._fix_gpu_configuration(),
            "index_repair": self._repair_index_if_needed(),
            "final_test": self._run_final_loading_test(),
            "fixes_applied": self.fixes_applied,
            "errors_found": self.errors_found,
            "recommendations": []
        }
        
        # Gerar recomendações
        report["recommendations"] = self._generate_recommendations(report)
        
        # Salvar relatório
        self._save_report(report)
        
        # Imprimir resumo
        self._print_summary(report)
        
        return report
    
    def _check_system_requirements(self) -> Dict[str, Any]:
        """
        Verifica requisitos do sistema.
        """
        logger.info("🔍 Verificando requisitos do sistema...")
        
        system_check = {
            "python_version": sys.version,
            "torch_available": False,
            "torch_version": None,
            "cuda_available": False,
            "gpu_name": None,
            "faiss_available": False,
            "faiss_gpu_available": False,
            "sentence_transformers_available": False
        }
        
        try:
            # Verificar PyTorch
            import torch
            system_check["torch_available"] = True
            system_check["torch_version"] = torch.__version__
            system_check["cuda_available"] = torch.cuda.is_available()
            
            if torch.cuda.is_available():
                system_check["gpu_name"] = torch.cuda.get_device_name(0)
                logger.info(f"✅ GPU detectada: {system_check['gpu_name']}")
            else:
                logger.warning("⚠️ CUDA não disponível")
                
        except ImportError as e:
            self.errors_found.append(f"PyTorch não disponível: {e}")
            logger.error(f"❌ PyTorch não disponível: {e}")
        
        try:
            # Verificar FAISS
            import faiss
            system_check["faiss_available"] = True
            
            # Testar FAISS-GPU
            if system_check["cuda_available"]:
                try:
                    # Criar um índice pequeno para testar GPU
                    test_index = faiss.IndexFlatL2(128)
                    gpu_res = faiss.StandardGpuResources()
                    gpu_index = faiss.index_cpu_to_gpu(gpu_res, 0, test_index)
                    system_check["faiss_gpu_available"] = True
                    logger.info("✅ FAISS-GPU funcional")
                except Exception as e:
                    logger.warning(f"⚠️ FAISS-GPU não funcional: {e}")
                    
        except ImportError as e:
            self.errors_found.append(f"FAISS não disponível: {e}")
            logger.error(f"❌ FAISS não disponível: {e}")
        
        try:
            # Verificar SentenceTransformers
            import sentence_transformers
            system_check["sentence_transformers_available"] = True
            logger.info("✅ SentenceTransformers disponível")
        except ImportError as e:
            self.errors_found.append(f"SentenceTransformers não disponível: {e}")
            logger.error(f"❌ SentenceTransformers não disponível: {e}")
        
        return system_check
    
    def _check_index_integrity(self) -> Dict[str, Any]:
        """
        Verifica integridade dos arquivos de índice.
        """
        logger.info("📁 Verificando integridade do índice...")
        
        try:
            from ..core_logic.constants import (
                FAISS_INDEX_DIR, FAISS_INDEX_FILE, 
                FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE
            )
            
            integrity_check = {
                "index_dir_exists": FAISS_INDEX_DIR.exists(),
                "faiss_index_exists": (FAISS_INDEX_DIR / FAISS_INDEX_FILE).exists(),
                "documents_exists": (FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE).exists(),
                "metadata_exists": (FAISS_INDEX_DIR / FAISS_METADATA_FILE).exists(),
                "embeddings_exists": (FAISS_INDEX_DIR / "embeddings.npy").exists(),
                "pytorch_info_exists": (FAISS_INDEX_DIR / "pytorch_conversion_info.json").exists(),
                "file_sizes": {},
                "documents_count": 0,
                "metadata_count": 0,
                "embeddings_shape": None,
                "consistency_check": False
            }
            
            # Verificar tamanhos dos arquivos
            for filename in [FAISS_INDEX_FILE, FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE, "embeddings.npy"]:
                file_path = FAISS_INDEX_DIR / filename
                if file_path.exists():
                    integrity_check["file_sizes"][filename] = file_path.stat().st_size
                    logger.info(f"📄 {filename}: {file_path.stat().st_size} bytes")
                else:
                    logger.warning(f"⚠️ Arquivo ausente: {filename}")
            
            # Verificar conteúdo dos arquivos JSON
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            if documents_path.exists():
                try:
                    with open(documents_path, 'r', encoding='utf-8') as f:
                        documents = json.load(f)
                        integrity_check["documents_count"] = len(documents)
                        logger.info(f"📚 Documentos: {len(documents)}")
                except Exception as e:
                    self.errors_found.append(f"Erro ao ler documents.json: {e}")
                    logger.error(f"❌ Erro ao ler documents.json: {e}")
            
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            if metadata_path.exists():
                try:
                    with open(metadata_path, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                        integrity_check["metadata_count"] = len(metadata)
                        logger.info(f"🏷️ Metadados: {len(metadata)}")
                except Exception as e:
                    self.errors_found.append(f"Erro ao ler metadata.json: {e}")
                    logger.error(f"❌ Erro ao ler metadata.json: {e}")
            
            # Verificar embeddings
            embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
            if embeddings_path.exists():
                try:
                    import numpy as np
                    embeddings = np.load(embeddings_path)
                    integrity_check["embeddings_shape"] = embeddings.shape
                    logger.info(f"🔢 Embeddings shape: {embeddings.shape}")
                except Exception as e:
                    self.errors_found.append(f"Erro ao ler embeddings.npy: {e}")
                    logger.error(f"❌ Erro ao ler embeddings.npy: {e}")
            
            # Verificar consistência
            docs_count = integrity_check["documents_count"]
            meta_count = integrity_check["metadata_count"]
            emb_shape = integrity_check["embeddings_shape"]
            
            if docs_count > 0 and meta_count > 0 and emb_shape is not None:
                emb_count = emb_shape[0] if len(emb_shape) > 0 else 0
                integrity_check["consistency_check"] = (docs_count == meta_count == emb_count)
                
                if integrity_check["consistency_check"]:
                    logger.info(f"✅ Consistência verificada: {docs_count} itens")
                else:
                    logger.warning(f"⚠️ Inconsistência: docs={docs_count}, meta={meta_count}, emb={emb_count}")
                    self.errors_found.append(f"Inconsistência nos dados: docs={docs_count}, meta={meta_count}, emb={emb_count}")
            
            return integrity_check
            
        except Exception as e:
            self.errors_found.append(f"Erro na verificação de integridade: {e}")
            logger.error(f"❌ Erro na verificação de integridade: {e}")
            return {"error": str(e)}
    
    def _test_faiss_loading(self) -> Dict[str, Any]:
        """
        Testa carregamento direto do índice FAISS.
        """
        logger.info("🔍 Testando carregamento FAISS...")
        
        faiss_test = {
            "direct_load_success": False,
            "temp_load_success": False,
            "index_size": 0,
            "index_dimension": 0,
            "error": None
        }
        
        try:
            import faiss
            from ..core_logic.constants import FAISS_INDEX_DIR, FAISS_INDEX_FILE
            
            index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
            
            if not index_path.exists():
                faiss_test["error"] = f"Arquivo de índice não encontrado: {index_path}"
                return faiss_test
            
            # Teste 1: Carregamento direto
            try:
                index = faiss.read_index(str(index_path))
                faiss_test["direct_load_success"] = True
                faiss_test["index_size"] = index.ntotal
                faiss_test["index_dimension"] = index.d
                logger.info(f"✅ Carregamento direto: {index.ntotal} vetores, dim={index.d}")
            except Exception as e:
                logger.warning(f"⚠️ Carregamento direto falhou: {e}")
                faiss_test["error"] = f"Carregamento direto falhou: {e}"
            
            # Teste 2: Carregamento via arquivo temporário (como no código original)
            try:
                with tempfile.NamedTemporaryFile(suffix='.bin', delete=False) as temp_file:
                    temp_file_path = Path(temp_file.name)
                
                shutil.copy2(str(index_path), str(temp_file_path))
                index = faiss.read_index(str(temp_file_path))
                
                faiss_test["temp_load_success"] = True
                faiss_test["index_size"] = index.ntotal
                faiss_test["index_dimension"] = index.d
                
                # Limpar arquivo temporário
                temp_file_path.unlink()
                
                logger.info(f"✅ Carregamento temporário: {index.ntotal} vetores, dim={index.d}")
                
            except Exception as e:
                logger.warning(f"⚠️ Carregamento temporário falhou: {e}")
                if not faiss_test["error"]:
                    faiss_test["error"] = f"Carregamento temporário falhou: {e}"
            
        except Exception as e:
            faiss_test["error"] = f"Erro geral no teste FAISS: {e}"
            logger.error(f"❌ Erro geral no teste FAISS: {e}")
        
        return faiss_test
    
    def _test_pytorch_loading(self) -> Dict[str, Any]:
        """
        Testa carregamento do backend PyTorch.
        """
        logger.info("🔍 Testando carregamento PyTorch...")
        
        pytorch_test = {
            "embeddings_load_success": False,
            "documents_load_success": False,
            "metadata_load_success": False,
            "gpu_transfer_success": False,
            "embeddings_shape": None,
            "device_used": None,
            "error": None
        }
        
        try:
            import torch
            import numpy as np
            from core_logic.constants import (
                FAISS_INDEX_DIR, FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE
            )
            
            # Teste 1: Carregar embeddings
            embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
            if embeddings_path.exists():
                try:
                    embeddings = np.load(embeddings_path)
                    pytorch_test["embeddings_load_success"] = True
                    pytorch_test["embeddings_shape"] = embeddings.shape
                    logger.info(f"✅ Embeddings carregados: {embeddings.shape}")
                    
                    # Teste de transferência para GPU
                    if torch.cuda.is_available():
                        try:
                            embeddings_tensor = torch.from_numpy(embeddings).float()
                            embeddings_gpu = embeddings_tensor.cuda()
                            pytorch_test["gpu_transfer_success"] = True
                            pytorch_test["device_used"] = str(embeddings_gpu.device)
                            logger.info(f"✅ Transferência para GPU: {embeddings_gpu.device}")
                        except Exception as e:
                            logger.warning(f"⚠️ Falha na transferência para GPU: {e}")
                            pytorch_test["device_used"] = "cpu"
                    else:
                        pytorch_test["device_used"] = "cpu"
                        logger.info("ℹ️ Usando CPU (CUDA não disponível)")
                        
                except Exception as e:
                    logger.error(f"❌ Erro ao carregar embeddings: {e}")
                    pytorch_test["error"] = f"Erro ao carregar embeddings: {e}"
            
            # Teste 2: Carregar documentos
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            if documents_path.exists():
                try:
                    with open(documents_path, 'r', encoding='utf-8') as f:
                        documents = json.load(f)
                        pytorch_test["documents_load_success"] = True
                        logger.info(f"✅ Documentos carregados: {len(documents)} itens")
                except Exception as e:
                    logger.error(f"❌ Erro ao carregar documentos: {e}")
                    if not pytorch_test["error"]:
                        pytorch_test["error"] = f"Erro ao carregar documentos: {e}"
            
            # Teste 3: Carregar metadados
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            if metadata_path.exists():
                try:
                    with open(metadata_path, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                        pytorch_test["metadata_load_success"] = True
                        logger.info(f"✅ Metadados carregados: {len(metadata)} itens")
                except Exception as e:
                    logger.error(f"❌ Erro ao carregar metadados: {e}")
                    if not pytorch_test["error"]:
                        pytorch_test["error"] = f"Erro ao carregar metadados: {e}"
            
        except Exception as e:
            pytorch_test["error"] = f"Erro geral no teste PyTorch: {e}"
            logger.error(f"❌ Erro geral no teste PyTorch: {e}")
        
        return pytorch_test
    
    def _test_embedding_model(self) -> Dict[str, Any]:
        """
        Testa carregamento do modelo de embedding.
        """
        logger.info("🤖 Testando modelo de embedding...")
        
        model_test = {
            "model_load_success": False,
            "model_name": None,
            "embedding_dimension": 0,
            "test_embedding_success": False,
            "device_used": None,
            "error": None
        }
        
        try:
            from ..core_logic.constants import EMBEDDING_MODEL_NAME
            from sentence_transformers import SentenceTransformer
            
            model_test["model_name"] = EMBEDDING_MODEL_NAME
            
            # Carregar modelo
            try:
                model = SentenceTransformer(EMBEDDING_MODEL_NAME)
                model_test["model_load_success"] = True
                model_test["embedding_dimension"] = model.get_sentence_embedding_dimension()
                model_test["device_used"] = str(model.device)
                
                logger.info(f"✅ Modelo carregado: {EMBEDDING_MODEL_NAME}")
                logger.info(f"📐 Dimensão: {model_test['embedding_dimension']}")
                logger.info(f"💻 Device: {model_test['device_used']}")
                
                # Teste de embedding
                try:
                    test_text = "teste de embedding"
                    embedding = model.encode(test_text)
                    model_test["test_embedding_success"] = True
                    logger.info(f"✅ Teste de embedding: shape {embedding.shape}")
                except Exception as e:
                    logger.error(f"❌ Falha no teste de embedding: {e}")
                    model_test["error"] = f"Falha no teste de embedding: {e}"
                    
            except Exception as e:
                logger.error(f"❌ Falha ao carregar modelo: {e}")
                model_test["error"] = f"Falha ao carregar modelo: {e}"
                
        except Exception as e:
            model_test["error"] = f"Erro geral no teste do modelo: {e}"
            logger.error(f"❌ Erro geral no teste do modelo: {e}")
        
        return model_test
    
    def _fix_gpu_configuration(self) -> Dict[str, Any]:
        """
        Corrige configurações de GPU.
        """
        logger.info("🔧 Corrigindo configuração de GPU...")
        
        gpu_fix = {
            "cuda_cache_cleared": False,
            "torch_optimizations_applied": False,
            "gpu_memory_optimized": False,
            "fixes_applied": []
        }
        
        try:
            import torch
            
            if torch.cuda.is_available():
                # Limpar cache CUDA
                try:
                    torch.cuda.empty_cache()
                    gpu_fix["cuda_cache_cleared"] = True
                    gpu_fix["fixes_applied"].append("Cache CUDA limpo")
                    logger.info("✅ Cache CUDA limpo")
                except Exception as e:
                    logger.warning(f"⚠️ Falha ao limpar cache CUDA: {e}")
                
                # Aplicar otimizações PyTorch
                try:
                    torch.backends.cudnn.benchmark = True
                    torch.backends.cuda.matmul.allow_tf32 = True
                    torch.backends.cudnn.allow_tf32 = True
                    
                    gpu_fix["torch_optimizations_applied"] = True
                    gpu_fix["fixes_applied"].append("Otimizações PyTorch aplicadas")
                    logger.info("✅ Otimizações PyTorch aplicadas")
                except Exception as e:
                    logger.warning(f"⚠️ Falha ao aplicar otimizações: {e}")
                
                # Otimizar memória GPU
                try:
                    # Configurar alocação de memória mais conservadora
                    torch.cuda.set_per_process_memory_fraction(0.8)
                    gpu_fix["gpu_memory_optimized"] = True
                    gpu_fix["fixes_applied"].append("Memória GPU otimizada (80%)")
                    logger.info("✅ Memória GPU otimizada")
                except Exception as e:
                    logger.warning(f"⚠️ Falha ao otimizar memória GPU: {e}")
            
            self.fixes_applied.extend(gpu_fix["fixes_applied"])
            
        except Exception as e:
            logger.error(f"❌ Erro na correção de GPU: {e}")
            gpu_fix["error"] = str(e)
        
        return gpu_fix
    
    def _repair_index_if_needed(self) -> Dict[str, Any]:
        """
        Repara o índice se necessário.
        """
        logger.info("🔧 Verificando necessidade de reparo do índice...")
        
        repair_result = {
            "repair_needed": False,
            "repair_attempted": False,
            "repair_successful": False,
            "actions_taken": []
        }
        
        try:
            # Verificar se há problemas que requerem reparo
            integrity_issues = []
            
            # Verificar se os testes anteriores falharam
            if hasattr(self, 'test_results'):
                faiss_test = self.test_results.get('faiss_loading_test', {})
                pytorch_test = self.test_results.get('pytorch_loading_test', {})
                
                if not faiss_test.get('direct_load_success', False) and not faiss_test.get('temp_load_success', False):
                    integrity_issues.append("FAISS não carrega")
                
                if not pytorch_test.get('embeddings_load_success', False):
                    integrity_issues.append("Embeddings PyTorch não carregam")
            
            if integrity_issues:
                repair_result["repair_needed"] = True
                repair_result["repair_attempted"] = True
                
                logger.info(f"🔧 Problemas detectados: {', '.join(integrity_issues)}")
                
                # Tentar converter FAISS para PyTorch se FAISS falhar
                if "FAISS não carrega" in integrity_issues:
                    try:
                        from .convert_faiss_to_pytorch import convert_faiss_to_pytorch
                        
                        logger.info("🔄 Tentando conversão FAISS -> PyTorch...")
                        success = convert_faiss_to_pytorch()
                        
                        if success:
                            repair_result["actions_taken"].append("Conversão FAISS -> PyTorch")
                            logger.info("✅ Conversão FAISS -> PyTorch bem-sucedida")
                        else:
                            logger.warning("⚠️ Conversão FAISS -> PyTorch falhou")
                            
                    except Exception as e:
                        logger.error(f"❌ Erro na conversão: {e}")
                        repair_result["actions_taken"].append(f"Falha na conversão: {e}")
                
                # Verificar se o reparo foi bem-sucedido
                if repair_result["actions_taken"]:
                    repair_result["repair_successful"] = True
                    self.fixes_applied.extend(repair_result["actions_taken"])
            
        except Exception as e:
            logger.error(f"❌ Erro no reparo do índice: {e}")
            repair_result["error"] = str(e)
        
        return repair_result
    
    def _run_final_loading_test(self) -> Dict[str, Any]:
        """
        Executa teste final de carregamento.
        """
        logger.info("🧪 Executando teste final de carregamento...")
        
        final_test = {
            "rag_retriever_init": False,
            "index_loading": False,
            "search_test": False,
            "backend_type": None,
            "search_results_count": 0,
            "error": None
        }
        
        try:
            from ..core_logic.rag_retriever import RAGRetriever
            
            # Teste com diferentes configurações
            configs = [
                {"force_pytorch": True, "use_optimizations": True},
                {"force_pytorch": False, "use_optimizations": True},
                {"force_pytorch": True, "use_optimizations": False}
            ]
            
            for i, config in enumerate(configs):
                try:
                    logger.info(f"🔍 Testando configuração {i+1}: {config}")
                    
                    # Inicializar retriever
                    retriever = RAGRetriever(**config)
                    
                    if retriever.initialize():
                        final_test["rag_retriever_init"] = True
                        logger.info("✅ RAGRetriever inicializado")
                        
                        # Tentar carregar índice
                        if retriever.load_index():
                            final_test["index_loading"] = True
                            final_test["backend_type"] = type(retriever.backend).__name__ if hasattr(retriever, 'backend') else "Unknown"
                            logger.info(f"✅ Índice carregado com backend: {final_test['backend_type']}")
                            
                            # Teste de busca
                            try:
                                results = retriever.search("teste arquitetura", top_k=3, min_score=0.1)
                                final_test["search_test"] = True
                                final_test["search_results_count"] = len(results)
                                logger.info(f"✅ Busca bem-sucedida: {len(results)} resultados")
                                
                                # Se chegou até aqui, o teste foi bem-sucedido
                                break
                                
                            except Exception as e:
                                logger.warning(f"⚠️ Falha na busca: {e}")
                                final_test["error"] = f"Falha na busca: {e}"
                        else:
                            logger.warning(f"⚠️ Falha no carregamento do índice com config {i+1}")
                    else:
                        logger.warning(f"⚠️ Falha na inicialização com config {i+1}")
                        
                except Exception as e:
                    logger.warning(f"⚠️ Erro com configuração {i+1}: {e}")
                    continue
            
            if not final_test["rag_retriever_init"]:
                final_test["error"] = "Falha na inicialização com todas as configurações"
            elif not final_test["index_loading"]:
                final_test["error"] = "Falha no carregamento do índice com todas as configurações"
            elif not final_test["search_test"]:
                final_test["error"] = "Falha na busca com todas as configurações"
            
        except Exception as e:
            final_test["error"] = f"Erro geral no teste final: {e}"
            logger.error(f"❌ Erro geral no teste final: {e}")
        
        return final_test
    
    def _generate_recommendations(self, report: Dict[str, Any]) -> List[str]:
        """
        Gera recomendações baseadas nos resultados.
        """
        recommendations = []
        
        final_test = report.get("final_test", {})
        
        if final_test.get("search_test", False):
            recommendations.append("✅ Sistema RAG funcionando corretamente após correções")
            recommendations.append("🔧 Monitore performance em uso contínuo")
        else:
            recommendations.append("🚨 CRÍTICO: Sistema ainda não funcional")
            
            # Recomendações específicas baseadas nos testes
            system_check = report.get("system_check", {})
            
            if not system_check.get("torch_available", False):
                recommendations.append("📦 Instalar PyTorch: pip install torch")
            
            if not system_check.get("faiss_available", False):
                recommendations.append("📦 Instalar FAISS: pip install faiss-cpu faiss-gpu")
            
            if not system_check.get("sentence_transformers_available", False):
                recommendations.append("📦 Instalar SentenceTransformers: pip install sentence-transformers")
            
            integrity_check = report.get("index_integrity", {})
            if not integrity_check.get("consistency_check", False):
                recommendations.append("🔧 Recriar índice: python setup_rag.py")
            
            faiss_test = report.get("faiss_loading_test", {})
            if not faiss_test.get("direct_load_success", False):
                recommendations.append("🔄 Converter para PyTorch: usar convert_faiss_to_pytorch()")
            
            model_test = report.get("embedding_model_test", {})
            if not model_test.get("model_load_success", False):
                recommendations.append("🤖 Verificar modelo de embedding: baixar manualmente se necessário")
        
        return recommendations
    
    def _save_report(self, report: Dict[str, Any]):
        """
        Salva o relatório de correções.
        """
        try:
            report_path = Path("index_loading_fix_report.json")
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False, default=str)
            logger.info(f"📄 Relatório salvo em: {report_path.absolute()}")
        except Exception as e:
            logger.error(f"Erro ao salvar relatório: {e}")
    
    def _print_summary(self, report: Dict[str, Any]):
        """
        Imprime resumo das correções.
        """
        print("\n" + "="*80)
        print("🔧 RELATÓRIO DE CORREÇÃO DO CARREGAMENTO DO ÍNDICE")
        print("="*80)
        
        # Sistema
        system_check = report.get("system_check", {})
        print(f"\n💻 Sistema:")
        print(f"   PyTorch: {system_check.get('torch_available', False)} ({system_check.get('torch_version', 'N/A')})")
        print(f"   CUDA: {system_check.get('cuda_available', False)}")
        print(f"   GPU: {system_check.get('gpu_name', 'N/A')}")
        print(f"   FAISS: {system_check.get('faiss_available', False)}")
        print(f"   FAISS-GPU: {system_check.get('faiss_gpu_available', False)}")
        
        # Integridade
        integrity = report.get("index_integrity", {})
        print(f"\n📁 Integridade do Índice:")
        print(f"   Documentos: {integrity.get('documents_count', 0)}")
        print(f"   Metadados: {integrity.get('metadata_count', 0)}")
        print(f"   Embeddings: {integrity.get('embeddings_shape', 'N/A')}")
        print(f"   Consistente: {integrity.get('consistency_check', False)}")
        
        # Testes de carregamento
        faiss_test = report.get("faiss_loading_test", {})
        pytorch_test = report.get("pytorch_loading_test", {})
        print(f"\n🔍 Testes de Carregamento:")
        print(f"   FAISS direto: {faiss_test.get('direct_load_success', False)}")
        print(f"   FAISS temporário: {faiss_test.get('temp_load_success', False)}")
        print(f"   PyTorch embeddings: {pytorch_test.get('embeddings_load_success', False)}")
        print(f"   GPU transfer: {pytorch_test.get('gpu_transfer_success', False)}")
        
        # Teste final
        final_test = report.get("final_test", {})
        print(f"\n🧪 Teste Final:")
        print(f"   Inicialização: {final_test.get('rag_retriever_init', False)}")
        print(f"   Carregamento: {final_test.get('index_loading', False)}")
        print(f"   Busca: {final_test.get('search_test', False)}")
        print(f"   Backend: {final_test.get('backend_type', 'N/A')}")
        print(f"   Resultados: {final_test.get('search_results_count', 0)}")
        
        # Correções aplicadas
        fixes = self.fixes_applied
        if fixes:
            print(f"\n✅ Correções Aplicadas:")
            for i, fix in enumerate(fixes, 1):
                print(f"   {i}. {fix}")
        
        # Erros encontrados
        errors = self.errors_found
        if errors:
            print(f"\n❌ Erros Encontrados:")
            for i, error in enumerate(errors, 1):
                print(f"   {i}. {error}")
        
        # Recomendações
        recommendations = report.get("recommendations", [])
        if recommendations:
            print(f"\n💡 Recomendações:")
            for i, rec in enumerate(recommendations, 1):
                print(f"   {i}. {rec}")
        
        print("\n" + "="*80)
        
        if final_test.get("search_test", False):
            print("🎉 CARREGAMENTO DO ÍNDICE CORRIGIDO COM SUCESSO!")
        else:
            print("⚠️ CARREGAMENTO AINDA PRECISA DE AJUSTES")
        
        print("📄 Relatório detalhado: index_loading_fix_report.json")
        print("="*80)

def main():
    """
    Função principal da correção.
    """
    print("🚀 Iniciando correção do carregamento do índice RAG...")
    
    fixer = IndexLoadingFixer()
    report = fixer.run_comprehensive_fix()
    
    print("\n✅ Correção concluída!")

if __name__ == "__main__":
    main()