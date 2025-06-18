---
**RAG_METADATA**:
**Documento Fonte**: `docs/03_Arquitetura_e_Design/03_STYLE_GUIDE.md`
**Versão RAG**: 1.0
**Data de Conversão**: Janeiro 2025
**Prioridade RAG**: ALTA
**Categoria**: UX e Design
**Tags**: #style-guide #design-system #ui-ux #identidade-visual #componentes #acessibilidade

---

# STYLE GUIDE RECOLOCA.AI - VERSÃO RAG

## CONTEXTO E OBJETIVOS

### Propósito do Style Guide
Definir **padrões visuais, de interação e comunicação** do Recoloca.ai, garantindo **consistência** em todas as interfaces e pontos de contato com o usuário.

### Princípios de Design Fundamentais
- **Simplicidade**: Interface limpa e intuitiva para profissionais em transição
- **Confiança**: Design que transmite credibilidade e profissionalismo
- **Acessibilidade**: Conformidade com WCAG 2.1 Nível AA (RNF-USA-003)
- **Responsividade**: Experiência consistente em todos os dispositivos
- **Orientação a Resultados**: Foco na jornada de recolocação profissional

### Público-Alvo
**Profissionais de TI Pleno/Sênior** em processo de recolocação profissional, que valorizam:
- Eficiência e produtividade
- Credibilidade e profissionalismo
- Facilidade de uso
- Resultados mensuráveis

## IDENTIDADE VISUAL

### Paleta de Cores

#### Cores Primárias
```css
/* Definição pelo @AgenteM_UXDesigner */
--primary-blue: #[HEX];     /* Confiança e profissionalismo */
--primary-green: #[HEX];    /* Sucesso e crescimento profissional */
--primary-dark: #[HEX];     /* Textos principais e elementos de destaque */
```

#### Cores Secundárias
```css
--secondary-light: #[HEX];  /* Backgrounds e áreas de destaque */
--secondary-gray: #[HEX];   /* Textos secundários e divisores */
--accent-orange: #[HEX];    /* CTAs e elementos de ação */
```

#### Cores de Sistema
```css
--success: #[HEX];          /* Feedback positivo */
--warning: #[HEX];          /* Alertas e atenção */
--error: #[HEX];            /* Erros e validações */
--info: #[HEX];             /* Informações neutras */
```

### Sistema Tipográfico

