# -*- coding: utf-8 -*-
"""
Módulo de Diagnósticos - RAG Infra

Este módulo contém scripts para diagnóstico e correção do sistema RAG.

Módulos disponíveis:
- correcao_rag: Script de correção do sistema RAG
- diagnostico_rag: Script de diagnóstico completo
- diagnostico_simples: Script de diagnóstico simplificado

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

__version__ = "1.0.0"
__author__ = "@AgenteM_DevFastAPI"

# Imports principais para facilitar o uso
try:
    from . import correcao_rag
    from . import diagnostico_rag
    from . import diagnostico_simples
except ImportError:
    # Imports opcionais para evitar erros durante a reorganização
    pass

__all__ = [
    "correcao_rag",
    "diagnostico_rag", 
    "diagnostico_simples"
]