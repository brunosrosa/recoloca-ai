# -*- coding: utf-8 -*-
"""
Indexador RAG para o Sistema Recoloca.ai

Este módulo é responsável por indexar toda a documentação do projeto,
processando arquivos Markdown, PDFs e outros formatos suportados,
criando embeddings e armazenando no índice FAISS.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import json
import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import hashlib

import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    TextLoader,
    PyMuPDFLoader,
    UnstructuredHTMLLoader,
    UnstructuredWordDocumentLoader
)
from langchain.schema import Document

from .constants import (
    RAG_ROOT_DIR, SOURCE_DOCUMENTS_DIR, FAISS_INDEX_DIR, FAISS_INDEX_FILE,
    FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE, EMBEDDING_MODEL_NAME, USE_GPU,
    PYTORCH_INDEX_DIR, PYTORCH_INDEX_FILE, PYTORCH_DOCUMENTS_FILE, PYTORCH_METADATA_FILE,
    PYTORCH_EMBEDDINGS_FILE, PYTORCH_MAPPING_FILE,
    LOGS_DIR, CACHE_DIR, METRICS_DIR,
    ENABLE_METRICS, ENABLE_CACHING, ENABLE_PYTORCH_OPTIMIZATION,
    PYTORCH_BATCH_SIZE, PYTORCH_MAX_MEMORY_GB,
    FAISS_NPROBE, FAISS_EF_SEARCH,
    CHUNK_SIZE, CHUNK_OVERLAP, MIN_CHUNK_SIZE, SEPARATORS,
    SUPPORTED_EXTENSIONS, ENCODING_FALLBACKS,
    STATUS_MESSAGES, RESULT_TEMPLATE, DOCUMENT_CATEGORIES,
    create_directories
)
from .embedding_model import EmbeddingModelManager, initialize_embedding_model, get_embedding_manager

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Criar handler para arquivo de log
LOGS_DIR.mkdir(parents=True, exist_ok=True)
file_handler = logging.FileHandler(LOGS_DIR / "rag_indexer.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

class DocumentProcessor:
    """
    Processador de documentos para diferentes formatos.
    """
    
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=SEPARATORS,
            length_function=len
        )
    
    def load_document(self, file_path: Path) -> Optional[List[Document]]:
        """
        Carrega um documento baseado na sua extensão.
        
        Args:
            file_path: Caminho para o arquivo
            
        Returns:
            List[Document]: Lista de documentos carregados ou None se erro
        """
        try:
            extension = file_path.suffix.lower()
            
            if extension not in SUPPORTED_EXTENSIONS:
                logger.warning(f"Extensão não suportada: {extension} para {file_path}")
                return None
            
            # Selecionar loader apropriado
            if extension == ".md" or extension == ".txt":
                loader = TextLoader(str(file_path), encoding="utf-8")
            elif extension == ".pdf":
                loader = PyMuPDFLoader(str(file_path))
            elif extension == ".html":
                loader = UnstructuredHTMLLoader(str(file_path))
            elif extension == ".docx":
                loader = UnstructuredWordDocumentLoader(str(file_path))
            else:
                logger.warning(f"Loader não implementado para: {extension}")
                return None
            
            documents = loader.load()
            logger.debug(f"Carregado {len(documents)} documento(s) de {file_path}")
            
            return documents
            
        except Exception as e:
            logger.error(f"Erro ao carregar documento {file_path}: {str(e)}")
            return None
    
    def process_document(self, file_path: Path) -> List[Dict[str, Any]]:
        """
        Processa um documento completo, incluindo chunking e metadados.
        
        Args:
            file_path: Caminho para o arquivo
            
        Returns:
            List[Dict]: Lista de chunks processados com metadados
        """
        documents = self.load_document(file_path)
        if not documents:
            return []
        
        processed_chunks = []
        
        for doc_idx, document in enumerate(documents):
            # Dividir documento em chunks
            chunks = self.text_splitter.split_documents([document])
            
            for chunk_idx, chunk in enumerate(chunks):
                # Gerar metadados enriquecidos
                metadata = self._generate_metadata(file_path, chunk, doc_idx, chunk_idx)
                
                processed_chunk = {
                    "content": chunk.page_content,
                    "metadata": metadata,
                    "chunk_id": self._generate_chunk_id(file_path, doc_idx, chunk_idx)
                }
                
                processed_chunks.append(processed_chunk)
        
        logger.debug(f"Processados {len(processed_chunks)} chunks de {file_path}")
        return processed_chunks
    
    def _generate_metadata(self, file_path: Path, chunk: Document, doc_idx: int, chunk_idx: int) -> Dict[str, Any]:
        """
        Gera metadados enriquecidos para um chunk.
        
        Args:
            file_path: Caminho do arquivo
            chunk: Chunk do documento
            doc_idx: Índice do documento
            chunk_idx: Índice do chunk
            
        Returns:
            Dict: Metadados do chunk
        """
        # Metadados básicos
        metadata = {
            "source": str(file_path.relative_to(SOURCE_DOCUMENTS_DIR)),
            "title": file_path.stem,
            "chunk_id": self._generate_chunk_id(file_path, doc_idx, chunk_idx),
            "timestamp": datetime.now().isoformat(),
            "file_type": file_path.suffix.lower(),
            "file_size": file_path.stat().st_size,
            "language": "pt-br",  # Assumindo português brasileiro
            "version": "1.0"
        }
        
        # Determinar categoria baseada no caminho
        category = self._determine_category(file_path)
        metadata["category"] = category
        
        # Extrair seção do conteúdo (se houver headers)
        section = self._extract_section(chunk.page_content)
        metadata["section"] = section
        
        # Adicionar metadados do chunk original se existirem
        if hasattr(chunk, 'metadata') and chunk.metadata:
            metadata.update(chunk.metadata)
        
        return metadata
    
    def _generate_chunk_id(self, file_path: Path, doc_idx: int, chunk_idx: int) -> str:
        """
        Gera um ID único para o chunk.
        
        Args:
            file_path: Caminho do arquivo
            doc_idx: Índice do documento
            chunk_idx: Índice do chunk
            
        Returns:
            str: ID único do chunk
        """
        source_str = f"{file_path.relative_to(SOURCE_DOCUMENTS_DIR)}_{doc_idx}_{chunk_idx}"
        return hashlib.md5(source_str.encode()).hexdigest()[:16]
    
    def _determine_category(self, file_path: Path) -> str:
        """
        Determina a categoria do documento baseada no caminho.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            str: Categoria do documento
        """
        path_parts = file_path.parts
        
        for part in path_parts:
            if part in DOCUMENT_CATEGORIES:
                return DOCUMENT_CATEGORIES[part]
        
        # Categoria padrão baseada no diretório pai
        parent_name = file_path.parent.name
        if "PM" in parent_name.upper():
            return "product_management"
        elif "UX" in parent_name.upper():
            return "user_experience"
        elif "TECH" in parent_name.upper() or "API" in parent_name.upper():
            return "technical"
        elif "ERS" in parent_name.upper():
            return "requirements"
        elif "ARQUITETURA" in parent_name.upper() or "HLD" in parent_name.upper():
            return "architecture"
        else:
            return "general"
    
    def _extract_section(self, content: str) -> str:
        """
        Extrai a seção do conteúdo baseada em headers Markdown.
        
        Args:
            content: Conteúdo do chunk
            
        Returns:
            str: Nome da seção ou 'main' se não encontrada
        """
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                # Remover marcadores de header e retornar o título
                return line.lstrip('#').strip()
        
        return "main"

class RAGIndexer:
    """
    Indexador principal do sistema RAG.
    """
    
    def __init__(self, force_cpu: bool = False):
        """
        Inicializa o indexador RAG.
        
        Args:
            force_cpu: Se True, força o uso de CPU
        """
        self.processor = DocumentProcessor()
        self.embedding_manager = None
        self.force_cpu = force_cpu
        self.index = None
        self.documents = []
        self.metadata = []
        
        # Criar diretórios necessários
        FAISS_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    
    def initialize(self) -> bool:
        """
        Inicializa o modelo de embedding.
        
        Returns:
            bool: True se inicializado com sucesso
        """
        try:
            logger.info("Inicializando modelo de embedding...")
            success = initialize_embedding_model(force_cpu=self.force_cpu)
            
            if success:
                self.embedding_manager = get_embedding_manager()
                logger.info("[OK] Modelo de embedding inicializado")
                return True
            else:
                logger.error("[ERROR] Falha ao inicializar modelo de embedding")
                return False
                
        except Exception as e:
            logger.error(f"Erro na inicialização: {str(e)}")
            return False
    
    def discover_documents(self) -> List[Path]:
        """
        Descobre todos os documentos para indexação.
        
        Returns:
            List[Path]: Lista de caminhos de arquivos encontrados
        """
        documents = []
        
        for extension in SUPPORTED_EXTENSIONS:
            pattern = f"**/*{extension}"
            found_files = list(SOURCE_DOCUMENTS_DIR.rglob(pattern))
            documents.extend(found_files)
        
        # Filtrar arquivos ocultos e temporários
        documents = [
            doc for doc in documents 
            if not any(part.startswith('.') for part in doc.parts)
            and not doc.name.startswith('~')
        ]
        
        logger.info(f"Descobertos {len(documents)} documentos para indexação")
        return documents
    
    def process_documents(self, file_paths: List[Path]) -> Tuple[List[str], List[Dict[str, Any]]]:
        """
        Processa todos os documentos e extrai chunks.
        
        Args:
            file_paths: Lista de caminhos de arquivos
            
        Returns:
            Tuple: (textos dos chunks, metadados dos chunks)
        """
        all_texts = []
        all_metadata = []
        
        total_files = len(file_paths)
        processed_files = 0
        
        for file_path in file_paths:
            try:
                logger.debug(f"Processando: {file_path}")
                chunks = self.processor.process_document(file_path)
                
                for chunk in chunks:
                    all_texts.append(chunk["content"])
                    all_metadata.append(chunk["metadata"])
                
                processed_files += 1
                
                if processed_files % 10 == 0:
                    logger.info(f"Progresso: {processed_files}/{total_files} arquivos processados")
                    
            except Exception as e:
                logger.error(f"Erro ao processar {file_path}: {str(e)}")
                continue
        
        logger.info(f"Processamento concluído: {len(all_texts)} chunks de {processed_files} arquivos")
        return all_texts, all_metadata
    
    def create_embeddings(self, texts: List[str]) -> Optional[np.ndarray]:
        """
        Cria embeddings para todos os textos.
        
        Args:
            texts: Lista de textos para embedding
            
        Returns:
            np.ndarray: Array de embeddings ou None se erro
        """
        if not self.embedding_manager:
            logger.error("Modelo de embedding não inicializado")
            return None
        
        try:
            logger.info(f"Gerando embeddings para {len(texts)} chunks...")
            start_time = time.time()
            
            embeddings = self.embedding_manager.embed_documents(texts)
            
            if embeddings is None:
                logger.error("Falha ao gerar embeddings")
                return None
            
            # Converter para numpy array
            embeddings_array = np.array(embeddings).astype('float32')
            
            elapsed_time = time.time() - start_time
            logger.info(f"Embeddings gerados em {elapsed_time:.2f}s")
            
            return embeddings_array
            
        except Exception as e:
            logger.error(f"Erro ao criar embeddings: {str(e)}")
            return None
    
    def create_faiss_index(self, embeddings: np.ndarray) -> Optional[faiss.Index]:
        """
        Cria o índice FAISS.
        
        Args:
            embeddings: Array de embeddings
            
        Returns:
            faiss.Index: Índice FAISS criado ou None se erro
        """
        try:
            dimension = embeddings.shape[1]
            logger.info(f"Criando índice FAISS com dimensão {dimension}")
            
            # Criar índice FAISS (Inner Product para embeddings normalizados)
            index = faiss.IndexFlatIP(dimension)
            
            # Adicionar embeddings ao índice
            index.add(embeddings)
            
            logger.info(f"Índice FAISS criado com {index.ntotal} vetores")
            return index
            
        except Exception as e:
            logger.error(f"Erro ao criar índice FAISS: {str(e)}")
            return None
    
    def save_index(self, index, documents: List[str], metadata: List[Dict]) -> bool:
        """
        Salva o índice FAISS e metadados.
        
        Args:
            index: Índice FAISS
            documents: Lista de documentos
            metadata: Lista de metadados dos documentos
            
        Returns:
            bool: True se salvo com sucesso
        """
        import tempfile
        import shutil
        import os
        from uuid import uuid4
        
        try:
            # Salvar índice FAISS usando diretório temporário para evitar problemas com Unicode
            index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
            
            # Usar diretório temporário seguro
            temp_dir = "C:\\Temp" if os.name == "nt" else "/tmp"
            if not Path(temp_dir).exists():
                Path(temp_dir).mkdir(parents=True, exist_ok=True)
            
            with tempfile.TemporaryDirectory(dir=temp_dir) as temp_path:
                temp_file_path = Path(temp_path) / f"faiss_index_{uuid4().hex}.bin"
                faiss.write_index(index, str(temp_file_path))
                shutil.move(str(temp_file_path), str(index_path))
            
            logger.info(f"Índice FAISS salvo em: {index_path}")
            
            # Salvar documentos
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            with open(documents_path, 'w', encoding='utf-8') as f:
                json.dump(documents, f, ensure_ascii=False, indent=2)
            logger.info(f"Documentos salvos em: {documents_path}")
            
            # Salvar metadados
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            index_metadata = {
                "created_at": datetime.now().isoformat(),
                "total_documents": len(documents),
                "embedding_model": self.embedding_manager.model_name,
                "index_dimension": index.d,
                "chunk_size": CHUNK_SIZE,
                "chunk_overlap": CHUNK_OVERLAP,
                "documents_metadata": metadata
            }
            
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(index_metadata, f, ensure_ascii=False, indent=2)
            logger.info(f"Metadados salvos em: {metadata_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao salvar índice: {str(e)}")
            return False
    
    def index_documents(self, reindex: bool = False) -> bool:
        """
        Executa o processo completo de indexação.
        
        Args:
            reindex: Se True, força reindexação mesmo se índice existir
            
        Returns:
            bool: True se indexação bem-sucedida
        """
        try:
            # Verificar se já existe índice
            index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
            if index_path.exists() and not reindex:
                logger.info("Índice já existe. Use reindex=True para forçar reindexação.")
                return True
            
            logger.info(STATUS_MESSAGES["indexing_start"])
            start_time = time.time()
            
            # 1. Inicializar modelo de embedding
            if not self.initialize():
                return False
            
            # 2. Descobrir documentos
            file_paths = self.discover_documents()
            if not file_paths:
                logger.warning("Nenhum documento encontrado para indexação")
                return False
            
            # 3. Processar documentos
            texts, metadata = self.process_documents(file_paths)
            if not texts:
                logger.error("Nenhum texto extraído dos documentos")
                return False
            
            # 4. Criar embeddings
            embeddings = self.create_embeddings(texts)
            if embeddings is None:
                return False
            
            # 5. Criar índice FAISS
            index = self.create_faiss_index(embeddings)
            if index is None:
                return False
            
            # 6. Salvar índice e metadados
            if not self.save_index(index, texts, metadata):
                return False
            
            elapsed_time = time.time() - start_time
            logger.info(STATUS_MESSAGES["indexing_complete"])
            logger.info(f"Tempo total de indexação: {elapsed_time:.2f}s")
            logger.info(f"Documentos indexados: {len(texts)} chunks de {len(file_paths)} arquivos")
            
            return True
            
        except Exception as e:
            logger.error(STATUS_MESSAGES["indexing_error"].format(error=str(e)))
            return False

def main():
    """
    Função principal para execução standalone.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Indexador RAG para Recoloca.ai")
    parser.add_argument("--reindex", action="store_true", help="Forçar reindexação")
    parser.add_argument("--cpu", action="store_true", help="Forçar uso de CPU")
    parser.add_argument("--verbose", "-v", action="store_true", help="Log verboso")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Criar indexador
    indexer = RAGIndexer(force_cpu=args.cpu)
    
    # Executar indexação
    success = indexer.index_documents(reindex=args.reindex)
    
    if success:
        print("[OK] Indexação concluída com sucesso!")
    else:
        print("[ERROR] Falha na indexação")
        exit(1)

if __name__ == "__main__":
    main()