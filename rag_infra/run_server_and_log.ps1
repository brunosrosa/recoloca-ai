# Força a codificação de saída para UTF-8 para lidar com caracteres especiais no caminho
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Define o diretório de trabalho para a raiz do projeto rag_infra (o diretório do script)
$projectRoot = $PSScriptRoot
Set-Location -Path $projectRoot

# Caminho para o arquivo de log unificado
$logFile = Join-Path -Path $projectRoot -ChildPath "logs\mcp_server.log"

# Caminho para o script do servidor MCP
$serverScript = Join-Path -Path $projectRoot -ChildPath "server\mcp_server.py"

# Define o PYTHONPATH para incluir o diretório do projeto
$env:PYTHONPATH = $projectRoot

# Executa o comando usando o operador de chamada '&' para segurança.
# Redireciona todos os streams (*>) para um processo ForEach-Object.
# Dentro do loop, cada linha de saída é adicionada ao arquivo de log com codificação UTF8
# e também escrita no console (host).
& uv run --link-mode=copy --active $serverScript *>&1 | ForEach-Object {
    $_ | Out-File -FilePath $logFile -Append -Encoding utf8
    Write-Host $_
}