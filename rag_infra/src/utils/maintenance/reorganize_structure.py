#!/usr/bin/env python3
"""
Script de Reorganização Estrutural do RAG_INFRA

Este script implementa a migração segura da estrutura atual do rag_infra
para a nova organização "future-proof" proposta.

Autor: @AgenteM_ArquitetoTI
Data: Junho 2025
Versão: 1.0

Uso:
    python scripts/reorganize_structure.py [--dry-run] [--backup-dir PATH]
"""

import os
import shutil
import argparse
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reorganization.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class RAGInfraReorganizer:
    """Classe responsável pela reorganização estrutural do rag_infra."""
    
    def __init__(self, base_path: str, backup_dir: str = None, dry_run: bool = False):
        self.base_path = Path(base_path)
        self.backup_dir = Path(backup_dir) if backup_dir else self.base_path.parent / f"rag_infra_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.dry_run = dry_run
        self.migration_log = []
        
    def create_new_structure(self) -> Dict[str, str]:
        """Cria a nova estrutura de diretórios."""
        new_structure = {
            # Código fonte
            'src': 'Código fonte principal',
            'src/core': 'Lógica central do RAG',
            'src/core/indexer': 'Módulos de indexação',
            'src/core/retriever': 'Módulos de recuperação',
            'src/core/embeddings': 'Gestão de embeddings',
            'src/core/mcp_server': 'Servidor MCP',
            'src/utils': 'Utilitários organizados',
            'src/utils/demos': 'Scripts de demonstração',
            'src/utils/optimization': 'Ferramentas de otimização',
            'src/utils/maintenance': 'Scripts de manutenção',
            'src/tests': 'Testes organizados',
            'src/tests/unit': 'Testes unitários',
            'src/tests/integration': 'Testes de integração',
            'src/tests/performance': 'Testes de performance',
            
            # Configurações
            'config': 'Configurações centralizadas',
            'config/environments': 'Configs por ambiente',
            'config/models': 'Configurações de modelos',
            'config/logging': 'Configurações de log',
            
            # Dados persistentes
            'data': 'Dados persistentes',
            'data/indexes': 'Índices FAISS e PyTorch',
            'data/indexes/faiss': 'Índices FAISS',
            'data/indexes/pytorch': 'Índices PyTorch',
            'data/source_documents': 'Documentação fonte',
            'data/source_documents/arquitetura': 'Documentos de arquitetura',
            'data/source_documents/requisitos': 'Documentos de requisitos',
            'data/source_documents/guias': 'Guias e manuais',
            'data/source_documents/kanban': 'Documentos de kanban',
            'data/source_documents/agentes': 'Documentos de agentes',
            'data/source_documents/tech_stack': 'Documentos de tech stack',
            'data/embeddings': 'Embeddings persistentes',
            
            # Arquivos temporários
            'temp': 'Arquivos temporários',
            'temp/cache': 'Cache unificado',
            'temp/cache/embeddings': 'Cache de embeddings',
            'temp/cache/indexes': 'Cache de índices',
            'temp/cache/queries': 'Cache de consultas',
            'temp/logs': 'Logs centralizados',
            'temp/logs/application': 'Logs da aplicação',
            'temp/logs/performance': 'Logs de performance',
            'temp/logs/errors': 'Logs de erros',
            'temp/processing': 'Arquivos de processamento temporário',
            
            # Documentação
            'docs': 'Documentação específica do RAG',
            'docs/api': 'Documentação da API',
            'docs/architecture': 'Diagramas e decisões arquiteturais',
            'docs/deployment': 'Guias de deploy',
            'docs/troubleshooting': 'Guias de resolução de problemas',
            
            # Scripts
            'scripts': 'Scripts de automação',
            'scripts/setup': 'Scripts de configuração inicial',
            'scripts/deployment': 'Scripts de deploy',
            'scripts/maintenance': 'Scripts de manutenção',
            'scripts/monitoring': 'Scripts de monitoramento',
            
            # Relatórios
            'reports': 'Relatórios e métricas',
            'reports/performance': 'Relatórios de performance',
            'reports/usage': 'Relatórios de uso',
            'reports/quality': 'Relatórios de qualidade'
        }
        
        logger.info("Criando nova estrutura de diretórios...")
        for dir_path, description in new_structure.items():
            full_path = self.base_path / dir_path
            if not self.dry_run:
                full_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Criado: {full_path}")
            else:
                logger.info(f"[DRY-RUN] Criaria: {full_path}")
            
            self.migration_log.append({
                'action': 'create_directory',
                'path': str(full_path),
                'description': description,
                'timestamp': datetime.now().isoformat()
            })
        
        return new_structure
    
    def create_backup(self) -> bool:
        """Cria backup completo da estrutura atual."""
        try:
            logger.info(f"Criando backup em: {self.backup_dir}")
            if not self.dry_run:
                shutil.copytree(self.base_path, self.backup_dir, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
                logger.info("Backup criado com sucesso")
            else:
                logger.info(f"[DRY-RUN] Criaria backup em: {self.backup_dir}")
            
            self.migration_log.append({
                'action': 'create_backup',
                'source': str(self.base_path),
                'destination': str(self.backup_dir),
                'timestamp': datetime.now().isoformat()
            })
            return True
        except Exception as e:
            logger.error(f"Erro ao criar backup: {e}")
            return False
    
    def get_migration_mapping(self) -> Dict[str, str]:
        """Define o mapeamento de migração de arquivos e pastas."""
        return {
            # Código fonte
            'core_logic/': 'src/core/',
            'utils/': 'src/utils/',
            'tests/': 'src/tests/',
            
            # Configurações
            'config/': 'config/',
            
            # Dados
            'data_index/': 'data/indexes/',
            'source_documents/': 'data/source_documents/',
            
            # Relatórios
            'results_and_reports/': 'reports/',
            
            # Arquivos na raiz que devem ser movidos
            '*.log': 'temp/logs/application/',
            'cache/': 'temp/cache/',
            'logs/': 'temp/logs/',
            
            # Arquivos que permanecem na raiz
            'README.md': 'README.md',
            'requirements.txt': 'requirements.txt',
            '.gitignore': '.gitignore'
        }
    
    def migrate_files(self) -> bool:
        """Executa a migração de arquivos baseada no mapeamento."""
        mapping = self.get_migration_mapping()
        success = True
        
        logger.info("Iniciando migração de arquivos...")
        
        for source_pattern, destination in mapping.items():
            try:
                source_path = self.base_path / source_pattern
                dest_path = self.base_path / destination
                
                # Handle wildcard patterns
                if '*' in source_pattern:
                    import glob
                    pattern = str(self.base_path / source_pattern)
                    matching_files = glob.glob(pattern)
                    
                    for file_path in matching_files:
                        file_name = os.path.basename(file_path)
                        final_dest = dest_path / file_name
                        
                        if not self.dry_run:
                            final_dest.parent.mkdir(parents=True, exist_ok=True)
                            shutil.move(file_path, final_dest)
                            logger.info(f"Movido: {file_path} -> {final_dest}")
                        else:
                            logger.info(f"[DRY-RUN] Moveria: {file_path} -> {final_dest}")
                        
                        self.migration_log.append({
                            'action': 'move_file',
                            'source': file_path,
                            'destination': str(final_dest),
                            'timestamp': datetime.now().isoformat()
                        })
                
                # Handle directory moves
                elif source_path.exists():
                    if not self.dry_run:
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(source_path), str(dest_path))
                        logger.info(f"Movido: {source_path} -> {dest_path}")
                    else:
                        logger.info(f"[DRY-RUN] Moveria: {source_path} -> {dest_path}")
                    
                    self.migration_log.append({
                        'action': 'move_directory',
                        'source': str(source_path),
                        'destination': str(dest_path),
                        'timestamp': datetime.now().isoformat()
                    })
                
            except Exception as e:
                logger.error(f"Erro ao migrar {source_pattern}: {e}")
                success = False
        
        return success
    
    def create_gitignore(self) -> None:
        """Cria/atualiza o .gitignore com as novas regras."""
        gitignore_content = """
# Arquivos temporários e cache
temp/
*.log
*.tmp
*.cache

# Arquivos de ambiente
.env
.env.local
.env.*.local

# Cache Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribuição / empacotamento
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# Ambientes virtuais
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Arquivos específicos do sistema
.DS_Store
Thumbs.db

# Dados sensíveis
config/secrets/
*.key
*.pem
*.p12

# Modelos e índices grandes (se necessário)
# data/indexes/large_models/
# data/embeddings/large_embeddings/
"""
        
        gitignore_path = self.base_path / '.gitignore'
        
        if not self.dry_run:
            with open(gitignore_path, 'w', encoding='utf-8') as f:
                f.write(gitignore_content)
            logger.info(f"Criado/atualizado: {gitignore_path}")
        else:
            logger.info(f"[DRY-RUN] Criaria/atualizaria: {gitignore_path}")
        
        self.migration_log.append({
            'action': 'create_gitignore',
            'path': str(gitignore_path),
            'timestamp': datetime.now().isoformat()
        })
    
    def create_readme_files(self) -> None:
        """Cria READMEs explicativos para as principais pastas."""
        readme_contents = {
            'src/README.md': """
# Código Fonte - RAG Infrastructure

Este diretório contém todo o código fonte da infraestrutura RAG.

## Estrutura

- `core/`: Lógica central do sistema RAG
- `utils/`: Utilitários e ferramentas auxiliares
- `tests/`: Testes organizados por tipo

## Desenvolvimento

Para contribuir com o código, consulte a documentação em `../docs/`.
""",
            
            'config/README.md': """
# Configurações - RAG Infrastructure

Centralização de todas as configurações do sistema.

## Estrutura

- `environments/`: Configurações por ambiente (dev, staging, prod)
- `models/`: Configurações de modelos de IA
- `logging/`: Configurações de logging

## Segurança

Nunca commite arquivos com credenciais ou chaves de API.
Use variáveis de ambiente para dados sensíveis.
""",
            
            'data/README.md': """
# Dados Persistentes - RAG Infrastructure

Armazenamento de dados importantes e persistentes.

## Estrutura

- `indexes/`: Índices FAISS e PyTorch
- `source_documents/`: Documentação fonte categorizada
- `embeddings/`: Embeddings persistentes

## Backup

Este diretório deve ser incluído em backups regulares.
""",
            
            'temp/README.md': """
# Arquivos Temporários - RAG Infrastructure

**ATENÇÃO**: Este diretório é ignorado pelo Git.

Contém arquivos temporários, cache e logs que podem ser regenerados.

## Estrutura

- `cache/`: Cache unificado do sistema
- `logs/`: Logs centralizados
- `processing/`: Arquivos de processamento temporário

## Limpeza

Este diretório pode ser limpo periodicamente sem perda de dados importantes.
"""
        }
        
        for file_path, content in readme_contents.items():
            full_path = self.base_path / file_path
            
            if not self.dry_run:
                full_path.parent.mkdir(parents=True, exist_ok=True)
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content.strip())
                logger.info(f"Criado: {full_path}")
            else:
                logger.info(f"[DRY-RUN] Criaria: {full_path}")
            
            self.migration_log.append({
                'action': 'create_readme',
                'path': str(full_path),
                'timestamp': datetime.now().isoformat()
            })
    
    def save_migration_log(self) -> None:
        """Salva o log detalhado da migração."""
        log_path = self.base_path / 'reports' / 'migration_log.json'
        
        if not self.dry_run:
            log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'migration_date': datetime.now().isoformat(),
                    'dry_run': self.dry_run,
                    'backup_location': str(self.backup_dir),
                    'actions': self.migration_log
                }, f, indent=2, ensure_ascii=False)
            logger.info(f"Log de migração salvo em: {log_path}")
        else:
            logger.info(f"[DRY-RUN] Salvaria log em: {log_path}")
    
    def run_migration(self) -> bool:
        """Executa a migração completa."""
        logger.info("=== INICIANDO REORGANIZAÇÃO ESTRUTURAL DO RAG_INFRA ===")
        
        # 1. Criar backup
        if not self.create_backup():
            logger.error("Falha ao criar backup. Abortando migração.")
            return False
        
        # 2. Criar nova estrutura
        self.create_new_structure()
        
        # 3. Migrar arquivos
        if not self.migrate_files():
            logger.error("Falha na migração de arquivos. Verifique os logs.")
            return False
        
        # 4. Criar arquivos de configuração
        self.create_gitignore()
        self.create_readme_files()
        
        # 5. Salvar log da migração
        self.save_migration_log()
        
        logger.info("=== REORGANIZAÇÃO CONCLUÍDA COM SUCESSO ===")
        logger.info(f"Backup disponível em: {self.backup_dir}")
        
        return True

