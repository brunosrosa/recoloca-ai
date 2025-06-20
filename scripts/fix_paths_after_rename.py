#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir caminhos após renomeação da pasta do projeto

Este script atualiza todos os caminhos hardcoded que referenciam o nome antigo
da pasta do projeto (💼 Recoloca.AI) para o novo nome (💼 Recoloca.AI).

Autor: @AgenteM_DevFastAPI
Data: Junho 2025
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Any

# Configurações
OLD_PATH_PATTERN = r"🧑🏻‍💼 Recoloca\.AI"
NEW_PATH_NAME = "💼 Recoloca.AI"

class PathFixer:
    """Classe para corrigir caminhos em arquivos após renomeação"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.files_updated = []
        self.errors = []
        
    def fix_json_file(self, file_path: Path) -> bool:
        """Corrige caminhos em arquivos JSON"""
        try:
            print(f"📝 Processando arquivo JSON: {file_path.name}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Substituir padrões de caminho
            original_content = content
            content = re.sub(OLD_PATH_PATTERN, NEW_PATH_NAME, content)
            
            if content != original_content:
                # Validar JSON antes de salvar
                try:
                    json.loads(content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.files_updated.append(str(file_path))
                    print(f"✅ Arquivo atualizado: {file_path.name}")
                    return True
                    
                except json.JSONDecodeError as e:
                    self.errors.append(f"Erro JSON em {file_path}: {e}")
                    print(f"❌ Erro de JSON em {file_path.name}: {e}")
                    return False
            else:
                print(f"ℹ️  Nenhuma alteração necessária em: {file_path.name}")
                return True
                
        except Exception as e:
            self.errors.append(f"Erro ao processar {file_path}: {e}")
            print(f"❌ Erro ao processar {file_path.name}: {e}")
            return False
    
    def fix_python_file(self, file_path: Path) -> bool:
        """Corrige caminhos em arquivos Python"""
        try:
            print(f"🐍 Processando arquivo Python: {file_path.name}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Substituir padrões de caminho
            original_content = content
            content = re.sub(OLD_PATH_PATTERN, NEW_PATH_NAME, content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.files_updated.append(str(file_path))
                print(f"✅ Arquivo atualizado: {file_path.name}")
                return True
            else:
                print(f"ℹ️  Nenhuma alteração necessária em: {file_path.name}")
                return True
                
        except Exception as e:
            self.errors.append(f"Erro ao processar {file_path}: {e}")
            print(f"❌ Erro ao processar {file_path.name}: {e}")
            return False
    
    def fix_text_file(self, file_path: Path) -> bool:
        """Corrige caminhos em arquivos de texto"""
        try:
            print(f"📄 Processando arquivo de texto: {file_path.name}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Substituir padrões de caminho
            original_content = content
            content = re.sub(OLD_PATH_PATTERN, NEW_PATH_NAME, content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.files_updated.append(str(file_path))
                print(f"✅ Arquivo atualizado: {file_path.name}")
                return True
            else:
                print(f"ℹ️  Nenhuma alteração necessária em: {file_path.name}")
                return True
                
        except Exception as e:
            self.errors.append(f"Erro ao processar {file_path}: {e}")
            print(f"❌ Erro ao processar {file_path.name}: {e}")
            return False
    
    def find_files_to_fix(self) -> List[Path]:
        """Encontra todos os arquivos que podem conter caminhos para corrigir"""
        files_to_check = []
        
        # Padrões de arquivos para verificar
        patterns = [
            "**/*.json",
            "**/*.py",
            "**/*.txt",
            "**/*.md",
            "**/*.log"
        ]
        
        for pattern in patterns:
            files_to_check.extend(self.project_root.glob(pattern))
        
        # Filtrar arquivos que podem conter caminhos
        relevant_files = []
        for file_path in files_to_check:
            # Pular arquivos em diretórios que não devem ser modificados
            if any(part.startswith('.') for part in file_path.parts):
                continue
            if 'node_modules' in file_path.parts:
                continue
            if '__pycache__' in file_path.parts:
                continue
                
            relevant_files.append(file_path)
        
        return relevant_files
    
    def run_fixes(self) -> Dict[str, Any]:
        """Executa todas as correções necessárias"""
        print("🔧 Iniciando correção de caminhos após renomeação...")
        print(f"📁 Diretório do projeto: {self.project_root}")
        print(f"🔄 Substituindo: {OLD_PATH_PATTERN} → {NEW_PATH_NAME}")
        print()
        
        files_to_fix = self.find_files_to_fix()
        print(f"📋 Encontrados {len(files_to_fix)} arquivos para verificar")
        print()
        
        success_count = 0
        for file_path in files_to_fix:
            try:
                if file_path.suffix == '.json':
                    if self.fix_json_file(file_path):
                        success_count += 1
                elif file_path.suffix == '.py':
                    if self.fix_python_file(file_path):
                        success_count += 1
                else:
                    if self.fix_text_file(file_path):
                        success_count += 1
            except Exception as e:
                self.errors.append(f"Erro geral em {file_path}: {e}")
                print(f"❌ Erro geral em {file_path.name}: {e}")
        
        # Relatório final
        report = {
            "total_files_checked": len(files_to_fix),
            "files_updated": len(self.files_updated),
            "files_with_errors": len(self.errors),
            "success_rate": success_count / len(files_to_fix) if files_to_fix else 0,
            "updated_files": self.files_updated,
            "errors": self.errors
        }
        
        return report

def main():
    """Função principal"""
    # Determinar diretório do projeto
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("🚀 Script de Correção de Caminhos - Recoloca.AI")
    print("=" * 50)
    
    # Executar correções
    fixer = PathFixer(project_root)
    report = fixer.run_fixes()
    
    # Exibir relatório
    print()
    print("📊 RELATÓRIO FINAL")
    print("=" * 30)
    print(f"📁 Arquivos verificados: {report['total_files_checked']}")
    print(f"✅ Arquivos atualizados: {report['files_updated']}")
    print(f"❌ Arquivos com erro: {report['files_with_errors']}")
    print(f"📈 Taxa de sucesso: {report['success_rate']:.1%}")
    
    if report['updated_files']:
        print("\n📝 Arquivos atualizados:")
        for file_path in report['updated_files']:
            print(f"  • {Path(file_path).name}")
    
    if report['errors']:
        print("\n❌ Erros encontrados:")
        for error in report['errors']:
            print(f"  • {error}")
    
    # Salvar relatório
    report_file = project_root / "path_fix_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Relatório salvo em: {report_file}")
    
    if report['files_updated'] > 0:
        print("\n🎯 PRÓXIMOS PASSOS:")
        print("1. ✅ Caminhos atualizados com sucesso")
        print("2. 🔄 Recriar ambiente virtual se necessário")
        print("3. 🧪 Testar imports relativos")
        print("4. 🚀 Executar testes do sistema RAG")
    
    return report['files_with_errors'] == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)