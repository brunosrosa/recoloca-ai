---
kanban-plugin: board
sticker: emoji//2b55
---

## 🧊 Backlog Geral

- [ ] **Pesquisa/Definição:** Pesquisar Ferramentas de Parsing PDF alternativas (se `pymupdf`/`Tesseract` não forem suficientes para `RF-CV-001`) #pesquisa #tecnico @Maestro
    
- [ ] **Infra/DevOps:** Definir Estratégia Detalhada de Monitoramento e Logging (Sentry, Better Uptime, Logtail, etc. para `RNF-REL-003`) #infra #devops @AgenteMentorDevOps @Maestro
    
- [ ] **Negócio:** Detalhar Estratégia de Precificação Tier Premium e Testes A/B (Pós-Validação com Usuários e Custos) #negocio #marketing @Maestro
    
- [ ] **Legal:** Validar Juridicamente Termos de Uso e Política de Privacidade (Pré-Lançamento Público) #legal #prioridade_media @Maestro
    
- [ ] **Arquitetura:** Detalhar LLD (Low-Level Design) para Módulos do MVP (Pós-Validação dos Passos Críticos) #arquitetura #documentacao @AgenteMentorArquitetoLLD @Maestro
    
    - [ ] `[[03_Arquitetura_e_Design/LLD/LLD_Modulo_Auth.md]]`
        
    - [ ] `[[03_Arquitetura_e_Design/LLD/LLD_Modulo_Kanban.md]]`
        
    - [ ] `[[03_Arquitetura_e_Design/LLD/LLD_Modulo_CV.md]]`
        
    - [ ] `[[03_Arquitetura_e_Design/LLD/LLD_Modulo_Coach.md]]`
        
    - [ ] `[[03_Arquitetura_e_Design/LLD/LLD_Modulo_Pagamentos.md]]`
        
- [ ] **Design:** Criar Style Guide Detalhado (`[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]` conforme `RNF-USAB-004`) #ux #ui #documentacao @AgenteMentorUIDesign @Maestro
    
- [ ] **API:** Desenvolver API Specs OpenAPI 3.0 (`[[03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]` conforme `RI-API-003`) #api #arquitetura #documentacao @AgenteMentorAPI @Maestro
    
- [ ] **Gerenciamento:** Planejar 1ª Sprint de Desenvolvimento do MVP (Pós-Validação dos Passos Críticos) #gerenciamento @Maestro
    
- [ ] **Desenvolvimento Feature - Kanban:** Implementar funcionalidades do Kanban (`RF-KAN-001` a `RF-KAN-007`) #desenvolvimento #feature_core #kanban @AgenteMentorDevFastAPI @AgenteMentorDevFlutter @Maestro
    
- [ ] **Desenvolvimento Feature - Importação de Vagas:** Implementar importação via Link com LLM (`RF-IMP-001`, `RF-IMP-002`) #desenvolvimento #feature_core #ia #importacao @AgenteMentorDevFastAPI @AgenteMentorDevFlutter @Maestro
    
- [ ] **Desenvolvimento Feature - Otimização CV:** Implementar upload, parsing, validação (`RF-CV-001`, `RF-CV-002`) #desenvolvimento #feature_core #cv @AgenteMentorDevFastAPI @AgenteMentorDevFlutter @Maestro
    
- [ ] **Desenvolvimento Feature - Otimização CV IA:** Implementar Análise Vaga-CV (Score IA), Sugestões de Otimização, Estimativa Salarial (`RF-CV-003`, `RF-CV-004`, `RF-CV-005`) #desenvolvimento #feature_core #ia #cv @AgenteMentorDevFastAPI @Maestro
    
- [ ] **Desenvolvimento Feature - Otimização CV Output:** Implementar download PDF otimizado, gerenciamento de versões (`RF-CV-006`, `RF-CV-007`) #desenvolvimento #feature_core #cv @AgenteMentorDevFastAPI @AgenteMentorDevFlutter @Maestro
    
- [ ] **Desenvolvimento Feature - Coach IA:** Implementar Chatbot básico, atuação proativa, orientações (`RF-COACH-001` a `RF-COACH-004`) #desenvolvimento #feature_core #ia #coach @AgenteMentorDevFastAPI @AgenteMentorDevFlutter @Maestro
    
