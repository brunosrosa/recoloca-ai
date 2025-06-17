---
kanban-plugin: board
sticker: lucide//bug
---

# 🐛 KANBAN BUGS & ISSUES TÉCNICAS

> **Objetivo:** Gestão específica de bugs, issues técnicas e correções do sistema Recoloca.ai
> **Quando usar:** Quando o volume de bugs justificar um quadro dedicado (geralmente pós-MVP)
> **Responsáveis:** @AgenteM_DevFastAPI, @AgenteM_DevFlutter, @AgenteM_ArquitetoTI

## 🚨 CRÍTICO (P0)

*Bugs que impedem o funcionamento básico do sistema*

### Critérios P0:
- Sistema inacessível ou inoperante
- Perda de dados do usuário
- Falhas de segurança críticas
- Quebra de funcionalidades core


## 🔺 ALTA PRIORIDADE (P1)

*Bugs que afetam funcionalidades importantes*

### Critérios P1:
- Funcionalidades principais com comportamento incorreto
- Performance severamente degradada
- Problemas de UX que impedem fluxos principais
- Erros que afetam múltiplos usuários


## ⏫ MÉDIA PRIORIDADE (P2)

*Bugs que afetam experiência do usuário*

### Critérios P2:
- Problemas de interface e usabilidade
- Funcionalidades secundárias com falhas
- Performance moderadamente afetada
- Inconsistências visuais


## 🔽 BAIXA PRIORIDADE (P3)

*Melhorias e correções menores*

### Critérios P3:
- Problemas cosméticos
- Funcionalidades nice-to-have com falhas
- Otimizações de código
- Refatorações técnicas


## 🔄 EM INVESTIGAÇÃO

*Issues sendo analisadas ou reproduzidas*

### Status de Investigação:
- **Reportado:** Bug identificado, aguardando análise
- **Reproduzindo:** Tentando replicar o problema
- **Analisando:** Investigando causa raiz
- **Aguardando Info:** Necessita mais detalhes do reporter


## ✅ RESOLVIDO

*Bugs corrigidos e validados*

### Critérios de Resolução:
- Fix implementado e testado
- Validação em ambiente de produção
- Confirmação do reporter (quando aplicável)
- Documentação atualizada (se necessário)

---

## 📋 TEMPLATE PARA NOVOS BUGS

```markdown
- [ ] **[BUG-XXX-001]** Título Descritivo do Bug 🔺 \ #bug \ #componente \ #prioridade \ #responsavel
	- **Descrição:** Descrição detalhada do problema
	- **Passos para Reproduzir:** 
		1. Passo 1
		2. Passo 2
		3. Resultado esperado vs obtido
	- **Ambiente:** [Dev/Staging/Prod] - [Browser/Device]
	- **Impacto:** Descrição do impacto no usuário/sistema
	- **Evidências:** Screenshots, logs, vídeos
	- **Workaround:** Solução temporária (se houver)
	- **Assignee:** @AgenteResponsavel
	- **Reporter:** Nome do reporter
	- **Data:** YYYY-MM-DD
```

## 🏷️ SISTEMA DE TAGS

### Por Componente:
- `#frontend` - Issues do Flutter/Web
- `#backend` - Issues do FastAPI
- `#database` - Issues do Supabase/BD
- `#auth` - Issues de autenticação
- `#api` - Issues de integração API
- `#ux` - Issues de experiência do usuário
- `#performance` - Issues de performance
- `#security` - Issues de segurança

### Por Tipo:
- `#bug` - Bug confirmado
- `#regression` - Funcionalidade que parou de funcionar
- `#enhancement` - Melhoria técnica
- `#hotfix` - Correção urgente
- `#technical-debt` - Débito técnico

### Por Ambiente:
- `#dev` - Ambiente de desenvolvimento
- `#staging` - Ambiente de homologação
- `#prod` - Ambiente de produção

## 📊 MÉTRICAS DE ACOMPANHAMENTO

### KPIs Importantes:
- **Time to Resolution:** Tempo médio para resolver bugs por prioridade
- **Bug Escape Rate:** % de bugs que chegam à produção
- **Reopen Rate:** % de bugs que retornam após correção
- **Customer Impact:** Número de usuários afetados por bugs

### Metas:
- **P0:** Resolução em < 4 horas
- **P1:** Resolução em < 24 horas
- **P2:** Resolução em < 1 semana
- **P3:** Resolução em < 1 mês

---

**Última Atualização:** {{date:YYYY-MM-DD}}
**Responsável pela Manutenção:** @AgenteM_Orquestrador

%% kanban:settings
```
{"kanban-plugin":"board","lane-width":350,"list-collapse":[null,null,null,null,null,false]}
```
%%