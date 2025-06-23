---
sticker: lucide//play-circle
---
# GUIA DE EXECUÇÃO - REORGANIZAÇÃO ESTRUTURAL RAG_INFRA

**Versão:** 1.0  
**Data:** Junho de 2025  
**Autor:** @AgenteM_ArquitetoTI  
**Destinatário:** Maestro  
**Tempo Estimado:** 6-8 horas  
**Complexidade:** Média  

## 🎯 RESUMO EXECUTIVO

Este guia fornece um roteiro completo para executar a reorganização estrutural do `rag_infra/`, transformando a estrutura atual em uma organização "future-proof" que resolve problemas de manutenibilidade, performance e escalabilidade.

### Benefícios Esperados
- ✅ **Organização clara:** Cada arquivo em seu lugar apropriado
- ✅ **Cache unificado:** Eliminação de duplicações e fragmentação
- ✅ **Logs centralizados:** Melhor observabilidade e debugging
- ✅ **Estrutura escalável:** Preparada para crescimento futuro
- ✅ **Manutenibilidade:** Facilidade para localizar e modificar componentes

## 📋 PRÉ-REQUISITOS

### Verificações Obrigatórias
- [ ] **Backup do projeto completo** (incluindo Git)
- [ ] **Sistema RAG funcionando** corretamente
- [ ] **Testes de integração** passando
- [ ] **Janela de manutenção** agendada (6-8 horas)
- [ ] **Python 3.8+** instalado
- [ ] **Permissões de escrita** no diretório do projeto

### Documentos de Referência
- [[PROPOSTA_REORGANIZACAO_RAG_INFRA_ESTRUTURAL.md]] - Proposta detalhada
- [[ADR-008-Reorganizacao-Estrutural-RAG-Infra.md]] - Decisão arquitetural
- [[01_HLD.md]] - Arquitetura atual do sistema

## 🚀 ROTEIRO DE EXECUÇÃO

### ETAPA 1: PREPARAÇÃO E VALIDAÇÃO (30 min)

#### 1.1 Backup Completo
```powershell
# Navegar para o diretório do projeto
<<<<<<< HEAD
cd "c:\Users\rosas\OneDrive\Documentos\Obisidian DB\🟢 Projects\💼 Recoloca.AI"
=======
cd "c:\Users\rosas\OneDrive\Documentos\Obisidian DB\Projects/Recoloca.AI"
>>>>>>> 1d8d89e (Messy. Needs to Refactore.)

# Criar backup com timestamp
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupDir = "rag_infra_backup_$timestamp"
Copy-Item -Path "rag_infra" -Destination $backupDir -Recurse

Write-Host "Backup criado em: $backupDir" -ForegroundColor Green
```

#### 1.2 Validação do Sistema Atual
```powershell
# Testar funcionamento do RAG
cd rag_infra
python -c "from core_logic.rag_retriever import RAGRetriever; print('Sistema RAG OK')"

# Verificar MCP Server
python core_logic/mcp_server.py --test
```

#### 1.3 Análise da Estrutura Atual
```powershell
# Listar estrutura atual
tree /F > estrutura_atual.txt
Get-Content estrutura_atual.txt
```

### ETAPA 2: EXECUÇÃO DA MIGRAÇÃO (4-5 horas)

#### 2.1 Dry-Run (Simulação)
```powershell
# Executar simulação para validar o plano
python scripts/reorganize_structure.py --dry-run --base-path .

# Revisar o log de simulação
Get-Content reorganization.log | Select-Object -Last 50
```

#### 2.2 Execução Real
```powershell
# ATENÇÃO: Esta operação modifica a estrutura real
# Certifique-se de que o backup foi criado

python scripts/reorganize_structure.py --base-path .

# Monitorar progresso
Get-Content reorganization.log -Wait
```

#### 2.3 Validação Pós-Migração
```powershell
# Verificar nova estrutura
tree /F > estrutura_nova.txt

# Comparar estruturas
fc estrutura_atual.txt estrutura_nova.txt

# Testar funcionamento básico
python src/core/mcp_server.py --test
```

### ETAPA 3: ATUALIZAÇÃO DE CONFIGURAÇÕES (1 hora)

#### 3.1 Atualizar Imports e Referências
```powershell
# Buscar por imports que precisam ser atualizados
Select-String -Path "src\**\*.py" -Pattern "from core_logic" -Recurse
Select-String -Path "src\**\*.py" -Pattern "import core_logic" -Recurse

# Atualizar manualmente os imports encontrados
# core_logic.* -> src.core.*
# utils.* -> src.utils.*
```

#### 3.2 Configurar Variáveis de Ambiente
```powershell
# Criar arquivo de configuração de ambiente
@"
RAG_BASE_PATH=./
RAG_DATA_PATH=./data
RAG_CACHE_PATH=./temp/cache
RAG_LOGS_PATH=./temp/logs
RAG_CONFIG_PATH=./config
"@ | Out-File -FilePath "config\environments\development.env" -Encoding UTF8
```

#### 3.3 Atualizar Scripts de Automação
```powershell
# Verificar scripts que referenciam caminhos antigos
Select-String -Path "scripts\**\*.py" -Pattern "core_logic|data_index|results_and_reports" -Recurse

# Atualizar conforme necessário
```