def main():
    parser = argparse.ArgumentParser(description='Reorganiza a estrutura do rag_infra')
    parser.add_argument('--dry-run', action='store_true', help='Executa sem fazer mudanças reais')
    parser.add_argument('--backup-dir', type=str, help='Diretório para backup (padrão: auto-gerado)')
    parser.add_argument('--base-path', type=str, default='.', help='Caminho base do rag_infra')
    
    args = parser.parse_args()
    
    # Determinar o caminho base
    if args.base_path == '.':
        # Se executado de dentro do rag_infra
        base_path = Path.cwd()
    else:
        base_path = Path(args.base_path)
    
    # Validar que estamos no diretório correto
    if not (base_path / "src/core/core_logic").exists() and not (base_path / 'rag_infra').exists() and not (base_path / 'src' / 'core' / "src/core/core_logic").exists():
        logger.error("Diretório rag_infra não encontrado. Verifique o caminho.")
        return 1
    
    # Ajustar para o rag_infra se necessário
    if (base_path / 'rag_infra').exists():
        base_path = base_path / 'rag_infra'
    
    reorganizer = RAGInfraReorganizer(
        base_path=str(base_path),
        backup_dir=args.backup_dir,
        dry_run=args.dry_run
    )
    
    if args.dry_run:
        logger.info("=== MODO DRY-RUN ATIVADO - NENHUMA MUDANÇA SERÁ FEITA ===")
    
    success = reorganizer.run_migration()
    return 0 if success else 1

if __name__ == '__main__':
    exit(main())