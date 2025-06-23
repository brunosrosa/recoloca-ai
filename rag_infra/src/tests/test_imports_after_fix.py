#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar imports relativos após correção de caminhos

Este script verifica se todos os módulos do sistema RAG podem ser
importados corretamente após a renomeação da pasta e correção dos caminhos.

Autor: @AgenteM_DevFastAPI
Data: Junho 2025
"""

import sys
import logging
import traceback
from pathlib import Path
from typing import List, Dict, Any

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class ImportTester:
    """Classe para testar imports do sistema RAG"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.rag_root = project_root / "rag_infra"
        self.core_logic_path = self.rag_root / "core_logic"
        self.test_results = []
        
    def setup_paths(self) -> bool:
        """Configura os caminhos do Python para importação"""
        try:
            # Adicionar caminhos necessários
            paths_to_add = [
                str(self.project_root),
                str(self.rag_root),
                str(self.core_logic_path)
            ]
            
            for path in paths_to_add:
                if path not in sys.path:
                    sys.path.insert(0, path)
                    logger.info(f"[OK] Path adicionado: {path}")
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro ao configurar paths: {e}")
            return False
    
    def test_import(self, module_name: str, description: str = "") -> Dict[str, Any]:
        """Testa a importação de um módulo específico"""
        result = {
            "module": module_name,
            "description": description,
            "success": False,
            "error": None,
            "details": None
        }
        
        try:
            logger.info(f"🧪 Testando import: {module_name}")
            
            # Tentar importar o módulo
            if '.' in module_name:
                # Import com from
                parts = module_name.split('.')
                module_path = '.'.join(parts[:-1])
                item_name = parts[-1]
                exec(f"from {module_path} import {item_name}")
            else:
                # Import direto
                exec(f"import {module_name}")
            
            result["success"] = True
            result["details"] = "Import realizado com sucesso"
            logger.info(f"[OK] {module_name} importado com sucesso")
            
        except ImportError as e:
            result["error"] = f"ImportError: {str(e)}"
            result["details"] = traceback.format_exc()
            logger.error(f"[ERROR] Erro de import em {module_name}: {e}")
            
        except Exception as e:
            result["error"] = f"Erro geral: {str(e)}"
            result["details"] = traceback.format_exc()
            logger.error(f"[ERROR] Erro geral em {module_name}: {e}")
        
        self.test_results.append(result)
        return result
    
    def test_core_modules(self) -> List[Dict[str, Any]]:
        """Testa imports dos módulos principais do sistema RAG"""
        logger.info("[SEARCH] Testando módulos principais do sistema RAG...")
        
        # Lista de módulos para testar
        modules_to_test = [
            ("constants", "Constantes do sistema RAG"),
            ("embedding_model", "Modelo de embeddings"),
            ("rag_indexer", "Indexador RAG"),
            ("rag_retriever", "Retriever RAG"),
            ("faiss_to_pytorch_converter", "Conversor FAISS para PyTorch"),
            ("pytorch_gpu_retriever", "Retriever GPU PyTorch"),
            ("rag_retriever.get_retriever", "Função get_retriever"),
            ("rag_retriever.initialize_retriever", "Função initialize_retriever")
        ]
        
        results = []
        for module_name, description in modules_to_test:
            result = self.test_import(module_name, description)
            results.append(result)
        
        return results
    
    def test_rag_system_initialization(self) -> Dict[str, Any]:
        """Testa a inicialização completa do sistema RAG"""
        logger.info("[START] Testando inicialização completa do sistema RAG...")
        
        result = {
            "test": "rag_system_initialization",
            "success": False,
            "error": None,
            "details": None
        }
        
        try:
            # Importar e inicializar o retriever
            from rag_retriever import get_retriever, initialize_retriever
            
            logger.info("[EMOJI] Tentando inicializar retriever...")
            retriever = get_retriever()
            
            if retriever is not None:
                result["success"] = True
                result["details"] = "Sistema RAG inicializado com sucesso"
                logger.info("[OK] Sistema RAG inicializado com sucesso")
            else:
                result["error"] = "Retriever retornou None"
                result["details"] = "get_retriever() retornou None"
                logger.warning("[WARNING] Retriever retornou None")
                
        except Exception as e:
            result["error"] = str(e)
            result["details"] = traceback.format_exc()
            logger.error(f"[ERROR] Erro na inicialização do sistema RAG: {e}")
        
        self.test_results.append(result)
        return result
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Executa todos os testes de import"""
        logger.info("🧪 Iniciando testes de import após correção de caminhos...")
        
        # Configurar paths
        if not self.setup_paths():
            return {
                "success": False,
                "error": "Falha ao configurar paths",
                "results": []
            }
        
        # Testar módulos principais
        core_results = self.test_core_modules()
        
        # Testar inicialização do sistema
        init_result = self.test_rag_system_initialization()
        
        # Calcular estatísticas
        total_tests = len(self.test_results)
        successful_tests = sum(1 for r in self.test_results if r.get("success", False))
        success_rate = successful_tests / total_tests if total_tests > 0 else 0
        
        # Relatório final
        report = {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": total_tests - successful_tests,
            "success_rate": success_rate,
            "all_tests_passed": success_rate == 1.0,
            "results": self.test_results
        }
        
        return report

def main():
    """Função principal"""
    # Determinar diretório do projeto
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("🧪 Teste de Imports - Sistema RAG Recoloca.AI")
    print("=" * 50)
    print(f"[EMOJI] Diretório do projeto: {project_root}")
    print()
    
    # Executar testes
    tester = ImportTester(project_root)
    report = tester.run_all_tests()
    
    # Exibir relatório
    print()
    print("[EMOJI] RELATÓRIO DE TESTES")
    print("=" * 30)
    print(f"🧪 Total de testes: {report['total_tests']}")
    print(f"[OK] Testes bem-sucedidos: {report['successful_tests']}")
    print(f"[ERROR] Testes falharam: {report['failed_tests']}")
    print(f"[EMOJI] Taxa de sucesso: {report['success_rate']:.1%}")
    
    if report['all_tests_passed']:
        print("\n[EMOJI] TODOS OS TESTES PASSARAM!")
        print("[OK] Sistema RAG está funcionando corretamente")
    else:
        print("\n[WARNING] ALGUNS TESTES FALHARAM")
        print("\n[ERROR] Testes que falharam:")
        for result in report['results']:
            if not result.get('success', False):
                module = result.get('module', result.get('test', 'Unknown'))
                error = result.get('error', 'Erro desconhecido')
                print(f"  • {module}: {error}")
    
    # Salvar relatório
    import json
    report_file = project_root / "import_test_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n[SAVE] Relatório detalhado salvo em: {report_file}")
    
    if report['all_tests_passed']:
        print("\n[EMOJI] PRÓXIMOS PASSOS:")
        print("1. [OK] Imports funcionando corretamente")
        print("2. [START] Sistema RAG pronto para uso")
        print("3. 🧪 Executar testes funcionais")
        print("4. [EMOJI] Continuar desenvolvimento")
    else:
        print("\n[EMOJI] AÇÕES NECESSÁRIAS:")
        print("1. [SEARCH] Verificar erros de import listados acima")
        print("2. [EMOJI] Instalar dependências faltantes")
        print("3. [EMOJI] Corrigir caminhos ou configurações")
        print("4. 🧪 Executar testes novamente")
    
    return report['all_tests_passed']

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)