- [ ] **Desenvolvimento Feature - Contas:** Implementar Autenticação, Onboarding, Gerenciamento de Perfil/CVs/Notificações/Assinaturas (`RF-AUTH-001` a `RF-AUTH-012`) #desenvolvimento #feature_core #auth @AgenteMentorDevFastAPI @AgenteMentorDevFlutter @Maestro
    
- [ ] **Desenvolvimento Feature - Pagamentos:** Configurar Gateway de Pagamento e Lógica de Assinaturas Freemium (`RF-PAY-SUB-001` a `RF-PAY-SUB-004`) #desenvolvimento #feature_core #pagamento @AgenteMentorDevFastAPI @Maestro
    
- [ ] **Desenvolvimento Pós-MVP - Extensão:** Desenvolver Web Clipper para LinkedIn (Extensão Chrome - `RF-IMP-003`) #pos_mvp #desenvolvimento #extensao @AgenteMentorDevJS @Maestro
    
- [ ] **QA/Testes:** Definir abordagem inicial para testes de funcionalidades com IA (ex: Otimização de CV, Coach IA) #qa #ia #estrategia @AgenteMentorQA @Maestro
    
- [ ] **RAG/Dados:** Identificar e Coletar Fontes de Dados para RAG de Estimativa Salarial (TI Brasil - para `RF-CV-005`) #ia_agente #dados #pesquisa @Maestro
    

## 🎯 A Fazer - Próxima Fase (Validação e Preparação MVP)

- [ ] **Validação Técnica: Criar Protótipo RLS FastAPI/Supabase (ERS Seção 6.1)** #tecnico #validacao #prioridade_alta #risco_alto @Maestro @AgenteMentorDevFastAPI @AgenteMentorSeguranca
    
- [ ] **Validação de Negócio: Realizar Estimativa Detalhada de Custos (API Gemini, Infraestrutura - ERS Seção 6.2)** #negocio #pesquisa #prioridade_alta @Maestro
    
- [ ] **Pesquisa Ferramentas UI:** Pesquisa e Avaliação Inicial do Google Stitch (ou similar) para Prototipagem de UI/Fluxos #ux #design #ia #ferramentas @Maestro @AgenteMentorUIDesign
    
- [ ] **Validação de UX/Valor: Criar Mockups/Protótipos Baixa Fidelidade para Validação com Usuários (Base para ERS Seção 6.3 - considerar uso de Stitch/FlutterFlow)** #ux #design #validacao #prioridade_alta @AgenteMentorUIDesign @Maestro
    
- [ ] **Validação de UX/Valor: Elaborar Roteiro de Entrevista com Usuários-Alvo (Base para ERS Seção 6.3)** #ux #pesquisa #validacao #prioridade_alta @AgenteMentorPO @Maestro
    
- [ ] **Validação de UX/Valor: Conduzir Entrevistas com Usuários-Alvo (3-5 profissionais de TI - ERS Seção 6.3)** #ux #pesquisa #validacao #prioridade_alta @Maestro
    
- [ ] **Análise Pós-Validação: Analisar Feedback das Entrevistas com Usuários e Refinar ERS/Prioridades se necessário** #ux #requisitos #validacao #prioridade_media @Maestro @AgenteMentorPO
    
- [ ] **Requisitos: Definir as 5-7 primeiras Histórias de Usuário (HUs) e Critérios de Aceite (ACs) cruciais para o MVP (Pós-Validação com Usuários)** #requisitos #agile @AgenteMentorPO @Maestro
    
- [ ] **Configuração Ferramentas - Pipedream:** Criar conta (plano gratuito) e explorar integrações básicas (ex: notificação por email para CI/CD) #configuracao #devops @Maestro
    
- [ ] **Configuração Ferramentas - FlutterFlow (Opcional):** Criar conta (se for usar para prototipagem de UI) #configuracao #ux #ui @Maestro
    
- [ ] **Configuração Ferramentas - Ambientes de Desenvolvimento:** Instalar/Verificar Python, FastAPI, Node.js (para futuro dev JS da extensão), Flutter SDK #configuracao #tecnico @Maestro
    
