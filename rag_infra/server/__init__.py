# -*- coding: utf-8 -*-
"""
Módulo de Servidor - RAG Infra

Este módulo contém componentes de servidor e integração do sistema RAG.

Módulos disponíveis:
- mcp_server: Servidor MCP para integração com Trae IDE

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

__version__ = "1.0.0"
__author__ = "@AgenteM_DevFastAPI"

# Imports principais para facilitar o uso
try:
    from . import mcp_server
except ImportError:
    # Imports opcionais para evitar erros durante a reorganização
    pass

__all__ = [
    "mcp_server"
]