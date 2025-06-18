# ESPECIFICAÇÃO DE REQUISITOS DE SOFTWARE (ERS) - VERSÃO RAG

**Documento Fonte**: `docs/02_Requisitos/01_ERS.md`
**Versão RAG**: 1.0
**Data de Conversão**: Janeiro 2025
**Prioridade RAG**: CRÍTICA
**Categoria**: Requisitos e Especificações
**Tags**: #ers #requisitos #funcionais #nao-funcionais #mvp #especificacoes

---

## CONTEXTO DO PRODUTO

### Propósito
O **Recoloca.AI** é um Micro-SaaS para auxiliar **profissionais de TI Pleno/Sênior no Brasil** no processo de recolocação profissional, atuando como **"integrador e cockpit"** que combina:
- Gerenciamento de candidaturas
- Otimização de currículos com IA
- Assistente de IA para coaching proativo

### Público-Alvo
- **Primário**: Desenvolvedores, Arquitetos, Tech Leads (Pleno/Sênior)
- **Secundário**: Profissionais de TI em transição de carreira
- **Geográfico**: Brasil (PT-BR como idioma principal)

### Diferencial Competitivo
**Coach IA proativo e contextual** que monitora progresso e oferece orientações personalizadas durante todo o processo de recolocação.

## REQUISITOS FUNCIONAIS (RF)

### RF001 - Gerenciamento de Candidaturas (Kanban)
**Prioridade**: ALTA | **Complexidade**: MÉDIA

**Descrição**: Sistema visual para organizar e acompanhar aplicações com pipeline estruturado.

**Funcionalidades**:
- Criar, editar e excluir candidaturas
- Mover candidaturas entre colunas do pipeline
- Visualização em formato Kanban
- Filtros por status, data, empresa
- Busca textual por vaga/empresa

**Pipeline Padrão**:
1. **Interessante** - Vagas identificadas
2. **Aplicado** - Candidatura enviada
3. **Em Processo** - Processo seletivo em andamento
4. **Finalizado** - Processo concluído (aprovado/rejeitado)

**Critérios de Aceitação**:
- Usuário pode criar nova candidatura com dados mínimos
- Drag & drop funcional entre colunas
- Persistência de dados em tempo real
- Interface responsiva (desktop/mobile)

### RF002 - Importação Inteligente de Vagas
**Prioridade**: ALTA | **Complexidade**: ALTA

**Descrição**: Facilidade para adicionar vagas via link com processamento por LLM.

**Funcionalidades**:
- Input de URL da vaga
- Processamento automático via LLM
- Extração de dados estruturados
- Preenchimento automático de campos
- Validação e correção manual

**Dados Extraídos**:
- Título da vaga
- Empresa
- Localização (remoto/presencial/híbrido)
- Requisitos técnicos
- Benefícios
- Faixa salarial (quando disponível)
- Descrição completa

**Critérios de Aceitação**:
- Processamento de URLs de principais job boards brasileiros
- Taxa de extração correta >85%
- Tempo de processamento <30 segundos
- Fallback para preenchimento manual

### RF003 - Otimização de Currículo com IA (MOMENTO AHA!)
**Prioridade**: CRÍTICA | **Complexidade**: ALTA

**Descrição**: Análise de adequação CV vs. vaga com sugestões contextualizadas.

**Funcionalidades**:
- Upload de currículo (PDF/DOCX)
- Análise automática CV vs. vaga específica
- Score de adequação (0-100)
- Sugestões de melhorias específicas
- Geração de versão otimizada
- Comparação lado a lado

**Métricas de Análise**:
- **Compatibilidade técnica** (skills match)
- **Experiência relevante** (anos/projetos)
- **Palavras-chave** (ATS optimization)
- **Estrutura e formatação**
- **Adequação cultural** (soft skills)

**Critérios de Aceitação**:
- Score preciso baseado em múltiplos fatores
- Sugestões específicas e acionáveis
- Geração de CV otimizado em <60 segundos
- Suporte a formatos PDF e DOCX
- Preservação de formatação original

### RF004 - Estimativa de Range Salarial com IA
**Prioridade**: MÉDIA | **Complexidade**: MÉDIA

**Descrição**: Análise da vaga para estimativa de faixa salarial baseada em dados de mercado.

**Funcionalidades**:
- Análise automática da descrição da vaga
- Estimativa de faixa salarial
- Contextualização por região/senioridade
- Comparação com dados de mercado
- Histórico de estimativas

**Fatores de Análise**:
- Senioridade da posição
- Stack tecnológico
- Localização geográfica
- Tamanho da empresa
- Benefícios oferecidos

**Critérios de Aceitação**:
- Estimativa com margem de erro <20%
- Contextualização regional (SP, RJ, etc.)
- Fonte de dados transparente
- Atualização periódica dos benchmarks

### RF005 - Coach IA Proativo
**Prioridade**: ALTA | **Complexidade**: ALTA

**Descrição**: Assistente contextual que monitora progresso e oferece orientações personalizadas.

**Funcionalidades**:
- Monitoramento automático de progresso
- Notificações proativas
- Sugestões contextualizadas
- Chat interativo
- Insights estratégicos
- Preparação para entrevistas

**Tipos de Orientação**:
- **Estratégicas**: Priorização de vagas
- **Táticas**: Otimização de aplicações
- **Preparação**: Dicas para entrevistas
- **Motivacionais**: Suporte emocional
- **Analíticas**: Insights sobre performance

**Critérios de Aceitação**:
- Notificações relevantes (não spam)
- Respostas contextualizadas ao histórico
- Interface de chat intuitiva
- Sugestões acionáveis
- Personalização baseada em perfil

