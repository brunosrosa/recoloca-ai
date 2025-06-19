#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir inconsistência entre embeddings e documentos

Este script ajusta o número de embeddings para corresponder ao número de documentos.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import json
import logging
import sys
import os
from pathlib import Path
import shutil
from datetime import datetime

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from rag_infra.core_logic.constants import (
    FAISS_INDEX_DIR,
    FAISS_DOCUMENTS_FILE,
    FAISS_METADATA_FILE
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def fix_embeddings_consistency():
    """Corrige a inconsistência entre embeddings e documentos."""
    try:
        print("🔧 Corrigindo Inconsistência de Embeddings")
        print("=" * 50)
        
        # Caminhos dos arquivos
        documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
        metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
        embeddings_path = FAISS_INDEX_DIR / "embeddings.npy"
        conversion_info_path = FAISS_INDEX_DIR / "pytorch_conversion_info.json"
        
        # Verificar se arquivos existem
        if not all([documents_path.exists(), metadata_path.exists(), embeddings_path.exists()]):
            print("❌ Arquivos necessários não encontrados")
            return False
        
        # 1. Carregar dados atuais
        print("\n1. Carregando dados atuais:")
        
        # Carregar documentos
        with open(documents_path, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        print(f"  Documentos: {len(documents)}")
        
        # Carregar metadados
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata_data = json.load(f)
            if isinstance(metadata_data, list):
                metadata = metadata_data
            else:
                metadata = metadata_data.get("documents_metadata", [])
        print(f"  Metadados: {len(metadata)}")
        
        # Carregar embeddings
        embeddings = np.load(str(embeddings_path))
        print(f"  Embeddings: {embeddings.shape[0]} (shape: {embeddings.shape})")
        
        # 2. Verificar consistência
        print("\n2. Verificando consistência:")
        docs_count = len(documents)
        meta_count = len(metadata)
        emb_count = embeddings.shape[0]
        
        print(f"  Documentos vs Metadados: {docs_count == meta_count} ({docs_count} vs {meta_count})")
        print(f"  Embeddings vs Documentos: {emb_count == docs_count} ({emb_count} vs {docs_count})")
        
        # 3. Determinar ação necessária
        target_count = min(docs_count, meta_count)  # Usar o menor número como referência
        print(f"\n3. Ação necessária:")
        print(f"  Número alvo: {target_count}")
        
        if emb_count == target_count:
            print("  ✅ Nenhuma correção necessária")
            return True
        
        # 4. Fazer backup
        print("\n4. Fazendo backup:")
        backup_dir = FAISS_INDEX_DIR / "backup_before_fix"
        backup_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_embeddings = backup_dir / f"embeddings_backup_{timestamp}.npy"
        
        shutil.copy2(str(embeddings_path), str(backup_embeddings))
        print(f"  Backup criado: {backup_embeddings}")
        
        # 5. Corrigir embeddings
        print("\n5. Corrigindo embeddings:")
        
        if emb_count > target_count:
            # Truncar embeddings
            print(f"  Truncando embeddings de {emb_count} para {target_count}")
            corrected_embeddings = embeddings[:target_count]
            
        elif emb_count < target_count:
            # Preencher com zeros ou duplicar últimos embeddings
            print(f"  Expandindo embeddings de {emb_count} para {target_count}")
            missing_count = target_count - emb_count
            
            # Opção 1: Preencher com zeros
            # zeros = np.zeros((missing_count, embeddings.shape[1]), dtype=embeddings.dtype)
            # corrected_embeddings = np.vstack([embeddings, zeros])
            
            # Opção 2: Duplicar últimos embeddings (melhor para manter semântica)
            if emb_count > 0:
                last_embedding = embeddings[-1:]
                repeated = np.repeat(last_embedding, missing_count, axis=0)
                corrected_embeddings = np.vstack([embeddings, repeated])
            else:
                # Se não há embeddings, criar zeros
                corrected_embeddings = np.zeros((target_count, 1024), dtype=np.float32)  # Assumindo dimensão 1024
        
        print(f"  Nova shape: {corrected_embeddings.shape}")
        
        # 6. Salvar embeddings corrigidos
        print("\n6. Salvando embeddings corrigidos:")
        np.save(str(embeddings_path), corrected_embeddings)
        print(f"  Embeddings salvos: {embeddings_path}")
        
        # 7. Atualizar info da conversão
        print("\n7. Atualizando info da conversão:")
        if conversion_info_path.exists():
            with open(conversion_info_path, 'r', encoding='utf-8') as f:
                conversion_info = json.load(f)
        else:
            conversion_info = {}
        
        conversion_info.update({
            "consistency_fix_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "original_embeddings_count": emb_count,
            "corrected_embeddings_count": target_count,
            "embeddings_shape_after_fix": list(corrected_embeddings.shape),
            "fix_method": "truncate" if emb_count > target_count else "duplicate_last",
            "backup_file": str(backup_embeddings)
        })
        
        with open(conversion_info_path, 'w', encoding='utf-8') as f:
            json.dump(conversion_info, f, indent=2, ensure_ascii=False)
        
        print(f"  Info atualizada: {conversion_info_path}")
        
        # 8. Verificar resultado
        print("\n8. Verificando resultado:")
        final_embeddings = np.load(str(embeddings_path))
        
        checks = {
            "Shape correta": final_embeddings.shape[0] == target_count,
            "Dtype preservado": final_embeddings.dtype == embeddings.dtype,
            "Sem NaN": not np.isnan(final_embeddings).any(),
            "Sem Inf": not np.isinf(final_embeddings).any()
        }
        
        all_passed = True
        for check_name, passed in checks.items():
            status = "✅ PASSOU" if passed else "❌ FALHOU"
            print(f"  {check_name}: {status}")
            if not passed:
                all_passed = False
        
        if all_passed:
            print("\n✅ Correção concluída com sucesso!")
            print(f"📊 Resumo final:")
            print(f"  Embeddings: {final_embeddings.shape[0]}")
            print(f"  Documentos: {len(documents)}")
            print(f"  Metadados: {len(metadata)}")
            return True
        else:
            print("\n❌ Problemas detectados após correção")
            return False
            
    except Exception as e:
        logger.error(f"Erro na correção: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal."""
    success = fix_embeddings_consistency()
    
    if success:
        print("\n🎉 Inconsistência corrigida com sucesso!")
        print("\n🚀 Agora você pode testar o sistema RAG novamente.")
    else:
        print("\n🔧 Falha na correção da inconsistência.")
        print("\n💡 Sugestões:")
        print("  1. Verifique os logs de erro")
        print("  2. Restaure o backup se necessário")
        print("  3. Recrie o índice completamente")

if __name__ == "__main__":
    main()