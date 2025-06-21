---
rag_priority: CRITICAL
rag_category: design_system
rag_keywords: ["style guide", "design system", "UI/UX", "componentes", "paleta cores", "tipografia", "acessibilidade", "responsividade", "Flutter", "CSS", "WCAG", "animações", "microcopy", "tom de voz"]
rag_context: "Guia de estilo e design system do Recoloca.ai - padrões visuais, componentes, acessibilidade e diretrizes de implementação"
rag_agents: ["@AgenteM_UXDesigner", "@AgenteMentorDevFlutter", "@AgenteMentorDevJS", "@AgenteOrquestrador"]
rag_related_docs: ["PLANO_MESTRE_RECOLOCA_AI", "ERS", "HLD", "GUIA_AVANCADO"]
rag_version: "1.0"
rag_last_update: "2025-06-27"
---

# STYLE GUIDE - RECOLOCA.AI (Versão RAG)

## 📋 INFORMAÇÕES DO DOCUMENTO

**Versão Original:** 1.0 (Estrutura Inicial)
**Versão RAG:** 1.0
**Data de Criação:** Junho de 2025
**Data de Última Atualização:** Junho de 2025
**Autor:** @AgenteOrquestrador
**Responsável pela Evolução:** @AgenteM_UXDesigner
**Baseado em:** PLANO_MESTRE_RECOLOCA_AI v1.1, ERS v1.1, GUIA_AVANCADO v1.1

## 🎯 VISÃO GERAL E PRINCÍPIOS

### Objetivo Principal
Definir padrões visuais, de interação e comunicação do Recoloca.ai, garantindo consistência em todas as interfaces e pontos de contato com o usuário, conforme requisito **RNF-USA-004** do ERS.

### Princípios de Design Fundamentais
- **Simplicidade:** Interface limpa e intuitiva para profissionais em transição de carreira
- **Confiança:** Design que transmite credibilidade e profissionalismo
- **Acessibilidade:** Conformidade com WCAG 2.1 Nível AA (RNF-USA-003)
- **Responsividade:** Experiência consistente em todos os dispositivos
- **Orientação a Resultados:** Foco na jornada de recolocação profissional

## 🎨 SISTEMA DE IDENTIDADE VISUAL

### Paleta de Cores (A ser definida pelo @AgenteM_UXDesigner)

#### Cores Primárias
```css
--primary-blue: #[HEX]; /* Cor principal - confiança e profissionalismo */
--primary-green: #[HEX]; /* Sucesso e crescimento profissional */
--primary-dark: #[HEX]; /* Textos principais e elementos de destaque */
```

#### Cores Secundárias
```css
--secondary-light: #[HEX]; /* Backgrounds e áreas de destaque */
--secondary-gray: #[HEX]; /* Textos secundários e divisores */
--accent-orange: #[HEX]; /* CTAs e elementos de ação */
```

#### Cores de Sistema
```css
--success: #[HEX]; /* Feedback positivo */
--warning: #[HEX]; /* Alertas e atenção */
--error: #[HEX]; /* Erros e validações */
--info: #[HEX]; /* Informações neutras */
```

### Sistema Tipográfico