### ETAPA 4: TESTES E VALIDAÇÃO (1-2 horas)

#### 4.1 Testes de Funcionalidade
```powershell
# Executar testes unitários
python -m pytest src/tests/unit/ -v

# Executar testes de integração
python -m pytest src/tests/integration/ -v

# Teste manual do MCP Server
python src/core/mcp_server/mcp_server.py
```

#### 4.2 Testes de Performance
```powershell
# Benchmark de indexação
python src/utils/optimization/benchmark_indexing.py

# Benchmark de consultas
python src/utils/optimization/benchmark_queries.py

# Comparar com métricas anteriores
```

#### 4.3 Validação de Integração
```powershell
# Testar integração com Trae IDE
# (Verificar se o MCP Server responde corretamente)

# Testar sincronização automática
python src/utils/maintenance/rag_auto_sync.py --test
```

### ETAPA 5: DOCUMENTAÇÃO E FINALIZAÇÃO (30 min)

#### 5.1 Atualizar Documentação
- [ ] Atualizar [[01_HLD.md]] com nova estrutura
- [ ] Revisar READMEs criados automaticamente
- [ ] Atualizar guias de desenvolvimento

#### 5.2 Commit das Mudanças
```powershell
# Adicionar arquivos ao Git
git add .

# Commit com mensagem descritiva
git commit -m "feat: reorganização estrutural completa do rag_infra

- Implementa nova estrutura future-proof
- Unifica cache e logs em temp/
- Organiza código fonte em src/
- Centraliza configurações em config/
- Separa dados persistentes em data/
- Adiciona documentação e scripts organizados

Ref: ADR-008"

# Push para repositório
git push
```

#### 5.3 Limpeza e Otimização
```powershell
# Limpar cache antigo (se existir)
Remove-Item -Path "temp\cache\old_*" -Recurse -Force -ErrorAction SilentlyContinue

# Executar primeira indexação com nova estrutura
python src/core/indexer/rag_indexer.py --full-reindex
```

## 🔍 CHECKLIST DE VALIDAÇÃO

### Funcionalidade
- [ ] Sistema RAG indexa documentos corretamente
- [ ] Consultas semânticas funcionam
- [ ] MCP Server responde adequadamente
- [ ] Integração com Trae IDE operacional
- [ ] Sincronização automática ativa

### Performance
- [ ] Tempo de indexação ≤ baseline anterior
- [ ] Tempo de consulta ≤ baseline anterior
- [ ] Uso de memória estável
- [ ] Cache funcionando eficientemente

### Organização
- [ ] Estrutura conforme especificação
- [ ] Arquivos temporários em temp/
- [ ] Logs centralizados
- [ ] Cache unificado
- [ ] Configurações organizadas

### Documentação
- [ ] READMEs criados e informativos
- [ ] HLD atualizado
- [ ] ADR-008 marcado como implementado
- [ ] Guias de desenvolvimento atualizados

## 🚨 PLANO DE ROLLBACK

Em caso de problemas críticos:

### Rollback Rápido (15 min)
```powershell
# Parar sistema
Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue

# Remover estrutura nova
Remove-Item -Path "rag_infra" -Recurse -Force

# Restaurar backup
Copy-Item -Path $backupDir -Destination "rag_infra" -Recurse

# Validar funcionamento
cd rag_infra
python core_logic/mcp_server.py --test
```

### Investigação Pós-Rollback
1. Analisar logs de erro
2. Identificar causa raiz
3. Ajustar plano de migração
4. Reagendar nova tentativa

## 📊 MÉTRICAS DE SUCESSO

### Quantitativas
- **Tempo de indexação:** Mantido ou melhorado
- **Tempo de consulta:** < 500ms (baseline atual)
- **Uso de disco:** Redução de 10-20% (cache unificado)
- **Taxa de erro:** 0% durante operação normal

### Qualitativas
- **Facilidade de navegação:** Estrutura intuitiva
- **Manutenibilidade:** Localização rápida de componentes
- **Escalabilidade:** Preparação para crescimento
- **Conformidade:** Alinhamento com padrões arquiteturais

## 🎉 PÓS-IMPLEMENTAÇÃO

### Ações Imediatas
1. **Monitorar sistema** por 24-48 horas
2. **Coletar feedback** da equipe de desenvolvimento
3. **Documentar lições aprendidas**
4. **Atualizar procedimentos** de manutenção

### Melhorias Futuras
1. **Automação adicional** de limpeza de cache
2. **Monitoramento proativo** de uso de disco
3. **Scripts de backup** automatizados
4. **Integração com CI/CD** para validação contínua

## 📞 SUPORTE E CONTATOS

- **Arquiteto Responsável:** @AgenteM_ArquitetoTI
- **Suporte Técnico:** @AgenteM_DevFastAPI
- **Escalação:** @AgenteM_Orquestrador

---

**⚠️ IMPORTANTE:** Este guia deve ser seguido integralmente. Em caso de dúvidas ou problemas, interrompa o processo e consulte o arquiteto responsável antes de prosseguir.

**✅ SUCESSO:** Ao final deste processo, você terá uma infraestrutura RAG organizada, escalável e preparada para o futuro, com melhor manutenibilidade e performance otimizada.