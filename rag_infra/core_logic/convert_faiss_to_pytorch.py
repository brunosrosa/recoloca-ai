#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversor de índice FAISS para PyTorch GPU

Este script converte o índice FAISS existente para o formato PyTorch,
extrai os embeddings e os salva como arquivo .npy para uso com GPU.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import json
import logging
import time
from pathlib import Path
from typing import Optional

import numpy as np
import faiss

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core_logic.constants import (
    FAISS_INDEX_DIR,
    FAISS_INDEX_FILE,
    FAISS_DOCUMENTS_FILE,
    FAISS_METADATA_FILE,
    LOGS_DIR
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Criar handler para arquivo de log
LOGS_DIR.mkdir(parents=True, exist_ok=True)
file_handler = logging.FileHandler(LOGS_DIR / "faiss_to_pytorch_converter.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def extract_embeddings_from_faiss(index_path: Path) -> Optional[np.ndarray]:
    """
    Extrai embeddings do índice FAISS.
    
    Args:
        index_path: Caminho para o arquivo do índice FAISS
        
    Returns:
        np.ndarray: Array com os embeddings extraídos
    """
    try:
        logger.info(f"Carregando índice FAISS de: {index_path}")
        
        # Usar diretório temporário para evitar problemas com Unicode
        import tempfile
        import shutil
        from uuid import uuid4
        
        temp_dir = "C:\\Temp" if os.name == "nt" else "/tmp"
        if not Path(temp_dir).exists():
            Path(temp_dir).mkdir(parents=True, exist_ok=True)
        
        with tempfile.TemporaryDirectory(dir=temp_dir) as temp_path:
            temp_file_path = Path(temp_path) / f"faiss_index_{uuid4().hex}.bin"
            shutil.copy2(str(index_path), str(temp_file_path))
            index = faiss.read_index(str(temp_file_path))
        
        logger.info(f"Índice carregado: {index.ntotal} vetores, dimensão {index.d}")
        
        # Verificar tipo do índice
        if hasattr(index, 'reconstruct_n'):
            # Índice que suporta reconstrução
            logger.info("Extraindo embeddings usando reconstruct_n...")
            embeddings = index.reconstruct_n(0, index.ntotal)
            
        elif hasattr(index, 'xb') and index.xb is not None:
            # Índice Flat - acesso direto aos dados
            logger.info("Extraindo embeddings de índice Flat...")
            embeddings = faiss.vector_to_array(index.xb).reshape(index.ntotal, index.d)
            
        else:
            # Tentar extrair usando reconstruct individual
            logger.info("Extraindo embeddings usando reconstruct individual...")
            embeddings = np.zeros((index.ntotal, index.d), dtype=np.float32)
            
            batch_size = 1000
            for i in range(0, index.ntotal, batch_size):
                end_idx = min(i + batch_size, index.ntotal)
                for j in range(i, end_idx):
                    try:
                        embeddings[j] = index.reconstruct(j)
                    except Exception as e:
                        logger.warning(f"Erro ao reconstruir vetor {j}: {e}")
                        # Preencher com zeros se não conseguir reconstruir
                        embeddings[j] = np.zeros(index.d, dtype=np.float32)
                
                if i % 5000 == 0:
                    logger.info(f"Progresso: {i}/{index.ntotal} embeddings extraídos")
        
        logger.info(f"Embeddings extraídos: shape {embeddings.shape}")
        return embeddings
        
    except Exception as e:
        logger.error(f"Erro ao extrair embeddings: {str(e)}")
        return None

def convert_faiss_to_pytorch() -> bool:
    """
    Converte o índice FAISS para formato PyTorch.
    
    Returns:
        bool: True se conversão foi bem-sucedida
    """
    try:
        logger.info("Iniciando conversão FAISS para PyTorch...")
        start_time = time.time()
        
        # Verificar se os arquivos FAISS existem
        index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
        documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
        metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
        
        if not all([index_path.exists(), documents_path.exists(), metadata_path.exists()]):
            logger.error("Arquivos FAISS não encontrados. Execute a indexação primeiro.")
            return False
        
        # 1. Extrair embeddings do FAISS
        logger.info("Extraindo embeddings do índice FAISS...")
        embeddings = extract_embeddings_from_faiss(index_path)
        
        if embeddings is None:
            logger.error("Falha ao extrair embeddings")
            return False
        
        # 2. Salvar embeddings como arquivo .npy
        embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
        logger.info(f"Salvando embeddings em: {embeddings_path}")
        np.save(str(embeddings_path), embeddings)
        
        # 3. Verificar consistência com documentos
        with open(documents_path, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata_data = json.load(f)
            metadata = metadata_data.get("documents_metadata", [])
        
        logger.info(f"Verificando consistência:")
        logger.info(f"  - Embeddings: {embeddings.shape[0]}")
        logger.info(f"  - Documentos: {len(documents)}")
        logger.info(f"  - Metadados: {len(metadata)}")
        
        if embeddings.shape[0] != len(documents):
            logger.warning(f"Inconsistência detectada: {embeddings.shape[0]} embeddings vs {len(documents)} documentos")
        
        # 4. Criar arquivo de informações da conversão
        conversion_info = {
            "conversion_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "original_faiss_index": str(index_path),
            "embeddings_shape": list(embeddings.shape),
            "embeddings_dtype": str(embeddings.dtype),
            "documents_count": len(documents),
            "metadata_count": len(metadata),
            "conversion_time_seconds": time.time() - start_time
        }
        
        conversion_info_path = FAISS_INDEX_DIR / "pytorch_conversion_info.json"
        with open(conversion_info_path, 'w', encoding='utf-8') as f:
            json.dump(conversion_info, f, indent=2, ensure_ascii=False)
        
        elapsed_time = time.time() - start_time
        logger.info(f"✅ Conversão concluída em {elapsed_time:.2f}s")
        logger.info(f"Arquivos criados:")
        logger.info(f"  - {embeddings_path}")
        logger.info(f"  - {conversion_info_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Erro na conversão: {str(e)}")
        return False

def verify_pytorch_data() -> bool:
    """
    Verifica se os dados PyTorch foram criados corretamente.
    
    Returns:
        bool: True se dados estão válidos
    """
    try:
        logger.info("Verificando dados PyTorch...")
        
        embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
        documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
        metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
        conversion_info_path = FAISS_INDEX_DIR / "pytorch_conversion_info.json"
        
        # Verificar se arquivos existem
        missing_files = []
        for path in [embeddings_path, documents_path, metadata_path, conversion_info_path]:
            if not path.exists():
                missing_files.append(str(path))
        
        if missing_files:
            logger.error(f"Arquivos não encontrados: {missing_files}")
            return False
        
        # Carregar e verificar embeddings
        embeddings = np.load(str(embeddings_path))
        logger.info(f"Embeddings carregados: shape {embeddings.shape}, dtype {embeddings.dtype}")
        
        # Carregar documentos
        with open(documents_path, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        
        # Carregar metadados
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata_data = json.load(f)
            metadata = metadata_data.get("documents_metadata", [])
        
        # Carregar info da conversão
        with open(conversion_info_path, 'r', encoding='utf-8') as f:
            conversion_info = json.load(f)
        
        # Verificar consistência
        checks = {
            "embeddings_shape_consistency": embeddings.shape[0] == len(documents),
            "metadata_consistency": len(documents) == len(metadata),
            "embeddings_not_empty": embeddings.shape[0] > 0,
            "embeddings_valid_dtype": embeddings.dtype in [np.float32, np.float64],
            "conversion_info_valid": "conversion_date" in conversion_info
        }
        
        logger.info("Resultados da verificação:")
        all_passed = True
        for check_name, passed in checks.items():
            status = "✅ PASSOU" if passed else "❌ FALHOU"
            logger.info(f"  {check_name}: {status}")
            if not passed:
                all_passed = False
        
        if all_passed:
            logger.info("✅ Todos os dados PyTorch estão válidos")
        else:
            logger.error("❌ Problemas detectados nos dados PyTorch")
        
        return all_passed
        
    except Exception as e:
        logger.error(f"Erro na verificação: {str(e)}")
        return False

def main():
    """
    Função principal.
    """
    print("Conversor FAISS para PyTorch GPU")
    print("=" * 40)
    
    # Verificar se já existe conversão
    embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
    if embeddings_path.exists():
        print("⚠️  Embeddings PyTorch já existem.")
        response = input("Deseja reconverter? (s/N): ").strip().lower()
        if response not in ['s', 'sim', 'y', 'yes']:
            print("Verificando dados existentes...")
            if verify_pytorch_data():
                print("✅ Dados PyTorch válidos. Conversão não necessária.")
                return
            else:
                print("❌ Dados PyTorch inválidos. Reconvertendo...")
    
    # Executar conversão
    if convert_faiss_to_pytorch():
        print("\n✅ Conversão concluída com sucesso!")
        
        # Verificar resultado
        if verify_pytorch_data():
            print("✅ Dados PyTorch verificados e válidos")
            print("\n🚀 Agora você pode usar o PyTorchGPURetriever!")
        else:
            print("❌ Problemas detectados após conversão")
    else:
        print("❌ Falha na conversão")

if __name__ == "__main__":
    main()