### RF006 - Módulo de Métricas Pessoais
**Prioridade**: MÉDIA | **Complexidade**: BAIXA

**Descrição**: Dashboard de acompanhamento do funil de candidatura com KPIs.

**Métricas Principais**:
- **Taxa de conversão** por etapa do funil
- **Tempo médio** em cada etapa
- **Número de aplicações** por período
- **Taxa de resposta** das empresas
- **Score médio** de adequação CV
- **Evolução temporal** dos indicadores

**Visualizações**:
- Gráficos de funil
- Linha temporal de progresso
- Comparação com benchmarks
- Heatmap de atividades
- Relatórios exportáveis

**Critérios de Aceitação**:
- Dashboard responsivo e interativo
- Dados atualizados em tempo real
- Exportação em PDF/Excel
- Comparação com médias do mercado

### RF007 - Sistema de Autenticação
**Prioridade**: CRÍTICA | **Complexidade**: MÉDIA

**Funcionalidades**:
- Registro com email/senha
- Login com Google OAuth
- Recuperação de senha
- Verificação de email
- Gestão de sessões
- Logout seguro

**Critérios de Aceitação**:
- Integração com Supabase Auth
- Suporte a OAuth providers
- Sessões seguras e persistentes
- Validação robusta de dados

### RF008 - Sistema de Pagamentos (Freemium)
**Prioridade**: ALTA | **Complexidade**: MÉDIA

**Tiers de Produto**:
- **Free**: Funcionalidades básicas limitadas
- **Pro**: Acesso completo às funcionalidades
- **Enterprise**: Recursos avançados (futuro)

**Funcionalidades**:
- Integração com Stripe
- Gestão de assinaturas
- Billing automático
- Upgrade/downgrade de planos
- Histórico de pagamentos

**Critérios de Aceitação**:
- Checkout seguro via Stripe
- Ativação automática de recursos
- Gestão de ciclo de vida da assinatura
- Compliance com regulamentações

## REQUISITOS NÃO FUNCIONAIS (RNF)

### RNF001 - Performance
- **Tempo de resposta API**: <200ms para 95% das requisições
- **Tempo de carregamento inicial**: <3 segundos
- **Processamento de CV**: <60 segundos
- **Importação de vaga**: <30 segundos
- **Suporte a 1000+ usuários** simultâneos

### RNF002 - Disponibilidade
- **Uptime**: >99.5% (SLA)
- **Backup automático**: Diário
- **Recovery time**: <4 horas
- **Monitoramento**: 24/7
- **Alertas automáticos**: Para falhas críticas

### RNF003 - Segurança
- **Autenticação**: OAuth 2.0 + JWT
- **Autorização**: Row Level Security (RLS)
- **Criptografia**: TLS 1.3 em trânsito
- **Dados sensíveis**: Criptografia em repouso
- **Compliance**: LGPD
- **Auditoria**: Logs estruturados

### RNF004 - Usabilidade
- **Interface responsiva**: Desktop + Mobile
- **PWA**: Instalável e offline-capable
- **Acessibilidade**: WCAG 2.1 AA
- **Internacionalização**: PT-BR (primário)
- **Tempo para primeiro valor**: <5 minutos

### RNF005 - Escalabilidade
- **Arquitetura**: Cloud-native
- **Database**: PostgreSQL com RLS
- **API**: RESTful + OpenAPI
- **Cache**: Redis para dados frequentes
- **CDN**: Para assets estáticos

### RNF006 - Manutenibilidade
- **Cobertura de testes**: >80%
- **Documentação**: Automática via OpenAPI
- **Code quality**: Linting + Type checking
- **CI/CD**: Deploy automatizado
- **Monitoramento**: Métricas + Logs

### RNF007 - Compatibilidade
- **Browsers**: Chrome, Firefox, Safari, Edge (últimas 2 versões)
- **Mobile**: iOS 14+, Android 10+
- **Formatos de arquivo**: PDF, DOCX para CVs
- **APIs externas**: Job boards brasileiros

## RESTRIÇÕES E PREMISSAS

### Restrições Técnicas
- **Orçamento limitado**: Soluções cost-effective
- **Desenvolvimento solo**: Automação máxima
- **Compliance LGPD**: Obrigatório
- **Latência LLM**: Dependente de providers externos

### Premissas de Negócio
- **Mercado receptivo**: Profissionais TI buscam ferramentas
- **Monetização freemium**: Conversão >5%
- **Diferencial IA**: Sustentável competitivamente
- **Crescimento orgânico**: Word-of-mouth inicial

### Dependências Externas
- **Supabase**: Disponibilidade e performance
- **OpenRouter**: Acesso a LLMs
- **Stripe**: Processamento de pagamentos
- **Job boards**: APIs ou scraping permitido

## CRITÉRIOS DE ACEITAÇÃO GERAIS

### MVP (Minimum Viable Product)
- Todas as funcionalidades RF001-RF008 implementadas
- RNFs críticos atendidos (performance, segurança, usabilidade)
- Testes automatizados com cobertura >80%
- Deploy automatizado funcionando
- Documentação técnica completa

### Definição de Pronto (DoD)
- Código revisado e aprovado
- Testes unitários e integração passando
- Documentação atualizada
- Deploy em ambiente de produção
- Métricas de performance validadas

### Métricas de Sucesso
- **Técnicas**: Performance, uptime, cobertura de testes
- **Produto**: Retenção, conversão, NPS
- **Negócio**: MRR, CAC, LTV

---

**NOTA IMPORTANTE**: Esta especificação serve como contrato entre stakeholders e guia para desenvolvimento. Mudanças devem ser documentadas e aprovadas pelo Maestro, com impacto avaliado nos agentes IA e cronograma do projeto.