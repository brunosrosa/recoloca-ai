#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste de inicialização do RAG
"""

import sys
import os
from pathlib import Path
import unittest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestRAGInitialization(unittest.TestCase):
    def setUp(self):
        # Add core directory to path
        self.project_root = Path(__file__).parent.parent.parent
        sys.path.insert(0, str(self.project_root / "src" / "core"))
        
        logger.info("Testing RAG initialization...")
        self.core_logic_path = self.project_root / "src" / "core"
        logger.info(f"Core logic path: {self.core_logic_path}")
        logger.info(f"Path exists: {self.core_logic_path.exists()}")

    def test_rag_import(self):
        try:
            from rag_infra.src.core.rag_retriever import RAGRetriever
            logger.info("[OK] Import successful")
            self.assertTrue(True)
        except Exception:
            logger.error("[ERROR] Import failed")
            self.fail("Failed to import RAGRetriever")

    def test_rag_initialization(self):
        from rag_infra.src.core.rag_retriever import RAGRetriever
        retriever = RAGRetriever()
        logger.info(f"[OK] Retriever type: {type(retriever)}")
        logger.info(f"Is loaded: {retriever.is_loaded}")
        
        self.assertIsInstance(retriever, RAGRetriever)
        self.assertIsNotNone(retriever.is_loaded)

    def test_rag_search(self):
        from rag_infra.src.core.rag_retriever import RAGRetriever
        retriever = RAGRetriever()

        try:
            if not retriever.is_loaded:
                retriever.initialize()
                retriever.load_index()
                
            logger.info("\n[SEARCH] Testing search...")
            results = retriever.search("teste", top_k=1)
            logger.info(f"Search results: {len(results) if results else 'None'}")
            
            self.assertIsNotNone(results)
            
        except AttributeError:
            logger.error("[ERROR] Retriever not loaded")
            self.fail("Retriever not loaded")
        except RuntimeError:
            logger.error("[ERROR] Initialization failed")
            self.fail("Initialization failed")
        except Exception as e:
            logger.error(f"[ERROR] Error: {e}")
            self.fail(f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    unittest.main()
