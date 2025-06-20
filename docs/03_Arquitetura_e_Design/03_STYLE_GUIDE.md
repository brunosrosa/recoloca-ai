---
sticker: lucide//palette
---
# STYLE GUIDE - RECOLOCA.AI

**Versão:** 1.0 (Estrutura Inicial Como MODELO - Não Aprovada)
**Data de Criação:** Junho de 2025
**Data de Última Atualização:** Junho de 2025
**Autor:** @AgenteOrquestrador
**Baseado em:** [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] v1.1, [[docs/02_Requisitos/01_ERS.md]] v1.1, [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] v1.1
**Responsável pela Evolução:** @AgenteM_UXDesigner

## 🎯 VISÃO GERAL

### Objetivo
Este Style Guide define os padrões visuais, de interação e de comunicação do Recoloca.ai, garantindo consistência em todas as interfaces e pontos de contato com o usuário, conforme requisito **RNF-USA-004** do [[docs/02_Requisitos/01_ERS.md]].

### Princípios de Design
- **Simplicidade:** Interface limpa e intuitiva para profissionais em transição de carreira
- **Confiança:** Design que transmite credibilidade e profissionalismo
- **Acessibilidade:** Conformidade com WCAG 2.1 Nível AA (RNF-USA-003)
- **Responsividade:** Experiência consistente em todos os dispositivos
- **Orientação a Resultados:** Foco na jornada de recolocação profissional

---

## 🎨 IDENTIDADE VISUAL

### Paleta de Cores

#### Cores Primárias
```css
/* A ser definido pelo @AgenteM_UXDesigner */
--primary-blue: #[HEX]; /* Cor principal - confiança e profissionalismo */
--primary-green: #[HEX]; /* Sucesso e crescimento profissional */
--primary-dark: #[HEX]; /* Textos principais e elementos de destaque */
```

#### Cores Secundárias
```css
/* A ser definido pelo @AgenteM_UXDesigner */
--secondary-light: #[HEX]; /* Backgrounds e áreas de destaque */
--secondary-gray: #[HEX]; /* Textos secundários e divisores */
--accent-orange: #[HEX]; /* CTAs e elementos de ação */
```

#### Cores de Sistema
```css
/* A ser definido pelo @AgenteM_UXDesigner */
--success: #[HEX]; /* Feedback positivo */
--warning: #[HEX]; /* Alertas e atenção */
--error: #[HEX]; /* Erros e validações */
--info: #[HEX]; /* Informações neutras */
```

### Tipografia

#### Fonte Principal
```css
/* A ser definido pelo @AgenteM_UXDesigner */
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

---

## 🧩 COMPONENTES DE INTERFACE

### Botões

#### Primários
- **Uso:** Ações principais ("Analisar CV", "Salvar Perfil")
- **Estilo:** [A ser definido]
- **Estados:** Default, Hover, Active, Disabled, Loading

#### Secundários
- **Uso:** Ações secundárias ("Cancelar", "Voltar")
- **Estilo:** [A ser definido]
- **Estados:** Default, Hover, Active, Disabled

#### Terciários
- **Uso:** Ações de baixa prioridade
- **Estilo:** [A ser definido]

### Formulários

#### Campos de Input
- **Estados:** Default, Focus, Error, Success, Disabled
- **Validação:** Feedback em tempo real
- **Labels:** Sempre visíveis e descritivas
- **Placeholders:** Exemplos práticos, não instruções

#### Dropdowns e Seletores
- **Estilo:** [A ser definido]
- **Comportamento:** [A ser definido]

### Cards e Containers
- **Elevação:** Sombras sutis para hierarquia
- **Bordas:** [A ser definido]
- **Espaçamento interno:** [A ser definido]

### Navegação

#### Menu Principal
- **Estrutura:** [A ser definida]
- **Estados:** Active, Hover, Default

#### Breadcrumbs
- **Uso:** Navegação em fluxos complexos
- **Estilo:** [A ser definido]

### Feedback e Estados

#### Loading States
- **Spinners:** Para carregamentos rápidos (<3s)
- **Progress Bars:** Para processos longos (análise de CV)
- **Skeleton Screens:** Para carregamento de conteúdo

#### Mensagens de Sistema
- **Success:** Confirmações de ações
- **Error:** Erros e validações
- **Warning:** Alertas importantes
- **Info:** Informações neutras

---

## 📱 RESPONSIVIDADE E LAYOUT

### Breakpoints
```css
/* A ser definido pelo @AgenteM_UXDesigner */
--mobile: 320px;
--tablet: 768px;
--desktop: 1024px;
--large: 1440px;
```

### Grid System
- **Colunas:** [A ser definido]
- **Gutters:** [A ser definido]
- **Margens:** [A ser definido]

### Espaçamento
```css
/* Sistema de espaçamento baseado em múltiplos de 8px */
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
```

---

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

---

## ♿ ACESSIBILIDADE

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

---

## 💻 PADRÕES DE CÓDIGO

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

---

## 🔄 ANIMAÇÕES E TRANSIÇÕES

### Princípios
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

---

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

---

## 🧪 TESTES E VALIDAÇÃO

### Testes de Usabilidade
- **Critérios:** Baseados nas heurísticas de Nielsen
- **Métricas:** Task completion rate, time on task, error rate
- **Ferramentas:** [A ser definido]

### Testes de Acessibilidade
- **Automáticos:** axe-core, WAVE
- **Manuais:** Navegação por teclado, screen readers
- **Validação:** WCAG 2.1 AA compliance

### Testes Visuais
- **Cross-browser:** Chrome, Firefox, Safari, Edge
- **Dispositivos:** Mobile, tablet, desktop
- **Ferramentas:** [A ser definido]

---

## 📚 RECURSOS E REFERÊNCIAS

### Documentação Relacionada
- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.1) - Visão e objetivos
- [[docs/02_Requisitos/01_ERS.md]] (v1.1) - Requisitos de usabilidade
- [[docs/02_Requisitos/02_HU_AC/HU_MVP_Jornada_Usuario.md]] - Jornada do usuário
- [[docs/03_Arquitetura_e_Design/01_HLD.md]] (v1.1) - Arquitetura de alto nível
- [[docs/04_Agentes_IA/02_Perfis/@AgenteM_UXDesigner.md]] - Responsável pela evolução

### Ferramentas de Design
- **Prototipagem:** [A ser definido]
- **Design System:** [A ser definido]
- **Colaboração:** [A ser definido]

### Inspirações e Benchmarks
- **Plataformas de Carreira:** LinkedIn, Indeed, Glassdoor
- **SaaS B2C:** [A ser pesquisado pelo @AgenteM_UXDesigner]
- **Design Systems:** Material Design, Human Interface Guidelines

---

## 🔄 PROCESSO DE EVOLUÇÃO

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

---

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

---

## 🚀 PRÓXIMOS PASSOS

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

---

**Nota:** Este documento serve como estrutura inicial para o Style Guide do Recoloca.ai. O @AgenteM_UXDesigner é responsável por evoluir e detalhar cada seção, garantindo alinhamento com os objetivos do projeto e as melhores práticas de UX/UI.

**Status:** 🟡 Estrutura criada - Aguardando desenvolvimento pelo @AgenteM_UXDesigner

--- FIM DO DOCUMENTO STYLE_GUIDE.md (v1.0) ---