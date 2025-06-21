#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simplificado para reorganização da estrutura RAG_INFRA
"""

import os
import shutil
from pathlib import Path
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('reorganization.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

def create_backup(base_path):
    """Cria backup da estrutura atual"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = base_path.parent / f'rag_infra_backup_{timestamp}'
    
    logger.info(f"Criando backup em: {backup_dir}")
    shutil.copytree(base_path, backup_dir, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    logger.info(f"Backup criado com sucesso: {backup_dir}")
    return backup_dir

def create_temp_structure(base_path):
    """Cria estrutura de diretórios temporários"""
    temp_dirs = [
        'temp',
        'temp/cache',
        'temp/cache/embeddings',
        'temp/cache/indexes', 
        'temp/cache/queries',
        'temp/logs',
        'temp/logs/application',
        'temp/logs/performance',
        'temp/logs/errors',
        'temp/processing'
    ]
    
    for dir_path in temp_dirs:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Criado diretório: {full_path}")

def move_cache_and_logs(base_path):
    """Move arquivos de cache e logs para temp/"""
    # Mover cache existente
    old_cache = base_path / 'cache'
    if old_cache.exists():
        new_cache = base_path / 'temp' / 'cache' / 'legacy'
        new_cache.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_cache), str(new_cache))
        logger.info(f"Cache movido: {old_cache} -> {new_cache}")
    
    # Mover logs existentes
    old_logs = base_path / 'logs'
    if old_logs.exists():
        new_logs = base_path / 'temp' / 'logs' / 'legacy'
        new_logs.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_logs), str(new_logs))
        logger.info(f"Logs movidos: {old_logs} -> {new_logs}")
    
    # Mover arquivos .log da raiz
    for log_file in base_path.glob('*.log'):
        dest = base_path / 'temp' / 'logs' / 'application' / log_file.name
        shutil.move(str(log_file), str(dest))
        logger.info(f"Log movido: {log_file} -> {dest}")

def create_gitignore(base_path):
    """Cria/atualiza .gitignore"""
    gitignore_content = """
# Arquivos temporários e cache
temp/
*.log
*.tmp
*.cache

# Cache Python
__pycache__/
*.py[cod]
*$py.class

# Arquivos de sistema
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Dados sensíveis
*.key
*.pem
*.env
"""
    
    gitignore_path = base_path / '.gitignore'
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write(gitignore_content.strip())
    logger.info(f"Gitignore atualizado: {gitignore_path}")

def create_temp_readme(base_path):
    """Cria README para diretório temp"""
    readme_content = """
# Arquivos Temporários - RAG Infrastructure

**ATENCAO**: Este diretório é ignorado pelo Git.

Contém arquivos temporários, cache e logs que podem ser regenerados.

## Estrutura

- `cache/`: Cache unificado do sistema
- `logs/`: Logs centralizados  
- `processing/`: Arquivos de processamento temporário

## Limpeza

Este diretório pode ser limpo periodicamente sem perda de dados importantes.
"""
    
    readme_path = base_path / 'temp' / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content.strip())
    logger.info(f"README criado: {readme_path}")

def main():
    """Função principal"""
    base_path = Path.cwd()
    
    logger.info("=== INICIANDO REORGANIZAÇÃO ESTRUTURAL RAG_INFRA ===")
    logger.info(f"Diretório base: {base_path}")
    
    try:
        # 1. Criar backup
        backup_dir = create_backup(base_path)
        
        # 2. Criar estrutura temp/
        create_temp_structure(base_path)
        
        # 3. Mover cache e logs
        move_cache_and_logs(base_path)
        
        # 4. Criar .gitignore
        create_gitignore(base_path)
        
        # 5. Criar README
        create_temp_readme(base_path)
        
        logger.info("=== REORGANIZAÇÃO CONCLUÍDA COM SUCESSO ===")
        logger.info(f"Backup disponível em: {backup_dir}")
        
        return True
        
    except Exception as e:
        logger.error(f"Erro durante reorganização: {e}")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)