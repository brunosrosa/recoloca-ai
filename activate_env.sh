#!/bin/bash
# Script para ativar o ambiente virtual .venv do Recoloca.AI
# Uso: source activate_env.sh

echo "🐍 Ativando ambiente virtual .venv do Recoloca.AI..."

# Verifica se o diretório .venv existe
if [ -f ".venv/bin/activate" ]; then
    # Ativa o ambiente virtual
    source .venv/bin/activate
    
    echo "✅ Ambiente .venv ativado com sucesso!"
    echo "📦 Versão do Python:"
    python --version
    
    echo "📋 Para verificar pacotes instalados, use: pip list"
    echo "🚀 Para executar o backend: cd src/backend_fastapi && uvicorn main:app --reload"
    
else
    echo "❌ Erro: Diretório .venv não encontrado!"
    echo "💡 Certifique-se de estar no diretório raiz do projeto Recoloca.AI"
fi