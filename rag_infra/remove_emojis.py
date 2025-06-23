#!/usr/bin/env python3
"""
Script para remover emojis de arquivos Python que causam UnicodeEncodeError no Windows.
"""

import os
import re
from pathlib import Path

# Padrão regex para detectar emojis
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "]+", flags=re.UNICODE)

# Mapeamento de emojis para texto
EMOJI_REPLACEMENTS = {
    "🔍": "[SEARCH]",
    "✅": "[OK]",
    "❌": "[ERROR]",
    "🚀": "[START]",
    "⚠️": "[WARNING]",
    "💾": "[SAVE]",
    "📥": "[LOAD]",
}

def remove_emojis_from_file(file_path):
    """Remove emojis de um arquivo específico."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Substituir emojis específicos primeiro
        for emoji, replacement in EMOJI_REPLACEMENTS.items():
            content = content.replace(emoji, replacement)
        
        # Remover qualquer emoji restante
        content = EMOJI_PATTERN.sub('[EMOJI]', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Emojis removidos de: {file_path}")
            return True
        else:
            print(f"[SKIP] Nenhum emoji encontrado em: {file_path}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Erro ao processar {file_path}: {e}")
        return False

def main():
    """Função principal."""
    base_dir = Path("c:/Users/rosas/OneDrive/Documentos/Obisidian DB/Projects/Recoloca.AI/rag_infra/src")
    
    # Arquivos prioritários (que podem ser executados na inicialização)
    priority_files = [
        "core/constants.py",
        "core/embedding_model.py",
        "core/rag_retriever.py",
        "core/mcp_server.py",
        "utils/rag_utilities.py"
    ]
    
    print("[START] Removendo emojis dos arquivos prioritários...")
    
    files_modified = 0
    
    # Processar arquivos prioritários primeiro
    for file_rel_path in priority_files:
        file_path = base_dir / file_rel_path
        if file_path.exists():
            if remove_emojis_from_file(file_path):
                files_modified += 1
        else:
            print(f"[WARNING] Arquivo não encontrado: {file_path}")
    
    # Processar todos os arquivos .py recursivamente
    print("\n[START] Processando todos os arquivos Python...")
    
    for py_file in base_dir.rglob("*.py"):
        if py_file.name not in [f.split('/')[-1] for f in priority_files]:  # Pular arquivos já processados
            if remove_emojis_from_file(py_file):
                files_modified += 1
    
    print(f"\n[OK] Processamento concluído! {files_modified} arquivos modificados.")

if __name__ == "__main__":
    main()