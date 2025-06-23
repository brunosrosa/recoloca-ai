#!/usr/bin/env python3
"""
Script para corrigir automaticamente os caminhos de importação após a reorganização da estrutura.
Este script atualiza todas as referências de 'core_logic' para 'src/core/core_logic'.

Autor: Arquiteto de TI Mentor Sênior
Data: 2025-01-20
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent
BACKUP_SUFFIX = ".backup_before_import_fix"

# Padrões de busca e substituição
PATTERNS = [
    # sys.path.insert com core_logic
    (r'sys\.path\.insert\(0, str\(.*?["\']core_logic["\']\)\)', 
     'sys.path.insert(0, str(project_root / "src" / "core" / "core_logic"))'),
    
    # sys.path.append com core_logic
    (r'sys\.path\.append\(.*?["\']core_logic["\'].*?\)', 
     'sys.path.append(str(project_root / "src" / "core" / "core_logic"))'),
    
    # Importações diretas de core_logic
    (r'from core_logic\.(\w+)', r'from rag_infra.src.core.core_logic.\1'),
    (r'import core_logic\.(\w+)', r'import rag_infra.src.core.core_logic.\1'),
    
    # Importações relativas incorretas
    (r'from \.core_logic\.(\w+)', r'from rag_infra.src.core.core_logic.\1'),
    (r'from \.\.\.core_logic\.(\w+)', r'from rag_infra.src.core.core_logic.\1'),
    (r'from \.\.\.\.\.core_logic\.(\w+)', r'from rag_infra.src.core.core_logic.\1'),
    
    # Importações rag_infra.core_logic (estrutura antiga)
    (r'from rag_infra\.core_logic\.(\w+)', r'from rag_infra.src.core.core_logic.\1'),
    (r'import rag_infra\.core_logic\.(\w+)', r'import rag_infra.src.core.core_logic.\1'),
    
    # Caminhos de diretório core_logic
    (r'["\']core_logic["\']', '"src/core/core_logic"'),
    
    # Caminhos específicos para src.core.core_logic
    (r'from src\.core\.core_logic\.(\w+)', r'from rag_infra.src.core.core_logic.\1'),
    (r'import src\.core\.core_logic\.(\w+)', r'import rag_infra.src.core.core_logic.\1'),
]

# Arquivos a serem ignorados (backups, etc.)
IGNORE_PATTERNS = [
    '*backup*',
    '*.backup',
    '*_backup_*',
    '.git/*',
    '__pycache__/*',
    '*.pyc',
    'fix_import_paths.py'  # Este próprio script
]

def should_ignore_file(file_path: Path) -> bool:
    """Verifica se o arquivo deve ser ignorado."""
    file_str = str(file_path)
    
    for pattern in IGNORE_PATTERNS:
        if pattern.replace('*', '') in file_str:
            return True
    
    return False

def backup_file(file_path: Path) -> Path:
    """Cria backup do arquivo antes da modificação."""
    backup_path = file_path.with_suffix(file_path.suffix + BACKUP_SUFFIX)
    backup_path.write_text(file_path.read_text(encoding='utf-8'), encoding='utf-8')
    return backup_path

def fix_imports_in_file(file_path: Path) -> Tuple[bool, List[str]]:
    """Corrige as importações em um arquivo específico."""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        changes = []
        
        # Adiciona import do project_root se necessário
        needs_project_root = False
        
        for pattern, replacement in PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                if 'project_root' in replacement and 'project_root =' not in content:
                    needs_project_root = True
                
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    changes.append(f"Padrão '{pattern}' -> '{replacement}'")
                    content = new_content
        
        # Adiciona definição do project_root se necessário
        if needs_project_root and 'project_root =' not in content:
            # Procura por imports existentes para inserir após eles
            import_lines = []
            lines = content.split('\n')
            insert_index = 0
            
            for i, line in enumerate(lines):
                if line.strip().startswith(('import ', 'from ')):
                    insert_index = i + 1
                elif line.strip().startswith('sys.path'):
                    insert_index = i
                    break
            
            project_root_def = "\nproject_root = Path(__file__).parent.parent\n"
            if 'from pathlib import Path' not in content:
                project_root_def = "from pathlib import Path\n" + project_root_def
            
            lines.insert(insert_index, project_root_def)
            content = '\n'.join(lines)
            changes.append("Adicionada definição de project_root")
        
        if content != original_content:
            # Cria backup antes de modificar
            backup_file(file_path)
            
            # Salva o arquivo modificado
            file_path.write_text(content, encoding='utf-8')
            return True, changes
        
        return False, []
        
    except Exception as e:
        print(f"[ERROR] Erro ao processar {file_path}: {e}")
        return False, []

def find_files_to_fix() -> List[Path]:
    """Encontra todos os arquivos Python que precisam ser corrigidos."""
    files_to_fix = []
    
    # Busca em todo o projeto
    for file_path in PROJECT_ROOT.rglob('*.py'):
        if should_ignore_file(file_path):
            continue
            
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Verifica se o arquivo contém padrões que precisam ser corrigidos
            for pattern, _ in PATTERNS:
                if re.search(pattern, content):
                    files_to_fix.append(file_path)
                    break
                    
        except Exception as e:
            print(f"[WARNING]  Erro ao ler {file_path}: {e}")
    
    return files_to_fix

def main():
    """Função principal."""
    print("[EMOJI] Iniciando correção de caminhos de importação...")
    print(f"[EMOJI] Diretório do projeto: {PROJECT_ROOT}")
    print()
    
    # Encontra arquivos que precisam ser corrigidos
    files_to_fix = find_files_to_fix()
    
    if not files_to_fix:
        print("[OK] Nenhum arquivo precisa ser corrigido!")
        return
    
    print(f"[EMOJI] Encontrados {len(files_to_fix)} arquivos para corrigir:")
    for file_path in files_to_fix:
        rel_path = file_path.relative_to(PROJECT_ROOT)
        print(f"   - {rel_path}")
    print()
    
    # Confirma antes de prosseguir
    response = input("🤔 Deseja prosseguir com as correções? (s/N): ")
    if response.lower() not in ['s', 'sim', 'y', 'yes']:
        print("[ERROR] Operação cancelada.")
        return
    
    # Processa cada arquivo
    fixed_count = 0
    total_changes = 0
    
    for file_path in files_to_fix:
        rel_path = file_path.relative_to(PROJECT_ROOT)
        print(f"[EMOJI] Processando: {rel_path}")
        
        was_fixed, changes = fix_imports_in_file(file_path)
        
        if was_fixed:
            fixed_count += 1
            total_changes += len(changes)
            print(f"   [OK] Corrigido ({len(changes)} alterações)")
            for change in changes:
                print(f"      - {change}")
        else:
            print(f"   ⏭[EMOJI]  Nenhuma alteração necessária")
    
    print()
    print(f"[EMOJI] Correção concluída!")
    print(f"   [EMOJI] Arquivos corrigidos: {fixed_count}/{len(files_to_fix)}")
    print(f"   [EMOJI] Total de alterações: {total_changes}")
    print()
    print(f"[SAVE] Backups criados com sufixo: {BACKUP_SUFFIX}")
    print("[WARNING]  Teste o sistema após as correções!")

if __name__ == "__main__":
    main()