#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..core_logic.constants import FAISS_INDEX_DIR, FAISS_INDEX_FILE
from pathlib import Path

print(f'FAISS_INDEX_DIR: {FAISS_INDEX_DIR}')
print(f'FAISS_INDEX_FILE: {FAISS_INDEX_FILE}')
print(f'Caminho completo: {FAISS_INDEX_DIR / FAISS_INDEX_FILE}')
print(f'Diretório existe: {FAISS_INDEX_DIR.exists()}')
print(f'Diretório absoluto: {FAISS_INDEX_DIR.absolute()}')

# Verificar se há algum problema com o caminho
try:
    # Tentar criar um arquivo de teste
    test_file = FAISS_INDEX_DIR / 'test.txt'
    with open(test_file, 'w') as f:
        f.write('teste')
    print('✅ Conseguiu escrever arquivo de teste')
    test_file.unlink()  # Remover arquivo de teste
except Exception as e:
    print(f'❌ Erro ao escrever arquivo: {e}')