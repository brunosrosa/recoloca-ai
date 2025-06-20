# -*- coding: utf-8 -*-
"""
Módulo de Configuração - RAG Infra

Este módulo contém scripts de configuração e inicialização do sistema RAG.

Módulos disponíveis:
- setup_rag: Script de configuração inicial do sistema

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

__version__ = "1.0.0"
__author__ = "@AgenteM_DevFastAPI"

# Imports principais para facilitar o uso
try:
    from . import setup_rag
except ImportError:
    # Imports opcionais para evitar erros durante a reorganização
    pass

__all__ = [
    "setup_rag"
]