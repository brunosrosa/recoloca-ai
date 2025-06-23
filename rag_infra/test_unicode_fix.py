#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples para verificar se o problema de codificação Unicode foi resolvido.
"""

import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from core.constants import STATUS_MESSAGES
    print("✓ Importação de constants bem-sucedida")
    
    # Testar as mensagens que antes causavam erro
    print("✓ Testando mensagens de status:")
    print(f"  - GPU disponível: {STATUS_MESSAGES['gpu_available']}")
    print(f"  - GPU indisponível: {STATUS_MESSAGES['gpu_unavailable']}")
    print(f"  - Modelo carregado: {STATUS_MESSAGES['model_loaded']}")
    
    print("\n✓ Teste de codificação Unicode passou com sucesso!")
    
except Exception as e:
    print(f"✗ Erro durante o teste: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)