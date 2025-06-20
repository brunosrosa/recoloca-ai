# Script para ativar o ambiente virtual .venv do Recoloca.AI
# Uso: .\activate_env.ps1

Write-Host "Ativando ambiente virtual .venv do Recoloca.AI..." -ForegroundColor Green

# Verifica se o diretório .venv existe
if (Test-Path ".venv\Scripts\Activate.ps1") {
    # Ativa o ambiente virtual
    & ".venv\Scripts\Activate.ps1"
    
    Write-Host "Ambiente .venv ativado com sucesso!" -ForegroundColor Green
    Write-Host "Versao do Python:" -ForegroundColor Cyan
    python --version
    
    Write-Host "Para verificar pacotes instalados, use: pip list" -ForegroundColor Yellow
    Write-Host "Para executar o backend: cd src/backend_fastapi && uvicorn main:app --reload" -ForegroundColor Yellow
    
} else {
    Write-Host "Erro: Diretorio .venv nao encontrado!" -ForegroundColor Red
    Write-Host "Certifique-se de estar no diretorio raiz do projeto Recoloca.AI" -ForegroundColor Yellow
}