- [ ] **IA Agentes - Setup RAG (v1.0):**
    
    - [ ] Definir documentos iniciais para `[[08_Knowledge_Base_RAG_Sources/]]` (ERS v0.5, Plano Mestre v1.3, Guia Avançado v2.1) #ia_agente #configuracao #documentacao @Maestro
        
    - [ ] Criar script `[[scripts/rag_indexer.py]]` (v1.0 - LangChain, FAISS) #ia_agente #desenvolvimento @Maestro @AgenteMentorDevFastAPI
        
    - [ ] Realizar 1ª indexação da "Documentação Viva" #ia_agente #configuracao @Maestro
        
- [ ] **IA Agentes - Setup Trae IDE (v1.0):**
    
    - [ ] Refinar `[[.trae/rules/user_rules.md]]` e `[[.trae/rules/project_rules.md]]` para Agentes de IA #ia_agente #configuracao @Maestro
        
    - [ ] Configurar/Refinar Agente `@AgenteOrquestrador` no Trae IDE (Prompt Base Inicial) #ia_agente #configuracao #prioridade_alta @Maestro
        
    - [ ] Configurar/Refinar Agente `@AgenteMentorPO` no Trae IDE (Prompt Base Inicial) #ia_agente #configuracao #prioridade_media @Maestro
        
    - [ ] Criar template de prompt inicial para `@AgenteMentorPO` em `[[05_Prompts/Templates_Base/TPL_Gerar_HU_AC.md]]` #ia_agente #documentacao @Maestro
        
    - [ ] Configurar/Refinar Agente `@AgenteMentorDevFastAPI` no Trae IDE (Prompt Base Inicial para protótipo RLS) #ia_agente #configuracao @Maestro
        
    - [ ] Configurar/Refinar Agente `@AgenteMentorSeguranca` no Trae IDE (Prompt Base Inicial para revisão do protótipo RLS) #ia_agente #configuracao @Maestro
        
    - [ ] Configurar/Refinar Agente `@AgenteMentorUIDesign` no Trae IDE (Prompt Base Inicial para mockups) #ia_agente #configuracao @Maestro
        

## ⚙️ Em Andamento

## 🧐 Validação/Revisão

## ✅ Concluído

- [x] **Pesquisa:** Realizar "Deep Research" (Mercado, Solução, MVP, Approach) @Maestro @Gemini 📅 2025-05-29
    
- [x] **Documentação:** Atualizar `[[02_Requisitos/ERS.md]]` para v0.5 @Maestro @Gemini 📅 2025-05-29
    
- [x] **Documentação:** Atualizar `[[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]]` para v1.3 @Maestro @Gemini 📅 2025-05-29
    
- [x] **Documentação:** Atualizar `[[01_Guias_Centrais/GUIA_AVANCADO.md]]` para v2.1 @Maestro @Gemini 📅 2025-05-29
    
- [x] **Versionamento:** Fazer Commit dos 3 Guias Centrais no Git (ERS v0.5, PM v1.3, GA v2.1) @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Obsidian:** Vault configurado para o projeto Recoloca.ai @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Obsidian:** Estrutura de pastas criada (conforme Plano Mestre) @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Obsidian:** Plugin "Kanban" instalado e configurado @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Obsidian:** Plugin "Obsidian Git" instalado e configurado @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Git & GitHub/GitLab:** Repositório local inicializado @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Git & GitHub/GitLab:** Repositório remoto criado e conectado @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Trae IDE:** Instalado e configurado @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - Trae IDE:** Conexão com OpenRouter (ou APIs Gemini) estabelecida @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - OpenRouter (ou Google AI Studio):** Conta criada e chaves de API geradas @Maestro 📅 2025-05-29
    
- [x] **Configuração Ferramentas - VS Code:** IDE com extensões relevantes configurado @Maestro 📅 2025-05-29




%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[null,null,null,null,true],"move-tags":true,"move-dates":true,"show-relative-date":true,"inline-metadata-position":"body","move-task-metadata":false,"show-checkboxes":false,"new-card-insertion-method":"prepend","full-list-lane-width":false,"lane-width":400}
```
%%