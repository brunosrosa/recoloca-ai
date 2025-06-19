#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de debug para conversão FAISS para PyTorch

Este script testa especificamente a conversão e identifica problemas.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import json
import logging
import sys
import os
from pathlib import Path

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from rag_infra.core_logic.constants import (
    FAISS_INDEX_DIR,
    FAISS_INDEX_FILE,
    FAISS_DOCUMENTS_FILE,
    FAISS_METADATA_FILE
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def debug_conversion():
    """Debug da conversão FAISS para PyTorch."""
    try:
        print("🔍 Debug da Conversão FAISS para PyTorch")
        print("=" * 50)
        
        # 1. Verificar arquivos base
        print("\n1. Verificando arquivos base:")
        index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
        documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
        metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
        embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
        conversion_info_path = FAISS_INDEX_DIR / "pytorch_conversion_info.json"
        
        files_status = {
            "FAISS Index": index_path.exists(),
            "Documents": documents_path.exists(),
            "Metadata": metadata_path.exists(),
            "Embeddings (PyTorch)": embeddings_path.exists(),
            "Conversion Info": conversion_info_path.exists()
        }
        
        for name, exists in files_status.items():
            status = "✅ Existe" if exists else "❌ Não existe"
            print(f"  {name}: {status}")
        
        # 2. Verificar dados se existem
        if embeddings_path.exists():
            print("\n2. Verificando embeddings PyTorch:")
            embeddings = np.load(str(embeddings_path))
            print(f"  Shape: {embeddings.shape}")
            print(f"  Dtype: {embeddings.dtype}")
            print(f"  Min/Max: {embeddings.min():.6f} / {embeddings.max():.6f}")
            print(f"  Tem NaN: {np.isnan(embeddings).any()}")
            print(f"  Tem Inf: {np.isinf(embeddings).any()}")
        
        if documents_path.exists():
            print("\n3. Verificando documentos:")
            with open(documents_path, 'r', encoding='utf-8') as f:
                documents = json.load(f)
            print(f"  Total documentos: {len(documents)}")
            if documents:
                print(f"  Primeiro documento (primeiros 100 chars): {documents[0][:100]}...")
        
        if metadata_path.exists():
            print("\n4. Verificando metadados:")
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata_data = json.load(f)
            
            if isinstance(metadata_data, list):
                metadata = metadata_data
                print(f"  Formato: Lista direta")
            else:
                metadata = metadata_data.get("documents_metadata", [])
                print(f"  Formato: Objeto com chave")
            
            print(f"  Total metadados: {len(metadata)}")
            if metadata:
                print(f"  Primeiro metadata: {metadata[0]}")
        
        if conversion_info_path.exists():
            print("\n5. Verificando info da conversão:")
            with open(conversion_info_path, 'r', encoding='utf-8') as f:
                conversion_info = json.load(f)
            
            for key, value in conversion_info.items():
                print(f"  {key}: {value}")
        
        # 3. Verificar consistência
        print("\n6. Verificando consistência:")
        if all([embeddings_path.exists(), documents_path.exists(), metadata_path.exists()]):
            embeddings = np.load(str(embeddings_path))
            
            with open(documents_path, 'r', encoding='utf-8') as f:
                documents = json.load(f)
            
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata_data = json.load(f)
                if isinstance(metadata_data, list):
                    metadata = metadata_data
                else:
                    metadata = metadata_data.get("documents_metadata", [])
            
            checks = {
                "Embeddings vs Documentos": embeddings.shape[0] == len(documents),
                "Documentos vs Metadados": len(documents) == len(metadata),
                "Embeddings não vazio": embeddings.shape[0] > 0,
                "Embeddings dtype válido": embeddings.dtype in [np.float32, np.float64],
                "Embeddings sem NaN": not np.isnan(embeddings).any(),
                "Embeddings sem Inf": not np.isinf(embeddings).any()
            }
            
            all_passed = True
            for check_name, passed in checks.items():
                status = "✅ PASSOU" if passed else "❌ FALHOU"
                print(f"  {check_name}: {status}")
                if not passed:
                    all_passed = False
            
            print(f"\n📊 Resumo:")
            print(f"  Embeddings: {embeddings.shape[0]}")
            print(f"  Documentos: {len(documents)}")
            print(f"  Metadados: {len(metadata)}")
            
            if all_passed:
                print("\n✅ Todos os checks passaram!")
                return True
            else:
                print("\n❌ Alguns checks falharam.")
                return False
        else:
            print("  ❌ Arquivos necessários não encontrados")
            return False
            
    except Exception as e:
        logger.error(f"Erro no debug: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal."""
    success = debug_conversion()
    
    if success:
        print("\n🎉 Conversão está funcionando corretamente!")
    else:
        print("\n🔧 Problemas detectados na conversão.")
        print("\n💡 Sugestões:")
        print("  1. Execute novamente o script de conversão")
        print("  2. Verifique se o índice FAISS está correto")
        print("  3. Recrie o índice se necessário")

if __name__ == "__main__":
    main()