#### Fonte Principal
```css
font-family: '[FONTE_PRINCIPAL]', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

#### Hierarquia Tipográfica
- **H1 (Títulos Principais)**: 32px/2rem - Páginas principais
- **H2 (Títulos de Seção)**: 24px/1.5rem - Seções importantes
- **H3 (Subtítulos)**: 20px/1.25rem - Subsecções
- **Body (Texto Principal)**: 16px/1rem - Conteúdo geral
- **Small (Textos Auxiliares)**: 14px/0.875rem - Informações secundárias
- **Caption (Legendas)**: 12px/0.75rem - Metadados e legendas

#### Pesos e Estilos
- **Regular (400)**: Texto padrão
- **Medium (500)**: Destaque moderado
- **Semibold (600)**: Títulos e elementos importantes
- **Bold (700)**: Ênfase máxima

### Iconografia

#### Especificações
- **Biblioteca**: [A definir - Lucide, Heroicons, Material Icons]
- **Estilo**: Outline/Filled consistente
- **Tamanhos Padrão**: 16px, 20px, 24px, 32px
- **Uso**: Sempre com labels para acessibilidade quando necessário

#### Contextos de Uso
- **Navegação**: Ícones de menu e navegação
- **Ações**: Botões e controles interativos
- **Status**: Indicadores de estado e feedback
- **Conteúdo**: Ilustração de conceitos e categorias

### Logotipo e Marca

#### Versões da Marca
- **Principal**: Uso padrão em fundos claros
- **Monocromática**: Para aplicações especiais
- **Simplificada**: Para espaços reduzidos
- **Horizontal/Vertical**: Adaptações de layout

#### Diretrizes de Uso
- **Área de Proteção**: [A ser definida pelo @AgenteM_UXDesigner]
- **Tamanhos Mínimos**: [A ser especificado]
- **Usos Incorretos**: [A ser documentado]

## SISTEMA DE COMPONENTES

### Botões

#### Botões Primários
- **Uso**: Ações principais ("Analisar CV", "Salvar Perfil")
- **Características**: Destaque visual máximo
- **Estados**: Default, Hover, Active, Disabled, Loading
- **Acessibilidade**: Contraste mínimo 4.5:1

#### Botões Secundários
- **Uso**: Ações secundárias ("Cancelar", "Voltar")
- **Características**: Menos destaque que primários
- **Estados**: Default, Hover, Active, Disabled

#### Botões Terciários
- **Uso**: Ações de baixa prioridade
- **Características**: Mínimo destaque visual
- **Estados**: Default, Hover, Active, Disabled

### Formulários

#### Campos de Entrada
- **Input Text**: Entrada de texto simples
- **Textarea**: Texto longo e descrições
- **Select**: Seleção de opções
- **Checkbox**: Seleção múltipla
- **Radio**: Seleção única
- **File Upload**: Upload de arquivos (CVs)

#### Estados dos Campos
- **Default**: Estado padrão
- **Focus**: Campo ativo
- **Error**: Validação com erro
- **Success**: Validação bem-sucedida
- **Disabled**: Campo inativo

#### Validação e Feedback
- **Mensagens de Erro**: Claras e acionáveis
- **Mensagens de Sucesso**: Confirmação de ações
- **Indicadores de Progresso**: Para processos longos
- **Tooltips**: Ajuda contextual

### Navegação

#### Menu Principal
- **Desktop**: Navegação horizontal
- **Mobile**: Menu hambúrguer
- **Estados**: Ativo, Inativo, Hover

#### Breadcrumbs
- **Uso**: Navegação hierárquica
- **Formato**: Home > Seção > Página Atual
- **Interatividade**: Links clicáveis

#### Paginação
- **Controles**: Anterior, Próximo, Números
- **Estados**: Ativo, Inativo, Disabled
- **Responsividade**: Adaptação para mobile

### Cards e Containers

#### Cards de Conteúdo
- **Estrutura**: Header, Body, Footer (opcional)
- **Sombras**: Elevação sutil
- **Bordas**: Raio consistente
- **Hover**: Feedback visual

#### Modais e Overlays
- **Backdrop**: Escurecimento do fundo
- **Posicionamento**: Centralizado
- **Fechamento**: X, ESC, clique fora
- **Acessibilidade**: Focus trap

### Feedback e Status

#### Notificações
- **Toast**: Mensagens temporárias
- **Alerts**: Avisos importantes
- **Banners**: Informações persistentes
- **Badges**: Indicadores de status

#### Loading States
- **Spinners**: Carregamento geral
- **Skeleton**: Placeholder de conteúdo
- **Progress Bars**: Progresso específico
- **Lazy Loading**: Carregamento progressivo

## PADRÕES DE INTERAÇÃO

### Micro-interações
- **Hover Effects**: Feedback visual sutil
- **Transitions**: Animações suaves (300ms)
- **Focus States**: Indicação clara de foco
- **Loading States**: Feedback de processamento

### Gestos e Controles
- **Click/Tap**: Ação primária
- **Hover**: Preview e feedback
- **Drag & Drop**: Reorganização (quando aplicável)
- **Keyboard Navigation**: Suporte completo

### Responsividade

#### Breakpoints
```css
/* Mobile First */
--mobile: 320px;
--tablet: 768px;
--desktop: 1024px;
--large: 1440px;
```

#### Adaptações
- **Layout**: Grid flexível
- **Tipografia**: Escala responsiva
- **Componentes**: Adaptação contextual
- **Imagens**: Otimização por dispositivo

## ACESSIBILIDADE (WCAG 2.1 AA)

### Contraste e Cores
- **Contraste Mínimo**: 4.5:1 para texto normal
- **Contraste Aprimorado**: 7:1 para texto pequeno
- **Não Dependência de Cor**: Informação não apenas por cor

### Navegação por Teclado
- **Tab Order**: Sequência lógica
- **Focus Visible**: Indicação clara
- **Skip Links**: Pular para conteúdo principal
- **Atalhos**: Teclas de acesso rápido

### Tecnologias Assistivas
- **Screen Readers**: Suporte completo
- **ARIA Labels**: Descrições adequadas
- **Semantic HTML**: Estrutura semântica
- **Alt Text**: Descrição de imagens

### Testes de Acessibilidade
- **Ferramentas**: axe-core, WAVE, Lighthouse
- **Testes Manuais**: Navegação por teclado
- **Usuários Reais**: Testes com pessoas com deficiência

## DIRETRIZES DE CONTEÚDO

### Tom de Voz
- **Profissional**: Credível e competente
- **Empático**: Compreensivo com desafios de recolocação
- **Direto**: Comunicação clara e objetiva
- **Motivacional**: Encorajador e positivo

### Linguagem
- **Clareza**: Evitar jargões desnecessários
- **Consistência**: Terminologia padronizada
- **Ação**: Verbos no imperativo para CTAs
- **Inclusividade**: Linguagem neutra e inclusiva

### Estrutura de Conteúdo
- **Hierarquia**: Informação mais importante primeiro
- **Escaneabilidade**: Fácil de percorrer rapidamente
- **Chunks**: Informação em blocos digestíveis
- **Call-to-Actions**: Claros e específicos

## IMPLEMENTAÇÃO E MANUTENÇÃO

### Ferramentas de Design
- **Design System**: [A definir - Figma, Sketch]
- **Tokens**: Variáveis de design centralizadas
- **Componentes**: Biblioteca reutilizável
- **Documentação**: Guias de uso

### Desenvolvimento
- **CSS Framework**: [A definir - Tailwind, Material-UI]
- **Component Library**: Componentes reutilizáveis
- **Storybook**: Documentação de componentes
- **Testes Visuais**: Regressão visual automatizada

### Evolução do Style Guide
- **Versionamento**: Controle de versões
- **Feedback**: Coleta de feedback de usuários
- **Iteração**: Melhorias contínuas
- **Documentação**: Manutenção da documentação

## MÉTRICAS E VALIDAÇÃO

### KPIs de Design
- **Usabilidade**: Taxa de conclusão de tarefas
- **Satisfação**: Net Promoter Score (NPS)
- **Eficiência**: Tempo para completar ações
- **Acessibilidade**: Conformidade WCAG

### Testes de Usuário
- **A/B Testing**: Comparação de variações
- **Usability Testing**: Testes de usabilidade
- **Accessibility Testing**: Testes de acessibilidade
- **Performance**: Métricas de performance

## REFERÊNCIAS CRUZADAS

### Documentos Relacionados
- `[[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]]` - Visão estratégica
- `[[docs/02_Requisitos/01_ERS.md]]` - Requisitos de usabilidade
- `[[docs/03_Arquitetura_e_Design/01_HLD.md]]` - Arquitetura do sistema
- `[[docs/04_Agentes_IA/01_Perfis/@AgenteM_UXDesigner.md]]` - Responsável pela evolução

### Próximos Passos
- Definição completa da paleta de cores
- Seleção da fonte principal
- Criação da biblioteca de ícones
- Desenvolvimento dos componentes base
- Implementação do design system

---

**NOTA RAG**: Este Style Guide serve como referência fundamental para decisões de design e implementação de interface, garantindo consistência visual e experiência de usuário otimizada para o público-alvo do Recoloca.ai.