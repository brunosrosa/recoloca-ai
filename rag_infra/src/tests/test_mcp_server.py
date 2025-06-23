#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste do MCP Server
"""

import sys
import logging
from pathlib import Path

# Adicionar o diretório pai (rag_infra) ao path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def test_mcp_server_import():
    """Testa se o MCP Server pode ser importado"""
    try:
        logger.info("=== Teste Import MCP Server ===")
        
        # Adicionar core_logic ao path
        core_logic_path = project_root / "src/core/core_logic"
        sys.path.insert(0, str(core_logic_path))
        
        # Tentar importar o servidor MCP
        logger.info("[EMOJI] Importando MCP Server...")
        from mcp_server import server, server_state
        logger.info("[OK] MCP Server importado com sucesso")
        
        # Verificar estado inicial
        logger.info(f"Estado inicial: {server_state}")
        
        # Verificar se o servidor tem as funções necessárias
        logger.info("[EMOJI] Verificando funcionalidades do MCP Server...")
        
        # Verificar se as funções principais existem
        has_list_tools = hasattr(server, 'list_tools')
        has_call_tool = hasattr(server, 'call_tool')
        
        logger.info(f"  - list_tools: {has_list_tools}")
        logger.info(f"  - call_tool: {has_call_tool}")
        logger.info(f"  - server_state: {server_state}")
        
        if has_list_tools and has_call_tool:
            logger.info("[OK] MCP Server funcionando corretamente")
            return True
        else:
            logger.error("[ERROR] MCP Server sem funcionalidades necessárias")
            return False
            
    except Exception as e:
        logger.error(f"[ERROR] Erro no teste MCP Server: {str(e)}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = test_mcp_server_import()
    
    if success:
        print("\n=== Resultado Final: SUCESSO ===")
        print("[EMOJI] MCP Server está funcionando corretamente!")
    else:
        print("\n=== Resultado Final: FALHA ===")
        print("[ERROR] Problemas detectados no MCP Server")
        sys.exit(1)