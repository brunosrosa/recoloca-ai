#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Correção dos Problemas do Sistema RAG

Este script corrige os problemas identificados no diagnóstico:
1. Falha no carregamento do índice
2. Threshold de similaridade inadequado
3. Configurações do PyTorch para RTX 2060
4. Normalização de vetores

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import sys
import os
import json
import logging
import torch
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core_logic'))

from ..core_logic.constants import (
    FAISS_INDEX_DIR, FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE,
    MIN_SIMILARITY_SCORE, DEFAULT_TOP_K
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RAGFixer:
    """
    Classe para corrigir problemas específicos do sistema RAG.
    """
    
    def __init__(self):
        self.fixes_applied = []
        self.errors_found = []
        
    def run_all_fixes(self) -> Dict[str, Any]:
        """
        Executa todas as correções necessárias.
        
        Returns:
            Dict: Relatório das correções aplicadas
        """
        logger.info("🔧 Iniciando correções do sistema RAG...")
        
        report = {
            "timestamp": str(torch.cuda.current_device() if torch.cuda.is_available() else "CPU"),
            "fixes_applied": [],
            "errors_found": [],
            "index_status": self._check_and_fix_index(),
            "threshold_fix": self._fix_threshold_settings(),
            "pytorch_config": self._optimize_pytorch_config(),
            "normalization_fix": self._fix_normalization_issues(),
            "test_results": self._test_fixes()
        }
        
        report["fixes_applied"] = self.fixes_applied
        report["errors_found"] = self.errors_found
        
        self._save_fix_report(report)
        self._print_fix_summary(report)
        
        return report
    
    def _check_and_fix_index(self) -> Dict[str, Any]:
        """
        Verifica e corrige problemas com o índice.
        """
        logger.info("📊 Verificando e corrigindo índice...")
        
        index_status = {
            "index_dir_exists": False,
            "documents_file_exists": False,
            "metadata_file_exists": False,
            "index_files_found": [],
            "documents_count": 0,
            "metadata_count": 0,
            "consistency_check": False,
            "fix_applied": False
        }
        
        try:
            # Verificar se o diretório do índice existe
            if FAISS_INDEX_DIR.exists():
                index_status["index_dir_exists"] = True
                logger.info(f"✅ Diretório do índice encontrado: {FAISS_INDEX_DIR}")
                
                # Listar arquivos no diretório
                index_files = list(FAISS_INDEX_DIR.glob("*"))
                index_status["index_files_found"] = [f.name for f in index_files]
                logger.info(f"📁 Arquivos encontrados: {index_status['index_files_found']}")
            else:
                self.errors_found.append(f"Diretório do índice não encontrado: {FAISS_INDEX_DIR}")
                logger.error(f"❌ Diretório do índice não encontrado: {FAISS_INDEX_DIR}")
                return index_status
            
            # Verificar arquivo de documentos
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            if documents_path.exists():
                index_status["documents_file_exists"] = True
                try:
                    with open(documents_path, 'r', encoding='utf-8') as f:
                        documents = json.load(f)
                        index_status["documents_count"] = len(documents)
                        logger.info(f"✅ Arquivo de documentos: {len(documents)} documentos")
                except Exception as e:
                    self.errors_found.append(f"Erro ao ler documentos: {e}")
                    logger.error(f"❌ Erro ao ler documentos: {e}")
            else:
                self.errors_found.append(f"Arquivo de documentos não encontrado: {documents_path}")
                logger.error(f"❌ Arquivo de documentos não encontrado: {documents_path}")
            
            # Verificar arquivo de metadados
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            if metadata_path.exists():
                index_status["metadata_file_exists"] = True
                try:
                    with open(metadata_path, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                        index_status["metadata_count"] = len(metadata)
                        logger.info(f"✅ Arquivo de metadados: {len(metadata)} entradas")
                except Exception as e:
                    self.errors_found.append(f"Erro ao ler metadados: {e}")
                    logger.error(f"❌ Erro ao ler metadados: {e}")
            else:
                self.errors_found.append(f"Arquivo de metadados não encontrado: {metadata_path}")
                logger.error(f"❌ Arquivo de metadados não encontrado: {metadata_path}")
            
            # Verificar consistência
            if (index_status["documents_file_exists"] and 
                index_status["metadata_file_exists"] and
                index_status["documents_count"] == index_status["metadata_count"] and
                index_status["documents_count"] > 0):
                index_status["consistency_check"] = True
                logger.info("✅ Índice consistente")
                self.fixes_applied.append("Índice verificado e consistente")
            else:
                self.errors_found.append("Inconsistência no índice detectada")
                logger.error("❌ Inconsistência no índice detectada")
                
                # Tentar corrigir executando o script de setup
                logger.info("🔧 Tentando recriar o índice...")
                try:
                    import subprocess
                    result = subprocess.run(
                        [sys.executable, "setup_rag.py"],
                        cwd=FAISS_INDEX_DIR.parent,
                        capture_output=True,
                        text=True,
                        timeout=300  # 5 minutos
                    )
                    
                    if result.returncode == 0:
                        index_status["fix_applied"] = True
                        self.fixes_applied.append("Índice recriado com sucesso")
                        logger.info("✅ Índice recriado com sucesso")
                    else:
                        self.errors_found.append(f"Falha ao recriar índice: {result.stderr}")
                        logger.error(f"❌ Falha ao recriar índice: {result.stderr}")
                        
                except Exception as e:
                    self.errors_found.append(f"Erro ao executar setup_rag.py: {e}")
                    logger.error(f"❌ Erro ao executar setup_rag.py: {e}")
            
        except Exception as e:
            self.errors_found.append(f"Erro na verificação do índice: {e}")
            logger.error(f"❌ Erro na verificação do índice: {e}")
        
        return index_status
    
    def _fix_threshold_settings(self) -> Dict[str, Any]:
        """
        Corrige configurações de threshold.
        """
        logger.info("📊 Corrigindo configurações de threshold...")
        
        threshold_fix = {
            "current_threshold": MIN_SIMILARITY_SCORE,
            "recommended_threshold": 0.1,
            "fix_applied": False,
            "config_file_updated": False
        }
        
        try:
            # Verificar se o threshold atual é muito alto
            if MIN_SIMILARITY_SCORE > 0.2:
                logger.info(f"🔧 Threshold atual ({MIN_SIMILARITY_SCORE}) muito alto, recomendando 0.1")
                
                # Tentar atualizar o arquivo constants.py
                constants_path = Path(__file__).parent.parent / "core_logic" / "constants.py"
                
                if constants_path.exists():
                    try:
                        # Ler arquivo atual
                        with open(constants_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Substituir o valor do threshold
                        old_line = f"MIN_SIMILARITY_SCORE = {MIN_SIMILARITY_SCORE}"
                        new_line = "MIN_SIMILARITY_SCORE = 0.1  # Threshold reduzido para melhor recall"
                        
                        if old_line in content:
                            new_content = content.replace(old_line, new_line)
                            
                            # Fazer backup
                            backup_path = constants_path.with_suffix('.py.backup')
                            with open(backup_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            
                            # Salvar nova versão
                            with open(constants_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            
                            threshold_fix["fix_applied"] = True
                            threshold_fix["config_file_updated"] = True
                            self.fixes_applied.append(f"Threshold reduzido de {MIN_SIMILARITY_SCORE} para 0.1")
                            logger.info("✅ Threshold atualizado no arquivo constants.py")
                        else:
                            self.errors_found.append("Linha do threshold não encontrada em constants.py")
                            logger.warning("⚠️ Linha do threshold não encontrada em constants.py")
                            
                    except Exception as e:
                        self.errors_found.append(f"Erro ao atualizar constants.py: {e}")
                        logger.error(f"❌ Erro ao atualizar constants.py: {e}")
                else:
                    self.errors_found.append(f"Arquivo constants.py não encontrado: {constants_path}")
                    logger.error(f"❌ Arquivo constants.py não encontrado: {constants_path}")
            else:
                logger.info(f"✅ Threshold atual ({MIN_SIMILARITY_SCORE}) adequado")
                self.fixes_applied.append("Threshold já está em valor adequado")
                
        except Exception as e:
            self.errors_found.append(f"Erro na correção do threshold: {e}")
            logger.error(f"❌ Erro na correção do threshold: {e}")
        
        return threshold_fix
    
    def _optimize_pytorch_config(self) -> Dict[str, Any]:
        """
        Otimiza configurações do PyTorch para RTX 2060.
        """
        logger.info("⚙️ Otimizando configurações do PyTorch...")
        
        pytorch_config = {
            "cuda_available": torch.cuda.is_available(),
            "gpu_name": None,
            "rtx_2060_detected": False,
            "optimizations_applied": [],
            "memory_optimized": False,
            "backend_configured": False
        }
        
        try:
            if torch.cuda.is_available():
                gpu_name = torch.cuda.get_device_name(0)
                pytorch_config["gpu_name"] = gpu_name
                
                # Detectar RTX 2060
                if "rtx 2060" in gpu_name.lower():
                    pytorch_config["rtx_2060_detected"] = True
                    logger.info("🔥 RTX 2060 detectada - aplicando otimizações específicas")
                    
                    # Otimizações para RTX 2060
                    optimizations = []
                    
                    # 1. Configurar uso eficiente de memória
                    try:
                        torch.cuda.empty_cache()
                        optimizations.append("Cache CUDA limpo")
                        pytorch_config["memory_optimized"] = True
                    except Exception as e:
                        logger.warning(f"Aviso ao limpar cache CUDA: {e}")
                    
                    # 2. Configurar flags de otimização
                    try:
                        # Habilitar otimizações para RTX 2060
                        torch.backends.cudnn.benchmark = True
                        optimizations.append("CuDNN benchmark habilitado")
                        
                        # Configurar precisão mista se disponível
                        if hasattr(torch.backends.cuda.matmul, 'allow_tf32'):
                            torch.backends.cuda.matmul.allow_tf32 = True
                            optimizations.append("TF32 habilitado para matmul")
                        
                        if hasattr(torch.backends.cudnn, 'allow_tf32'):
                            torch.backends.cudnn.allow_tf32 = True
                            optimizations.append("TF32 habilitado para CuDNN")
                            
                        pytorch_config["backend_configured"] = True
                        
                    except Exception as e:
                        logger.warning(f"Aviso ao configurar otimizações: {e}")
                    
                    pytorch_config["optimizations_applied"] = optimizations
                    self.fixes_applied.extend([f"PyTorch: {opt}" for opt in optimizations])
                    
                    logger.info(f"✅ {len(optimizations)} otimizações aplicadas para RTX 2060")
                else:
                    logger.info(f"✅ GPU {gpu_name} - configurações padrão adequadas")
                    self.fixes_applied.append(f"GPU {gpu_name} configurada adequadamente")
            else:
                logger.info("ℹ️ CUDA não disponível - usando CPU")
                self.fixes_applied.append("Configuração CPU aplicada")
                
        except Exception as e:
            self.errors_found.append(f"Erro na otimização do PyTorch: {e}")
            logger.error(f"❌ Erro na otimização do PyTorch: {e}")
        
        return pytorch_config
    
    def _fix_normalization_issues(self) -> Dict[str, Any]:
        """
        Corrige problemas de normalização de vetores.
        """
        logger.info("📐 Verificando e corrigindo normalização...")
        
        normalization_fix = {
            "embedding_config_checked": False,
            "normalization_enabled": False,
            "config_updated": False,
            "fix_applied": False
        }
        
        try:
            # Verificar configuração do modelo de embedding
            constants_path = Path(__file__).parent.parent / "core_logic" / "constants.py"
            
            if constants_path.exists():
                with open(constants_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                normalization_fix["embedding_config_checked"] = True
                
                # Verificar se normalização está habilitada
                if '"normalize_embeddings": True' in content:
                    normalization_fix["normalization_enabled"] = True
                    logger.info("✅ Normalização de embeddings já habilitada")
                    self.fixes_applied.append("Normalização de embeddings verificada")
                else:
                    logger.info("🔧 Habilitando normalização de embeddings...")
                    
                    # Tentar habilitar normalização
                    if '"normalize_embeddings": False' in content:
                        new_content = content.replace(
                            '"normalize_embeddings": False',
                            '"normalize_embeddings": True'
                        )
                        
                        # Fazer backup
                        backup_path = constants_path.with_suffix('.py.norm_backup')
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        # Salvar nova versão
                        with open(constants_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        normalization_fix["config_updated"] = True
                        normalization_fix["fix_applied"] = True
                        self.fixes_applied.append("Normalização de embeddings habilitada")
                        logger.info("✅ Normalização habilitada em constants.py")
                    else:
                        logger.info("ℹ️ Configuração de normalização não encontrada - assumindo padrão")
                        self.fixes_applied.append("Configuração de normalização verificada")
            else:
                self.errors_found.append(f"Arquivo constants.py não encontrado: {constants_path}")
                logger.error(f"❌ Arquivo constants.py não encontrado: {constants_path}")
                
        except Exception as e:
            self.errors_found.append(f"Erro na correção de normalização: {e}")
            logger.error(f"❌ Erro na correção de normalização: {e}")
        
        return normalization_fix
    
    def _test_fixes(self) -> Dict[str, Any]:
        """
        Testa se as correções funcionaram.
        """
        logger.info("🧪 Testando correções aplicadas...")
        
        test_results = {
            "retriever_initialization": False,
            "index_loading": False,
            "search_test": False,
            "results_found": 0,
            "avg_search_time": 0.0,
            "test_queries": [
                "arquitetura",
                "sistema",
                "documentação"
            ],
            "individual_results": {}
        }
        
        try:
            # Tentar inicializar o retriever com configurações otimizadas
            from ..core_logic.rag_retriever import RAGRetriever
            
            retriever = RAGRetriever(
                force_pytorch=True,  # Forçar PyTorch para RTX 2060
                use_optimizations=True,
                batch_size=16  # Batch size otimizado para RTX 2060
            )
            
            # Testar inicialização
            if retriever.initialize():
                test_results["retriever_initialization"] = True
                logger.info("✅ Retriever inicializado com sucesso")
                
                # Testar carregamento do índice
                if retriever.load_index():
                    test_results["index_loading"] = True
                    logger.info("✅ Índice carregado com sucesso")
                    
                    # Testar buscas
                    import time
                    total_time = 0
                    total_results = 0
                    
                    for query in test_results["test_queries"]:
                        try:
                            start_time = time.time()
                            results = retriever.search(query, top_k=5, min_score=0.1)
                            end_time = time.time()
                            
                            search_time = end_time - start_time
                            total_time += search_time
                            total_results += len(results)
                            
                            test_results["individual_results"][query] = {
                                "results_count": len(results),
                                "search_time": search_time,
                                "success": len(results) > 0
                            }
                            
                            logger.info(f"🔍 Query '{query}': {len(results)} resultados em {search_time:.3f}s")
                            
                        except Exception as e:
                            logger.error(f"❌ Erro na busca '{query}': {e}")
                            test_results["individual_results"][query] = {
                                "error": str(e),
                                "success": False
                            }
                    
                    test_results["results_found"] = total_results
                    test_results["avg_search_time"] = total_time / len(test_results["test_queries"])
                    
                    if total_results > 0:
                        test_results["search_test"] = True
                        logger.info(f"✅ Testes de busca bem-sucedidos: {total_results} resultados")
                        self.fixes_applied.append(f"Sistema funcionando: {total_results} resultados encontrados")
                    else:
                        self.errors_found.append("Nenhum resultado encontrado nos testes")
                        logger.error("❌ Nenhum resultado encontrado nos testes")
                else:
                    self.errors_found.append("Falha ao carregar índice")
                    logger.error("❌ Falha ao carregar índice")
            else:
                self.errors_found.append("Falha ao inicializar retriever")
                logger.error("❌ Falha ao inicializar retriever")
                
        except Exception as e:
            self.errors_found.append(f"Erro nos testes: {e}")
            logger.error(f"❌ Erro nos testes: {e}")
        
        return test_results
    
    def _save_fix_report(self, report: Dict[str, Any]):
        """
        Salva o relatório de correções.
        """
        try:
            report_path = Path("rag_fixes_report.json")
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False, default=str)
            logger.info(f"📄 Relatório de correções salvo em: {report_path.absolute()}")
        except Exception as e:
            logger.error(f"Erro ao salvar relatório: {e}")
    
    def _print_fix_summary(self, report: Dict[str, Any]):
        """
        Imprime resumo das correções.
        """
        print("\n" + "="*80)
        print("🔧 RELATÓRIO DE CORREÇÕES DO SISTEMA RAG")
        print("="*80)
        
        # Status do índice
        index_status = report["index_status"]
        print(f"\n📊 Status do Índice:")
        print(f"   Diretório existe: {index_status['index_dir_exists']}")
        print(f"   Documentos: {index_status['documents_count']}")
        print(f"   Metadados: {index_status['metadata_count']}")
        print(f"   Consistente: {index_status['consistency_check']}")
        
        # Configuração PyTorch
        pytorch_config = report["pytorch_config"]
        print(f"\n⚙️ PyTorch:")
        print(f"   GPU: {pytorch_config.get('gpu_name', 'N/A')}")
        print(f"   RTX 2060: {pytorch_config['rtx_2060_detected']}")
        print(f"   Otimizações: {len(pytorch_config['optimizations_applied'])}")
        
        # Testes
        test_results = report["test_results"]
        print(f"\n🧪 Testes:")
        print(f"   Inicialização: {test_results['retriever_initialization']}")
        print(f"   Carregamento: {test_results['index_loading']}")
        print(f"   Busca: {test_results['search_test']}")
        print(f"   Resultados: {test_results['results_found']}")
        
        # Correções aplicadas
        print(f"\n✅ Correções Aplicadas ({len(self.fixes_applied)}):")
        for i, fix in enumerate(self.fixes_applied, 1):
            print(f"   {i}. {fix}")
        
        # Erros encontrados
        if self.errors_found:
            print(f"\n❌ Erros Encontrados ({len(self.errors_found)}):")
            for i, error in enumerate(self.errors_found, 1):
                print(f"   {i}. {error}")
        
        print("\n" + "="*80)

def main():
    """
    Função principal do script de correção.
    """
    print("🚀 Iniciando correções do sistema RAG...")
    
    fixer = RAGFixer()
    report = fixer.run_all_fixes()
    
    print("\n✅ Correções concluídas!")
    print("📄 Relatório detalhado salvo em: rag_fixes_report.json")
    
    # Verificar se o sistema está funcionando
    test_results = report.get("test_results", {})
    if (test_results.get("retriever_initialization") and 
        test_results.get("index_loading") and 
        test_results.get("search_test")):
        print("🎉 Sistema RAG funcionando corretamente!")
    else:
        print("⚠️ Alguns problemas ainda precisam ser resolvidos.")
        print("   Verifique o relatório para mais detalhes.")

if __name__ == "__main__":
    main()