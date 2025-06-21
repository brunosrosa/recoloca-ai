# -*- coding: utf-8 -*-
"""
Utilitários PyTorch para o Sistema RAG do Recoloca.ai

Este módulo fornece funções utilitárias seguras para verificações de CUDA
e operações de cleanup, evitando AttributeError durante o shutdown do Python.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

def is_cuda_available() -> bool:
    """
    Verifica se CUDA está disponível de forma segura.
    
    Returns:
        bool: True se CUDA estiver disponível, False caso contrário
    """
    try:
        import torch
        return hasattr(torch, 'cuda') and torch.cuda is not None and torch.cuda.is_available()
    except (ImportError, AttributeError, RuntimeError):
        return False

def safe_cuda_empty_cache() -> None:
    """
    Limpa o cache CUDA de forma segura.
    
    Esta função verifica se torch e CUDA estão disponíveis antes de tentar
    limpar o cache, evitando AttributeError durante cleanup.
    """
    try:
        import torch
        if hasattr(torch, 'cuda') and torch.cuda is not None and torch.cuda.is_available():
            torch.cuda.empty_cache()
            logger.debug("Cache CUDA limpo com sucesso")
    except (ImportError, AttributeError, RuntimeError) as e:
        logger.debug(f"Não foi possível limpar cache CUDA: {e}")
        pass

def get_device_info() -> dict:
    """
    Obtém informações sobre dispositivos disponíveis de forma segura.
    
    Returns:
        dict: Informações sobre dispositivos disponíveis
    """
    info = {
        "cuda_available": False,
        "device_count": 0,
        "current_device": None,
        "device_name": None
    }
    
    try:
        import torch
        if hasattr(torch, 'cuda') and torch.cuda is not None:
            info["cuda_available"] = torch.cuda.is_available()
            if info["cuda_available"]:
                info["device_count"] = torch.cuda.device_count()
                info["current_device"] = torch.cuda.current_device()
                info["device_name"] = torch.cuda.get_device_name()
    except (ImportError, AttributeError, RuntimeError) as e:
        logger.debug(f"Erro ao obter informações do dispositivo: {e}")
    
    return info

def safe_tensor_cleanup(tensor_attr_name: str, obj: object) -> None:
    """
    Remove um tensor de forma segura de um objeto.
    
    Args:
        tensor_attr_name: Nome do atributo tensor a ser removido
        obj: Objeto que contém o tensor
    """
    try:
        if hasattr(obj, tensor_attr_name):
            tensor = getattr(obj, tensor_attr_name)
            if tensor is not None:
                delattr(obj, tensor_attr_name)
                del tensor
                logger.debug(f"Tensor {tensor_attr_name} removido com sucesso")
    except (AttributeError, RuntimeError) as e:
        logger.debug(f"Erro ao remover tensor {tensor_attr_name}: {e}")
        pass

class SafePyTorchCleanup:
    """
    Context manager para cleanup seguro de recursos PyTorch.
    
    Exemplo de uso:
        with SafePyTorchCleanup():
            # código que usa PyTorch
            pass
    """
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        safe_cuda_empty_cache()
        return False

# Função de conveniência para verificação rápida
def get_optimal_device(force_cpu: bool = False) -> str:
    """
    Retorna o dispositivo ótimo para uso (cuda ou cpu).
    
    Args:
        force_cpu: Se True, força o uso de CPU
    
    Returns:
        str: 'cuda' ou 'cpu'
    """
    if force_cpu:
        return 'cpu'
    
    return 'cuda' if is_cuda_available() else 'cpu'