#### Fonte Principal
```css
font-family: '[FONTE_PRINCIPAL]', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

#### Hierarquia Tipográfica
- **H1:** Títulos principais (32px/2rem)
- **H2:** Títulos de seção (24px/1.5rem)
- **H3:** Subtítulos (20px/1.25rem)
- **Body:** Texto principal (16px/1rem)
- **Small:** Textos auxiliares (14px/0.875rem)
- **Caption:** Legendas e metadados (12px/0.75rem)

### Iconografia
- **Biblioteca:** [A ser definida - ex: Lucide, Heroicons, Material Icons]
- **Estilo:** Outline/Filled consistente
- **Tamanhos:** 16px, 20px, 24px, 32px
- **Uso:** Sempre acompanhados de labels quando necessário para acessibilidade

### Logotipo e Marca
- **Versões:** Principal, monocromática, simplificada
- **Área de Proteção:** [A ser definida]
- **Usos Incorretos:** [A ser documentado]

## 🧩 BIBLIOTECA DE COMPONENTES

### Sistema de Botões

#### Botões Primários
- **Uso:** Ações principais ("Analisar CV", "Salvar Perfil")
- **Estados:** Default, Hover, Active, Disabled, Loading
- **Estilo:** [A ser definido pelo @AgenteM_UXDesigner]

#### Botões Secundários
- **Uso:** Ações secundárias ("Cancelar", "Voltar")
- **Estados:** Default, Hover, Active, Disabled
- **Estilo:** [A ser definido pelo @AgenteM_UXDesigner]

#### Botões Terciários
- **Uso:** Ações de baixa prioridade
- **Estados:** Default, Hover, Active, Disabled

### Sistema de Formulários

#### Campos de Input
- **Estados:** Default, Focus, Error, Success, Disabled
- **Validação:** Feedback em tempo real
- **Labels:** Sempre visíveis e descritivas
- **Placeholders:** Exemplos práticos, não instruções

#### Dropdowns e Seletores
- **Estilo:** [A ser definido pelo @AgenteM_UXDesigner]
- **Comportamento:** [A ser definido pelo @AgenteM_UXDesigner]

### Cards e Containers
- **Elevação:** Sombras sutis para hierarquia
- **Bordas:** [A ser definido pelo @AgenteM_UXDesigner]
- **Espaçamento interno:** [A ser definido pelo @AgenteM_UXDesigner]

### Sistema de Navegação

#### Menu Principal
- **Estrutura:** [A ser definida pelo @AgenteM_UXDesigner]
- **Estados:** Active, Hover, Default

#### Breadcrumbs
- **Uso:** Navegação em fluxos complexos
- **Estilo:** [A ser definido pelo @AgenteM_UXDesigner]

### Feedback e Estados do Sistema

#### Loading States
- **Spinners:** Para carregamentos rápidos (<3s)
- **Progress Bars:** Para processos longos (análise de CV)
- **Skeleton Screens:** Para carregamento de conteúdo

#### Mensagens de Sistema
- **Success:** Confirmações de ações
- **Error:** Erros e validações
- **Warning:** Alertas importantes
- **Info:** Informações neutras

## 📱 SISTEMA RESPONSIVO E LAYOUT

### Breakpoints
```css
--mobile: 320px;
--tablet: 768px;
--desktop: 1024px;
--large: 1440px;
```

### Grid System
- **Colunas:** [A ser definido pelo @AgenteM_UXDesigner]
- **Gutters:** [A ser definido pelo @AgenteM_UXDesigner]
- **Margens:** [A ser definido pelo @AgenteM_UXDesigner]

### Sistema de Espaçamento
```css
/* Sistema baseado em múltiplos de 8px */
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
```

## ✍️ TOM DE VOZ E COMUNICAÇÃO

### Personalidade da Marca
- **Profissional:** Linguagem técnica quando necessário, mas acessível
- **Empático:** Compreende os desafios da recolocação profissional
- **Motivador:** Foca em oportunidades e crescimento
- **Direto:** Comunicação clara e objetiva
- **Confiável:** Informações precisas e baseadas em dados

### Diretrizes de Escrita

#### Linguagem
- **Pessoa:** Segunda pessoa ("você") para proximidade
- **Tempo verbal:** Presente e futuro próximo
- **Formalidade:** Profissional, mas acessível
- **Jargões:** Evitar ou explicar quando necessário

#### Mensagens de Interface

##### Títulos e CTAs
- **Títulos:** Claros e orientados a ação
- **CTAs:** Verbos de ação específicos ("Analisar CV", "Encontrar Vagas")
- **Evitar:** "Clique aqui", "Saiba mais" genérico

##### Feedback ao Usuário
- **Sucesso:** "CV analisado com sucesso! Veja suas recomendações."
- **Erro:** "Não foi possível processar seu CV. Tente novamente."
- **Loading:** "Analisando seu CV... Isso pode levar alguns minutos."

##### Textos de Ajuda
- **Tooltips:** Explicações concisas
- **Placeholders:** Exemplos práticos
- **Instruções:** Passo a passo quando necessário

### Microcopy
- **Labels de formulário:** Descritivos e específicos
- **Mensagens de validação:** Construtivas, não punitivas
- **Estados vazios:** Orientações claras sobre próximos passos

## ♿ DIRETRIZES DE ACESSIBILIDADE

### Conformidade WCAG 2.1 AA
- **Contraste:** Mínimo 4.5:1 para texto normal, 3:1 para texto grande
- **Foco:** Indicadores visuais claros para navegação por teclado
- **Alt Text:** Descrições significativas para imagens
- **Labels:** Associações corretas entre labels e inputs

### Navegação por Teclado
- **Tab Order:** Lógica e intuitiva
- **Skip Links:** Para conteúdo principal
- **Atalhos:** Documentados e consistentes

### Tecnologias Assistivas
- **Screen Readers:** Estrutura semântica correta
- **ARIA Labels:** Quando necessário para clareza
- **Landmarks:** Navegação estruturada

## 💻 PADRÕES DE IMPLEMENTAÇÃO

### Flutter/Dart

#### Nomenclatura de Widgets
```dart
// Padrão: [Funcionalidade][Tipo]Widget
class CVAnalysisCardWidget extends StatelessWidget {}
class JobRecommendationListWidget extends StatelessWidget {}
```

#### Estrutura de Arquivos
```
lib/
├── widgets/
│   ├── common/          # Componentes reutilizáveis
│   ├── forms/           # Componentes de formulário
│   └── cards/           # Componentes de card
├── themes/
│   ├── app_theme.dart   # Tema principal
│   ├── colors.dart      # Paleta de cores
│   └── typography.dart  # Tipografia
```

#### Padrões de Estilo
```dart
// Usar ThemeData para consistência
class AppTheme {
  static ThemeData get lightTheme => ThemeData(
    primarySwatch: AppColors.primaryBlue,
    textTheme: AppTypography.textTheme,
    // ...
  );
}
```

### CSS/SCSS (Para extensão Chrome)

#### Nomenclatura BEM
```css
/* Bloco__Elemento--Modificador */
.cv-analysis__button--primary {}
.job-card__title--highlighted {}
```

#### Variáveis CSS
```css
:root {
  /* Cores */
  --color-primary: #[HEX];
  --color-secondary: #[HEX];
  
  /* Espaçamento */
  --space-sm: 8px;
  --space-md: 16px;
  
  /* Tipografia */
  --font-size-body: 16px;
  --font-weight-medium: 500;
}
```

## 🔄 SISTEMA DE ANIMAÇÕES E TRANSIÇÕES

### Princípios de Animação
- **Sutileza:** Animações devem auxiliar, não distrair
- **Performance:** 60fps em dispositivos móveis
- **Propósito:** Cada animação deve ter uma função clara
- **Duração:** 200-300ms para micro-interações, até 500ms para transições maiores

### Tipos de Animação

#### Micro-interações
- **Hover:** Mudanças sutis de cor/escala
- **Focus:** Indicadores visuais suaves
- **Loading:** Spinners e progress indicators

#### Transições de Página
- **Slide:** Para navegação sequencial
- **Fade:** Para mudanças de contexto
- **Scale:** Para modais e overlays

### Easing Functions
```css
/* Padrões recomendados */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
```

## 📐 ESPECIFICAÇÕES TÉCNICAS

### Imagens e Assets

#### Formatos
- **Ícones:** SVG (vetorial, escalável)
- **Fotos:** WebP com fallback JPEG
- **Ilustrações:** SVG ou PNG com transparência

#### Otimização
- **Compressão:** Máximo 80% qualidade para JPEG
- **Dimensões:** Múltiplas resoluções para responsividade
- **Lazy Loading:** Para imagens abaixo da dobra

### Performance
- **Tamanho de Bundle:** Monitorar e otimizar
- **Critical CSS:** Inline para above-the-fold
- **Font Loading:** Estratégia de carregamento otimizada

## 🧪 ESTRATÉGIA DE TESTES E VALIDAÇÃO

### Testes de Usabilidade
- **Critérios:** Baseados nas heurísticas de Nielsen
- **Métricas:** Task completion rate, time on task, error rate
- **Ferramentas:** [A ser definido pelo @AgenteM_UXDesigner]

### Testes de Acessibilidade
- **Automáticos:** axe-core, WAVE
- **Manuais:** Navegação por teclado, screen readers
- **Validação:** WCAG 2.1 AA compliance

### Testes Visuais
- **Cross-browser:** Chrome, Firefox, Safari, Edge
- **Dispositivos:** Mobile, tablet, desktop
- **Ferramentas:** [A ser definido pelo @AgenteM_UXDesigner]

## 📊 MÉTRICAS DE SUCESSO

### KPIs de Usabilidade
- **Task Completion Rate:** >90% para fluxos principais
- **Time on Task:** Redução de 20% após otimizações
- **Error Rate:** <5% em formulários críticos
- **User Satisfaction:** Score >4.0/5.0

### Métricas de Acessibilidade
- **WCAG Compliance:** 100% AA
- **Keyboard Navigation:** 100% funcional
- **Screen Reader Compatibility:** Testado e validado

### Métricas Técnicas
- **Performance Score:** >90 no Lighthouse
- **Bundle Size:** Monitoramento contínuo
- **Cross-browser Compatibility:** >95% dos usuários

## 🔄 PROCESSO DE EVOLUÇÃO E GOVERNANÇA

### Responsabilidades
- **@AgenteM_UXDesigner:** Evolução e manutenção do Style Guide
- **@AgenteMentorDevFlutter:** Implementação em Flutter
- **@AgenteMentorDevJS:** Implementação na extensão Chrome
- **@AgenteOrquestrador:** Validação estratégica e alinhamento

### Versionamento
- **Versão Atual:** 1.0 (Estrutura Inicial)
- **Próxima Versão:** 1.1 (Definições visuais completas)
- **Critérios de Atualização:** Feedback de usuários, testes de usabilidade, evolução do produto

### Processo de Aprovação
1. **Proposta:** @AgenteM_UXDesigner cria proposta de mudança
2. **Revisão:** @AgenteOrquestrador valida alinhamento estratégico
3. **Aprovação:** Maestro aprova mudanças
4. **Implementação:** Agentes de desenvolvimento implementam
5. **Validação:** Testes e feedback

## 🚀 ROADMAP DE IMPLEMENTAÇÃO

### Fase 1: Definições Visuais (Semana 4-5)
- [ ] Definir paleta de cores completa
- [ ] Escolher e configurar tipografia
- [ ] Criar biblioteca de ícones
- [ ] Definir componentes básicos

### Fase 2: Implementação (Semana 6-8)
- [ ] Implementar tema Flutter
- [ ] Criar componentes reutilizáveis
- [ ] Documentar padrões de código
- [ ] Testes de usabilidade iniciais

### Fase 3: Refinamento (Pós-MVP)
- [ ] Feedback de usuários reais
- [ ] Otimizações baseadas em dados
- [ ] Expansão do design system
- [ ] Documentação avançada

## 📚 RECURSOS E REFERÊNCIAS

### Documentação Relacionada
- **PLANO_MESTRE_RECOLOCA_AI** (v1.1) - Visão e objetivos
- **ERS** (v1.1) - Requisitos de usabilidade
- **HU_MVP_Jornada_Usuario** - Jornada do usuário
- **HLD** (v1.1) - Arquitetura de alto nível
- **@AgenteM_UXDesigner** - Responsável pela evolução

### Ferramentas de Design
- **Prototipagem:** [A ser definido pelo @AgenteM_UXDesigner]
- **Design System:** [A ser definido pelo @AgenteM_UXDesigner]
- **Colaboração:** [A ser definido pelo @AgenteM_UXDesigner]

### Inspirações e Benchmarks
- **Plataformas de Carreira:** LinkedIn, Indeed, Glassdoor
- **SaaS B2C:** [A ser pesquisado pelo @AgenteM_UXDesigner]
- **Design Systems:** Material Design, Human Interface Guidelines

## 🎯 CONTEXTO PARA AGENTES IA

### Para @AgenteM_UXDesigner
- **Prioridade:** Completar definições visuais (cores, tipografia, componentes)
- **Foco:** Criar sistema coeso e acessível
- **Entregáveis:** Paleta de cores, biblioteca de componentes, protótipos

### Para @AgenteMentorDevFlutter
- **Prioridade:** Implementar tema e componentes Flutter
- **Foco:** Seguir padrões definidos no Style Guide
- **Entregáveis:** ThemeData, widgets reutilizáveis, documentação de código

### Para @AgenteMentorDevJS
- **Prioridade:** Implementar CSS/SCSS para extensão Chrome
- **Foco:** Consistência visual com app Flutter
- **Entregáveis:** Variáveis CSS, componentes, nomenclatura BEM

### Para @AgenteOrquestrador
- **Prioridade:** Validar alinhamento estratégico
- **Foco:** Garantir que design suporte objetivos de negócio
- **Entregáveis:** Aprovações, feedback estratégico, priorização

## 📋 STATUS ATUAL

**Status:** 🟡 Estrutura criada - Aguardando desenvolvimento pelo @AgenteM_UXDesigner

**Próximas Ações Críticas:**
1. @AgenteM_UXDesigner definir paleta de cores
2. @AgenteM_UXDesigner escolher tipografia
3. @AgenteM_UXDesigner criar componentes básicos
4. @AgenteMentorDevFlutter implementar tema Flutter
5. @AgenteMentorDevJS implementar CSS para extensão

---

**IMPORTANTE PARA AGENTES:** Este Style Guide é a fonte única de verdade para todas as decisões de design e implementação visual do Recoloca.ai. Sempre consulte este documento antes de criar ou modificar componentes de interface.

--- FIM DO DOCUMENTO STYLE_GUIDE_para_RAG.md (v1.0) ---