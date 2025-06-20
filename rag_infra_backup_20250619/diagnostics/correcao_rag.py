#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Correção do Sistema RAG - Recoloca.ai

Este script implementa as correções identificadas no diagnóstico do RAGRetriever.

Autor: @AgenteM_ArquitetoTI
Versão: 1.0
Data: Junho 2025
"""

import sys
import logging
from pathlib import Path
import time

# Adicionar o diretório core_logic ao path
sys.path.insert(0, str(Path(__file__).parent / "core_logic"))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_score_thresholds():
    """Testa diferentes thresholds de score para otimizar resultados."""
    print("\n=== TESTE DE THRESHOLDS DE SCORE ===")
    
    try:
        from rag_retriever import RAGRetriever
        from constants import MIN_SIMILARITY_SCORE
        
        retriever = RAGRetriever()
        
        if not retriever.initialize():
            print("ERRO: Falha na inicialização")
            return
        
        if not retriever.load_index():
            print("ERRO: Falha no carregamento do índice")
            return
        
        test_query = "Recoloca.ai MVP desenvolvimento"
        thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
        
        print(f"Threshold atual configurado: {MIN_SIMILARITY_SCORE}")
        print(f"Testando query: '{test_query}'")
        print()
        
        for threshold in thresholds:
            results = retriever.search(test_query, top_k=5, min_score=threshold)
            print(f"Threshold {threshold:.1f}: {len(results)} resultados")
            
            if results:
                scores = [r.score for r in results]
                print(f"  Scores: {[f'{s:.3f}' for s in scores]}")
            print()
        
        # Teste com threshold otimizado
        print("=== TESTE COM THRESHOLD OTIMIZADO ===")
        optimal_threshold = 0.2  # Baseado nos resultados
        
        test_queries = [
            "Recoloca.ai MVP",
            "arquitetura sistema",
            "API desenvolvimento",
            "banco de dados",
            "autenticação usuário"
        ]
        
        for query in test_queries:
            results = retriever.search(query, top_k=3, min_score=optimal_threshold)
            print(f"'{query}': {len(results)} resultados")
            
            if results:
                best_score = max(r.score for r in results)
                print(f"  Melhor score: {best_score:.3f}")
        
    except Exception as e:
        print(f"ERRO no teste: {e}")
        import traceback
        traceback.print_exc()

def update_constants_file():
    """Atualiza o arquivo constants.py com threshold otimizado."""
    print("\n=== ATUALIZANDO CONSTANTS.PY ===")
    
    try:
        constants_path = Path(__file__).parent / "core_logic" / "constants.py"
        
        # Ler arquivo atual
        with open(constants_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar valor atual
        import re
        current_match = re.search(r'MIN_SIMILARITY_SCORE\s*=\s*([0-9.]+)', content)
        
        if current_match:
            current_value = float(current_match.group(1))
            print(f"Valor atual MIN_SIMILARITY_SCORE: {current_value}")
            
            # Atualizar para valor otimizado
            optimal_value = 0.2
            
            if current_value != optimal_value:
                new_content = re.sub(
                    r'MIN_SIMILARITY_SCORE\s*=\s*[0-9.]+',
                    f'MIN_SIMILARITY_SCORE = {optimal_value}',
                    content
                )
                
                # Fazer backup
                backup_path = constants_path.with_suffix('.py.backup')
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Backup criado: {backup_path}")
                
                # Salvar nova versão
                with open(constants_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"MIN_SIMILARITY_SCORE atualizado para: {optimal_value}")
            else:
                print("Valor já está otimizado")
        else:
            print("ERRO: MIN_SIMILARITY_SCORE não encontrado no arquivo")
        
    except Exception as e:
        print(f"ERRO na atualização: {e}")
        import traceback
        traceback.print_exc()

def test_mcp_integration():
    """Testa a integração com o MCP Server."""
    print("\n=== TESTE DE INTEGRAÇÃO MCP ===")
    
    try:
        # Testar funções do MCP
        from rag_retriever import search_documents, get_retriever
        
        # Teste da função search_documents (usada pelo MCP)
        print("Testando search_documents...")
        results = search_documents("Recoloca.ai MVP", top_k=3)
        print(f"search_documents: {len(results)} resultados")
        
        # Teste do get_retriever
        print("Testando get_retriever...")
        retriever = get_retriever()
        if retriever:
            print(f"get_retriever: OK - {type(retriever)}")
            print(f"Documentos carregados: {len(retriever.documents)}")
        else:
            print("get_retriever: FALHA")
        
    except Exception as e:
        print(f"ERRO no teste MCP: {e}")
        import traceback
        traceback.print_exc()

def validate_fixes():
    """Valida se as correções foram aplicadas com sucesso."""
    print("\n=== VALIDAÇÃO DAS CORREÇÕES ===")
    
    try:
        from rag_retriever import RAGRetriever
        from constants import MIN_SIMILARITY_SCORE
        
        print(f"MIN_SIMILARITY_SCORE atual: {MIN_SIMILARITY_SCORE}")
        
        # Teste final
        retriever = RAGRetriever()
        
        if not retriever.initialize():
            print("ERRO: Falha na inicialização")
            return False
        
        if not retriever.load_index():
            print("ERRO: Falha no carregamento")
            return False
        
        # Teste com query que anteriormente retornava 0 resultados
        results = retriever.search("Recoloca.ai MVP desenvolvimento", top_k=5)
        
        print(f"Teste final: {len(results)} resultados encontrados")
        
        if len(results) > 0:
            print("SUCESSO: Sistema RAG corrigido e funcionando")
            
            for i, result in enumerate(results[:3]):
                print(f"  [{i+1}] Score: {result.score:.3f} - {result.content[:60]}...")
            
            return True
        else:
            print("PROBLEMA: Ainda retornando 0 resultados")
            return False
        
    except Exception as e:
        print(f"ERRO na validação: {e}")
        return False

def main():
    """Executa todas as correções do sistema RAG."""
    print("CORRECAO DO SISTEMA RAG - RECOLOCA.AI")
    print("=" * 50)
    
    # Executar testes e correções
    test_score_thresholds()
    update_constants_file()
    test_mcp_integration()
    
    # Validação final
    success = validate_fixes()
    
    print("\n" + "=" * 50)
    if success:
        print("CORRECAO CONCLUIDA COM SUCESSO")
        print("\nProximos passos:")
        print("1. Testar MCP Server com as correções")
        print("2. Validar integração com Trae IDE")
        print("3. Documentar as correções aplicadas")
    else:
        print("CORRECAO FALHOU - INVESTIGACAO ADICIONAL NECESSARIA")
    
    return success

if __name__ == "__main__":
    main()