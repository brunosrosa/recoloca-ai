#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

# Criar diretório do índice FAISS
path = Path('data_index/faiss_index_bge_m3')
path.mkdir(parents=True, exist_ok=True)
print(f'Diretório criado: {path.absolute()}')

# Verificar se o diretório existe
if path.exists():
    print('✅ Diretório existe e está acessível')
else:
    print('❌ Problema ao criar diretório')