#!/usr/bin/env python3
"""
Script de Setup do Sistema RAG - Recoloca.ai

Este script automatiza a configuração inicial do sistema RAG, incluindo:
- Verificação de dependências
- Configuração do ambiente
- Indexação inicial dos documentos
- Teste do sistema

Uso:
    python setup_rag.py [--force-cpu] [--skip-indexing] [--verbose]
"""

import os
import sys
import argparse
import logging
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional

# Adicionar o diretório rag_infra ao path
rag_infra_path = Path(__file__).parent
sys.path.insert(0, str(rag_infra_path))
sys.path.insert(0, str(rag_infra_path / "core_logic"))

try:
    from core_logic.constants import (
        RAG_ROOT_DIR, SOURCE_DOCUMENTS_DIR, FAISS_INDEX_DIR, 
        LOGS_DIR, EMBEDDING_MODEL_NAME, USE_GPU
    )
    from core_logic.embedding_model import EmbeddingModelManager
    from core_logic.rag_indexer import RAGIndexer
    from core_logic.rag_retriever import RAGRetriever
except ImportError as e:
    print(f"❌ Erro ao importar módulos RAG: {e}")
    print("Verifique se todos os arquivos estão no local correto.")
    sys.exit(1)

class RAGSetup:
    """Classe para gerenciar o setup do sistema RAG."""
    
    def __init__(self, force_cpu: bool = False, verbose: bool = False):
        self.force_cpu = force_cpu
        self.verbose = verbose
        self.setup_logging()
        
    def setup_logging(self):
        """Configura o sistema de logging."""
        level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler(LOGS_DIR / "setup_rag.log")
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def check_python_version(self) -> bool:
        """Verifica se a versão do Python é compatível."""
        self.logger.info("🐍 Verificando versão do Python...")
        
        if sys.version_info < (3, 8):
            self.logger.error("❌ Python 3.8+ é necessário")
            return False
            
        self.logger.info(f"✅ Python {sys.version.split()[0]} detectado")
        return True
        
    def check_gpu_availability(self) -> Tuple[bool, str]:
        """Verifica disponibilidade de GPU e CUDA."""
        self.logger.info("🔍 Verificando disponibilidade de GPU...")
        
        if self.force_cpu:
            self.logger.info("⚠️ Forçando uso de CPU")
            return False, "CPU forçada pelo usuário"
            
        try:
            import torch
            if torch.cuda.is_available():
                gpu_name = torch.cuda.get_device_name(0)
                gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
                self.logger.info(f"✅ GPU detectada: {gpu_name} ({gpu_memory:.1f}GB)")
                return True, f"{gpu_name} ({gpu_memory:.1f}GB)"
            else:
                self.logger.warning("⚠️ CUDA não disponível, usando CPU")
                return False, "CUDA não disponível"
        except ImportError:
            self.logger.warning("⚠️ PyTorch não instalado, usando CPU")
            return False, "PyTorch não instalado"
            
    def check_dependencies(self) -> List[str]:
        """Verifica se todas as dependências estão instaladas."""
        self.logger.info("📦 Verificando dependências...")
        
        # Mapeamento de pacotes pip para nomes de importação
        required_packages = {
            'torch': 'torch',
            'transformers': 'transformers', 
            'sentence-transformers': 'sentence_transformers',
            'langchain': 'langchain',
            'faiss-cpu': 'faiss',
            'numpy': 'numpy',
            'pandas': 'pandas',
            'pymupdf': 'fitz',
            'python-dotenv': 'dotenv',
            'unstructured': 'unstructured'
        }
        
        missing_packages = []
        
        for package_name, import_name in required_packages.items():
            try:
                __import__(import_name)
                self.logger.debug(f"✅ {package_name} instalado")
            except ImportError:
                missing_packages.append(package_name)
                self.logger.warning(f"❌ {package_name} não encontrado")
                
        if missing_packages:
            self.logger.error(f"❌ Pacotes faltando: {', '.join(missing_packages)}")
        else:
            self.logger.info("✅ Todas as dependências estão instaladas")
            
        return missing_packages
        
    def create_directories(self) -> bool:
        """Cria os diretórios necessários."""
        self.logger.info("📁 Criando estrutura de diretórios...")
        
        directories = [
            RAG_ROOT_DIR,
            SOURCE_DOCUMENTS_DIR,
            FAISS_INDEX_DIR,
            LOGS_DIR
        ]
        
        try:
            for directory in directories:
                directory.mkdir(parents=True, exist_ok=True)
                self.logger.debug(f"✅ Diretório criado: {directory}")
                
            self.logger.info("✅ Estrutura de diretórios criada")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao criar diretórios: {e}")
            return False
            
    def check_source_documents(self) -> Tuple[bool, int]:
        """Verifica se há documentos para indexar."""
        self.logger.info("📄 Verificando documentos fonte...")
        
        supported_extensions = {'.md', '.txt', '.pdf', '.docx', '.html'}
        document_count = 0
        
        for ext in supported_extensions:
            files = list(SOURCE_DOCUMENTS_DIR.rglob(f"*{ext}"))
            document_count += len(files)
            if files:
                self.logger.debug(f"📄 {len(files)} arquivos {ext} encontrados")
                
        if document_count == 0:
            self.logger.warning("⚠️ Nenhum documento encontrado para indexar")
            self.logger.info(f"📁 Adicione documentos em: {SOURCE_DOCUMENTS_DIR}")
            return False, 0
        else:
            self.logger.info(f"✅ {document_count} documentos encontrados")
            return True, document_count
            
    def test_embedding_model(self) -> bool:
        """Testa o carregamento do modelo de embedding."""
        self.logger.info("🤖 Testando modelo de embedding...")
        
        try:
            embedding_manager = EmbeddingModelManager(force_cpu=self.force_cpu)
            
            # Teste simples de embedding
            test_text = "Este é um teste do sistema de embedding."
            embedding_manager.load_model()
            embedding = embedding_manager.embed_query(test_text)
            
            if embedding is not None and len(embedding) > 0:
                self.logger.info(f"✅ Modelo carregado: {EMBEDDING_MODEL_NAME}")
                self.logger.info(f"📊 Dimensão do embedding: {len(embedding)}")
                return True
            else:
                self.logger.error("❌ Falha ao gerar embedding")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro ao testar modelo: {e}")
            return False
            
    def run_indexing(self) -> bool:
        """Executa a indexação dos documentos."""
        self.logger.info("🔄 Iniciando indexação dos documentos...")
        
        try:
            indexer = RAGIndexer(force_cpu=self.force_cpu)
            success = indexer.index_documents()
            
            if success:
                self.logger.info("✅ Indexação concluída com sucesso")
                return True
            else:
                self.logger.error("❌ Falha na indexação")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro durante indexação: {e}")
            return False
            
    def test_retrieval(self) -> bool:
        """Testa o sistema de recuperação."""
        self.logger.info("🔍 Testando sistema de recuperação...")
        
        try:
            retriever = RAGRetriever(force_cpu=self.force_cpu)
            
            # Carregar o índice primeiro
            retriever.load_index()
            
            # Teste de consulta
            test_query = "arquitetura do sistema"
            results = retriever.search(test_query, top_k=3)
            
            if results:
                self.logger.info(f"✅ Recuperação funcionando: {len(results)} resultados")
                for i, result in enumerate(results[:2], 1):
                    self.logger.info(f"  {i}. {result.document_name} (score: {result.score:.3f})")
                return True
            else:
                self.logger.warning("⚠️ Nenhum resultado encontrado")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro no teste de recuperação: {e}")
            return False
            
    def test_mcp_server(self) -> bool:
        """Testa o servidor MCP."""
        self.logger.info("🌐 Testando servidor MCP...")
        
        try:
            # Importar e testar o servidor MCP
            mcp_server_path = RAG_ROOT_DIR / "mcp_server.py"
            if not mcp_server_path.exists():
                self.logger.error("❌ Arquivo mcp_server.py não encontrado")
                return False
                
            # Teste básico de importação
            spec = subprocess.run(
                [sys.executable, "-c", "import sys; sys.path.insert(0, 'rag_infra'); import mcp_server"],
                cwd=RAG_ROOT_DIR.parent,
                capture_output=True,
                text=True
            )
            
            if spec.returncode == 0:
                self.logger.info("✅ Servidor MCP pode ser importado")
                return True
            else:
                self.logger.error(f"❌ Erro ao importar MCP server: {spec.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erro no teste do MCP server: {e}")
            return False
            
    def generate_report(self, results: dict) -> str:
        """Gera relatório do setup."""
        report = []
        report.append("\n" + "="*60)
        report.append("📊 RELATÓRIO DE SETUP DO SISTEMA RAG")
        report.append("="*60)
        
        # Status geral
        total_checks = len(results)
        passed_checks = sum(1 for v in results.values() if v)
        success_rate = (passed_checks / total_checks) * 100
        
        report.append(f"\n🎯 Status Geral: {passed_checks}/{total_checks} verificações passaram ({success_rate:.1f}%)")
        
        # Detalhes das verificações
        report.append("\n📋 Detalhes das Verificações:")
        for check, status in results.items():
            icon = "✅" if status else "❌"
            report.append(f"  {icon} {check}")
            
        # Próximos passos
        report.append("\n🚀 Próximos Passos:")
        
        if all(results.values()):
            report.append("  ✅ Sistema RAG está pronto para uso!")
            report.append("  📝 Configure o Trae IDE usando: config/trae_mcp_config.json")
            report.append("  🔄 Execute consultas usando o MCP Server")
        else:
            report.append("  ⚠️ Corrija os problemas identificados acima")
            report.append("  🔄 Execute o setup novamente após as correções")
            
        # Comandos úteis
        report.append("\n🛠️ Comandos Úteis:")
        report.append("  • Reindexar: python rag_indexer.py")
        report.append("  • Testar consulta: python rag_retriever.py")
        report.append("  • Iniciar MCP Server: python mcp_server.py")
        report.append("  • Executar testes: python tests/test_rag_system.py")
        
        report.append("\n" + "="*60)
        
        return "\n".join(report)
        
    def run_setup(self, skip_indexing: bool = False) -> bool:
        """Executa o setup completo do sistema RAG."""
        self.logger.info("🚀 Iniciando setup do Sistema RAG - Recoloca.ai")
        
        # Dicionário para armazenar resultados das verificações
        results = {}
        
        # 1. Verificar versão do Python
        results["Python 3.8+"] = self.check_python_version()
        
        # 2. Verificar GPU
        gpu_available, gpu_info = self.check_gpu_availability()
        results[f"GPU ({gpu_info})"] = gpu_available or self.force_cpu
        
        # 3. Verificar dependências
        missing_deps = self.check_dependencies()
        results["Dependências"] = len(missing_deps) == 0
        
        # 4. Criar diretórios
        results["Estrutura de diretórios"] = self.create_directories()
        
        # 5. Verificar documentos fonte
        has_docs, doc_count = self.check_source_documents()
        results[f"Documentos fonte ({doc_count})"] = has_docs
        
        # 6. Testar modelo de embedding
        results["Modelo de embedding"] = self.test_embedding_model()
        
        # 7. Executar indexação (se solicitado)
        if not skip_indexing and has_docs:
            results["Indexação"] = self.run_indexing()
            
            # 8. Testar recuperação
            if results.get("Indexação", False):
                results["Sistema de recuperação"] = self.test_retrieval()
        else:
            self.logger.info("⏭️ Indexação pulada")
            
        # 9. Testar MCP Server
        results["Servidor MCP"] = self.test_mcp_server()
        
        # Gerar e exibir relatório
        report = self.generate_report(results)
        print(report)
        
        # Salvar relatório
        report_file = LOGS_DIR / "setup_report.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        self.logger.info(f"📄 Relatório salvo em: {report_file}")
        
        # Retornar sucesso geral
        return all(results.values())

def main():
    """Função principal do script de setup."""
    parser = argparse.ArgumentParser(
        description="Setup do Sistema RAG - Recoloca.ai",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python setup_rag.py                    # Setup completo
  python setup_rag.py --force-cpu        # Forçar uso de CPU
  python setup_rag.py --skip-indexing    # Pular indexação
  python setup_rag.py --verbose          # Modo verboso
        """
    )
    
    parser.add_argument(
        '--force-cpu',
        action='store_true',
        help='Forçar uso de CPU mesmo se GPU estiver disponível'
    )
    
    parser.add_argument(
        '--skip-indexing',
        action='store_true',
        help='Pular a etapa de indexação dos documentos'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Ativar modo verboso (debug)'
    )
    
    args = parser.parse_args()
    
    # Executar setup
    setup = RAGSetup(force_cpu=args.force_cpu, verbose=args.verbose)
    success = setup.run_setup(skip_indexing=args.skip_indexing)
    
    # Exit code baseado no sucesso
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()