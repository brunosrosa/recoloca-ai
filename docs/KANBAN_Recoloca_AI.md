---
kanban-plugin: basic
---
## 🧊 Backlog Geral
- [ ] Refinar ERS para RF-CV-005 [cite: 112] #humano #po
- [ ] Gerar HUs e ACs para RF-CV-005 [cite: 95] #agente_po [[TPL_Gerar_HU.md]] [[ERS.md#RF-CV-005]]
- [ ] Criar HLD para Módulo de Otimização de CV #agente_arquiteto [[TPL_Gerar_HLD.md]] [[ERS.md#RF-CV-005]]

## ✍️ À Fazer - Humano (Revisão/Preparação)
- [ ] Revisar HLD do Módulo de Otimização de CV #humano #maestro
- [ ] Preparar prompt detalhado para LLD do Parser #humano #maestro [[HLD.md]] [[TPL_Gerar_LLD.md]]

## 🤖 À Fazer - Agente IA
- [ ] Gerar LLD para Parser de PDF (RF-CV-002) [cite: 128] #agente_lld [[HLD.md]] [[ERS.md#RF-CV-002]] [[PRM_LLD_Parser.md]]
- [ ] Gerar código Backend para endpoint /cv/upload (RF-CV-001) [cite: 203] #agente_dev_backend [[LLD_Parser.md]] [[TPL_Gerar_Codigo_FastAPI.md]]

## ⚙️ Em Processamento - Humano
- [ ] Configurar ambiente de testes para Backend #humano #maestro

## ⏳ Em Processamento - Agente IA
- [ ] Gerando código Frontend para tela de Upload de CV #agente_dev_frontend

## 🧐 Revisão - Humano (HITL)
- [ ] Revisar código Backend /cv/upload gerado #humano #maestro #hitl_fase1
- [ ] Revisar e validar HUs/ACs geradas para RF-CV-005 [cite: 95] #humano #maestro

## ✅ Feito
- [x] Configurar Repositório Git para Documentação
- [x] Instalar Plugin Kanban no Obsidian

%% kanban:settings
{"kanban-plugin":"basic"}
%%