---
# RAG Metadata
document_type: "design_system"
project: "Recoloca.AI"
version: "1.0"
last_updated: "2025-06-18"
rag_keywords: ["style guide", "design system", "ui components", "visual identity", "brand guidelines", "color palette", "typography", "iconography", "layout patterns", "interaction design", "accessibility", "responsive design"]
related_documents: [
  "ESTRATEGIA_MOMENTO_AHA_para_RAG.md",
  "HLD_para_RAG.md",
  "ERS_para_RAG.md",
  "AGENTES_IA_MENTORES_OVERVIEW_para_RAG.md"
]
cross_references: [
  "design system", "visual identity", "brand guidelines", "ui components",
  "color palette", "typography system", "iconography", "layout patterns",
  "interaction design", "accessibility standards", "responsive design",
  "flutter components", "pwa design", "mobile first"
]
---

# STYLE GUIDE - RECOLOCA.AI

## Informações do Documento
- **Versão**: 1.0
- **Data de Criação**: 18 de junho de 2025
- **Data de Última Atualização**: 18 de junho de 2025
- **Autor**: @AgenteM_UXDesigner (com supervisão do Maestro Bruno S. Rosa)
- **Contexto**: Padrões visuais, de interação e comunicação para Recoloca.ai
- **Baseado em**: ESTRATEGIA_MOMENTO_AHA v1.0+, HLD v1.0+, ERS v1.0+

## 🎯 INTRODUÇÃO E PROPÓSITO

### Objetivo do Style Guide
Este documento define os **padrões visuais, de interação e comunicação** para o Recoloca.ai, garantindo **consistência** em todas as interfaces e pontos de contato com o usuário. Serve como referência única para desenvolvedores, designers e stakeholders.

### Princípios de Design

#### **1. Clareza e Simplicidade**
- Interface limpa e intuitiva
- Hierarquia visual clara
- Redução de ruído visual
- Foco na experiência do usuário

#### **2. Profissionalismo e Confiança**
- Visual corporativo moderno
- Credibilidade através do design
- Consistência em todos os touchpoints
- Qualidade premium percebida

#### **3. Acessibilidade e Inclusão**
- Conformidade com WCAG 2.1 AA
- Design inclusivo para todos os usuários
- Suporte a tecnologias assistivas
- Contraste adequado e legibilidade

#### **4. Responsividade e Adaptabilidade**
- Mobile-first approach
- Adaptação fluida a diferentes dispositivos
- Performance otimizada
- Progressive Web App (PWA) ready

## 🎨 IDENTIDADE VISUAL

### Paleta de Cores

#### **Cores Primárias**
```css
/* Azul Principal - Confiança e Profissionalismo */
--primary-blue: #2563EB;        /* rgb(37, 99, 235) */
--primary-blue-light: #3B82F6;  /* rgb(59, 130, 246) */
--primary-blue-dark: #1D4ED8;   /* rgb(29, 78, 216) */

/* Verde Sucesso - Crescimento e Oportunidade */
--success-green: #10B981;       /* rgb(16, 185, 129) */
--success-green-light: #34D399; /* rgb(52, 211, 153) */
--success-green-dark: #059669;  /* rgb(5, 150, 105) */
```

#### **Cores Secundárias**
```css
/* Laranja Energia - Ação e Motivação */
--accent-orange: #F59E0B;       /* rgb(245, 158, 11) */
--accent-orange-light: #FBBF24; /* rgb(251, 191, 36) */
--accent-orange-dark: #D97706;  /* rgb(217, 119, 6) */

/* Roxo Inovação - Tecnologia e IA */
--accent-purple: #8B5CF6;       /* rgb(139, 92, 246) */
--accent-purple-light: #A78BFA; /* rgb(167, 139, 250) */
--accent-purple-dark: #7C3AED;  /* rgb(124, 58, 237) */
```

#### **Cores Neutras**
```css
/* Escala de Cinzas */
--gray-50: #F9FAFB;   /* rgb(249, 250, 251) */
--gray-100: #F3F4F6;  /* rgb(243, 244, 246) */
--gray-200: #E5E7EB;  /* rgb(229, 231, 235) */
--gray-300: #D1D5DB;  /* rgb(209, 213, 219) */
--gray-400: #9CA3AF;  /* rgb(156, 163, 175) */
--gray-500: #6B7280;  /* rgb(107, 114, 128) */
--gray-600: #4B5563;  /* rgb(75, 85, 99) */
--gray-700: #374151;  /* rgb(55, 65, 81) */
--gray-800: #1F2937;  /* rgb(31, 41, 55) */
--gray-900: #111827;  /* rgb(17, 24, 39) */

/* Branco e Preto */
--white: #FFFFFF;     /* rgb(255, 255, 255) */
--black: #000000;     /* rgb(0, 0, 0) */
```

#### **Cores de Estado**
```css
/* Estados de Feedback */
--error-red: #EF4444;         /* rgb(239, 68, 68) */
--error-red-light: #F87171;   /* rgb(248, 113, 113) */
--error-red-dark: #DC2626;    /* rgb(220, 38, 38) */

--warning-yellow: #F59E0B;    /* rgb(245, 158, 11) */
--warning-yellow-light: #FBBF24; /* rgb(251, 191, 36) */
--warning-yellow-dark: #D97706;  /* rgb(217, 119, 6) */

--info-blue: #3B82F6;         /* rgb(59, 130, 246) */
--info-blue-light: #60A5FA;   /* rgb(96, 165, 250) */
--info-blue-dark: #2563EB;    /* rgb(37, 99, 235) */
```

### Uso das Cores

#### **Hierarquia de Cores**
- **Primária (Azul)**: CTAs principais, links importantes, elementos de navegação
- **Sucesso (Verde)**: Confirmações, sucessos, progresso positivo
- **Energia (Laranja)**: CTAs secundários, highlights, elementos de atenção
- **Inovação (Roxo)**: Elementos relacionados à IA, features premium
- **Neutras (Cinzas)**: Textos, backgrounds, bordas, elementos estruturais

#### **Contraste e Acessibilidade**
- Todas as combinações atendem WCAG 2.1 AA (4.5:1 para texto normal)
- Texto grande atende WCAG 2.1 AAA (3:1)
- Estados de foco com contraste mínimo de 3:1

## 📝 SISTEMA TIPOGRÁFICO

### Família Tipográfica

#### **Fonte Principal: Inter**
```css
/* Importação da fonte */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Definição da família */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

**Justificativa**: Inter é uma fonte moderna, altamente legível e otimizada para interfaces digitais, com excelente suporte a caracteres especiais e múltiplos pesos.

#### **Fonte Secundária: JetBrains Mono (Código)**
```css
/* Para elementos de código */
font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
```

### Escala Tipográfica

#### **Headings (Títulos)**
```css
/* H1 - Títulos Principais */
.heading-1 {
  font-size: 2.25rem;    /* 36px */
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.025em;
}

/* H2 - Títulos de Seção */
.heading-2 {
  font-size: 1.875rem;   /* 30px */
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.025em;
}

/* H3 - Subtítulos */
.heading-3 {
  font-size: 1.5rem;     /* 24px */
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.025em;
}

/* H4 - Títulos Menores */
.heading-4 {
  font-size: 1.25rem;    /* 20px */
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.025em;
}

/* H5 - Subtítulos Menores */
.heading-5 {
  font-size: 1.125rem;   /* 18px */
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.025em;
}

/* H6 - Títulos Mínimos */
.heading-6 {
  font-size: 1rem;       /* 16px */
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.025em;
}
```

#### **Body Text (Texto Corpo)**
```css
/* Texto Principal */
.body-large {
  font-size: 1.125rem;   /* 18px */
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0;
}

/* Texto Padrão */
.body-medium {
  font-size: 1rem;       /* 16px */
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0;
}

/* Texto Pequeno */
.body-small {
  font-size: 0.875rem;   /* 14px */
  font-weight: 400;
  line-height: 1.5;
  letter-spacing: 0;
}

/* Texto Muito Pequeno */
.body-xs {
  font-size: 0.75rem;    /* 12px */
  font-weight: 400;
  line-height: 1.4;
  letter-spacing: 0.025em;
}
```

#### **Texto Especializado**
```css
/* Labels e Formulários */
.label {
  font-size: 0.875rem;   /* 14px */
  font-weight: 500;
  line-height: 1.4;
  letter-spacing: 0.025em;
}

/* Código Inline */
.code-inline {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.875rem;   /* 14px */
  font-weight: 400;
  background: var(--gray-100);
  padding: 0.125rem 0.25rem;
  border-radius: 0.25rem;
}

/* Código em Bloco */
.code-block {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.875rem;   /* 14px */
  font-weight: 400;
  line-height: 1.5;
  background: var(--gray-900);
  color: var(--gray-100);
  padding: 1rem;
  border-radius: 0.5rem;
  overflow-x: auto;
}
```

### Responsividade Tipográfica

#### **Mobile (< 768px)**
```css
@media (max-width: 767px) {
  .heading-1 { font-size: 1.875rem; } /* 30px */
  .heading-2 { font-size: 1.5rem; }   /* 24px */
  .heading-3 { font-size: 1.25rem; }  /* 20px */
  .body-large { font-size: 1rem; }    /* 16px */
}
```

## 🔲 COMPONENTES DE INTERFACE

### Botões

#### **Botão Primário**
```css
.btn-primary {
  background: var(--primary-blue);
  color: var(--white);
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: var(--primary-blue-dark);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(37, 99, 235, 0.3);
}

.btn-primary:disabled {
  background: var(--gray-300);
  color: var(--gray-500);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}
```

#### **Botão Secundário**
```css
.btn-secondary {
  background: transparent;
  color: var(--primary-blue);
  border: 2px solid var(--primary-blue);
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: var(--primary-blue);
  color: var(--white);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}
```

#### **Botão de Sucesso**
```css
.btn-success {
  background: var(--success-green);
  color: var(--white);
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-success:hover {
  background: var(--success-green-dark);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}
```

#### **Tamanhos de Botão**
```css
/* Pequeno */
.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

/* Médio (padrão) */
.btn-md {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}

/* Grande */
.btn-lg {
  padding: 1rem 2rem;
  font-size: 1.125rem;
}

/* Extra Grande */
.btn-xl {
  padding: 1.25rem 2.5rem;
  font-size: 1.25rem;
}
```

### Formulários

#### **Input Fields**
```css
.input-field {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 2px solid var(--gray-300);
  border-radius: 0.5rem;
  font-size: 1rem;
  font-family: inherit;
  background: var(--white);
  transition: all 0.2s ease;
}

.input-field:focus {
  outline: none;
  border-color: var(--primary-blue);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.input-field:invalid {
  border-color: var(--error-red);
}

.input-field:disabled {
  background: var(--gray-100);
  color: var(--gray-500);
  cursor: not-allowed;
}
```

#### **Labels**
```css
.input-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  font-size: 0.875rem;
  color: var(--gray-700);
}

.input-label.required::after {
  content: ' *';
  color: var(--error-red);
}
```

#### **Mensagens de Erro**
```css
.input-error {
  margin-top: 0.25rem;
  font-size: 0.875rem;
  color: var(--error-red);
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.input-error::before {
  content: '⚠';
  font-size: 1rem;
}
```

### Cards

#### **Card Básico**
```css
.card {
  background: var(--white);
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  border: 1px solid var(--gray-200);
  overflow: hidden;
  transition: all 0.2s ease;
}

.card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.card-header {
  padding: 1.5rem 1.5rem 0;
}

.card-body {
  padding: 1.5rem;
}

.card-footer {
  padding: 0 1.5rem 1.5rem;
  border-top: 1px solid var(--gray-200);
  margin-top: 1rem;
  padding-top: 1rem;
}
```

#### **Card de Destaque**
```css
.card-featured {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
  border: none;
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
}

.card-featured:hover {
  box-shadow: 0 12px 35px rgba(37, 99, 235, 0.4);
}
```

### Navegação

#### **Menu Principal**
```css
.nav-main {
  background: var(--white);
  border-bottom: 1px solid var(--gray-200);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
}

.nav-item {
  padding: 0.5rem 1rem;
  color: var(--gray-700);
  text-decoration: none;
  font-weight: 500;
  border-radius: 0.5rem;
  transition: all 0.2s ease;
}

.nav-item:hover {
  background: var(--gray-100);
  color: var(--primary-blue);
}

.nav-item.active {
  background: var(--primary-blue);
  color: var(--white);
}
```

#### **Breadcrumbs**
```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: var(--gray-600);
  margin-bottom: 1rem;
}

.breadcrumb-item {
  color: var(--gray-600);
  text-decoration: none;
}

.breadcrumb-item:hover {
  color: var(--primary-blue);
}

.breadcrumb-item.current {
  color: var(--gray-900);
  font-weight: 500;
}

.breadcrumb-separator::before {
  content: '/';
  margin: 0 0.5rem;
  color: var(--gray-400);
}
```

## 📱 PADRÕES DE LAYOUT

### Grid System

#### **Container**
```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

@media (min-width: 640px) {
  .container { padding: 0 1.5rem; }
}

@media (min-width: 1024px) {
  .container { padding: 0 2rem; }
}
```

#### **Grid Layout**
```css
.grid {
  display: grid;
  gap: 1.5rem;
}

.grid-cols-1 { grid-template-columns: repeat(1, 1fr); }
.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-4 { grid-template-columns: repeat(4, 1fr); }

/* Responsivo */
@media (max-width: 767px) {
  .grid-cols-2,
  .grid-cols-3,
  .grid-cols-4 {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .grid-cols-3,
  .grid-cols-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

#### **Flexbox Utilities**
```css
.flex { display: flex; }
.flex-col { flex-direction: column; }
.flex-row { flex-direction: row; }
.items-center { align-items: center; }
.items-start { align-items: flex-start; }
.items-end { align-items: flex-end; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.justify-start { justify-content: flex-start; }
.justify-end { justify-content: flex-end; }
.gap-1 { gap: 0.25rem; }
.gap-2 { gap: 0.5rem; }
.gap-3 { gap: 0.75rem; }
.gap-4 { gap: 1rem; }
.gap-6 { gap: 1.5rem; }
.gap-8 { gap: 2rem; }
```

### Espaçamento

#### **Sistema de Espaçamento**
```css
/* Padding */
.p-1 { padding: 0.25rem; }
.p-2 { padding: 0.5rem; }
.p-3 { padding: 0.75rem; }
.p-4 { padding: 1rem; }
.p-6 { padding: 1.5rem; }
.p-8 { padding: 2rem; }
.p-12 { padding: 3rem; }

/* Margin */
.m-1 { margin: 0.25rem; }
.m-2 { margin: 0.5rem; }
.m-3 { margin: 0.75rem; }
.m-4 { margin: 1rem; }
.m-6 { margin: 1.5rem; }
.m-8 { margin: 2rem; }
.m-12 { margin: 3rem; }

/* Direcionais */
.pt-4 { padding-top: 1rem; }
.pb-4 { padding-bottom: 1rem; }
.pl-4 { padding-left: 1rem; }
.pr-4 { padding-right: 1rem; }
.px-4 { padding-left: 1rem; padding-right: 1rem; }
.py-4 { padding-top: 1rem; padding-bottom: 1rem; }
```

## 🎭 PADRÕES DE INTERAÇÃO

### Animações e Transições

#### **Transições Padrão**
```css
/* Transição suave para a maioria dos elementos */
.transition-smooth {
  transition: all 0.2s ease;
}

/* Transição rápida para feedback imediato */
.transition-fast {
  transition: all 0.1s ease;
}

/* Transição lenta para elementos complexos */
.transition-slow {
  transition: all 0.3s ease;
}
```

#### **Animações de Entrada**
```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-20px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.animate-fade-in {
  animation: fadeIn 0.3s ease;
}

.animate-slide-in-left {
  animation: slideInLeft 0.3s ease;
}

.animate-scale-in {
  animation: scaleIn 0.2s ease;
}
```

### Estados de Interação

#### **Estados de Hover**
```css
.hover-lift:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.hover-scale:hover {
  transform: scale(1.05);
}

.hover-glow:hover {
  box-shadow: 0 0 20px rgba(37, 99, 235, 0.3);
}
```

#### **Estados de Foco**
```css
.focus-ring:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
}

.focus-visible:focus-visible {
  outline: 2px solid var(--primary-blue);
  outline-offset: 2px;
}
```

### Loading States

#### **Skeleton Loading**
```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--gray-200) 25%,
    var(--gray-300) 50%,
    var(--gray-200) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  border-radius: 0.25rem;
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

#### **Spinner**
```css
.spinner {
  width: 2rem;
  height: 2rem;
  border: 2px solid var(--gray-300);
  border-top: 2px solid var(--primary-blue);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

## 🔍 ICONOGRAFIA

### Sistema de Ícones

#### **Biblioteca Principal: Lucide Icons**
- **Justificativa**: Ícones modernos, consistentes e otimizados
- **Estilo**: Outline, minimalista, profissional
- **Tamanhos**: 16px, 20px, 24px, 32px
- **Peso**: 1.5px stroke width

#### **Tamanhos de Ícones**
```css
.icon-sm { width: 1rem; height: 1rem; } /* 16px */
.icon-md { width: 1.25rem; height: 1.25rem; } /* 20px */
.icon-lg { width: 1.5rem; height: 1.5rem; } /* 24px */
.icon-xl { width: 2rem; height: 2rem; } /* 32px */
```

#### **Cores de Ícones**
```css
.icon-primary { color: var(--primary-blue); }
.icon-success { color: var(--success-green); }
.icon-warning { color: var(--warning-yellow); }
.icon-error { color: var(--error-red); }
.icon-muted { color: var(--gray-500); }
.icon-dark { color: var(--gray-700); }
```

### Ícones Específicos do Projeto

#### **Categorias de Ícones**
- **Navegação**: Menu, setas, home, voltar
- **Ações**: Editar, deletar, salvar, compartilhar
- **Status**: Sucesso, erro, aviso, informação
- **Funcionalidades**: Upload, download, busca, filtro
- **IA/Tecnologia**: Bot, análise, otimização, insights

## 📱 RESPONSIVIDADE

### Breakpoints

#### **Sistema de Breakpoints**
```css
/* Mobile First Approach */
/* xs: 0px - 639px (mobile) */
/* sm: 640px - 767px (mobile large) */
@media (min-width: 640px) { /* sm */ }

/* md: 768px - 1023px (tablet) */
@media (min-width: 768px) { /* md */ }

/* lg: 1024px - 1279px (desktop) */
@media (min-width: 1024px) { /* lg */ }

/* xl: 1280px - 1535px (desktop large) */
@media (min-width: 1280px) { /* xl */ }

/* 2xl: 1536px+ (desktop extra large) */
@media (min-width: 1536px) { /* 2xl */ }
```

### Padrões Responsivos

#### **Layout Adaptativo**
```css
/* Mobile: Stack vertical */
.responsive-layout {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Tablet: 2 colunas */
@media (min-width: 768px) {
  .responsive-layout {
    flex-direction: row;
    gap: 2rem;
  }
  
  .responsive-layout > * {
    flex: 1;
  }
}

/* Desktop: Layout específico */
@media (min-width: 1024px) {
  .responsive-layout {
    gap: 3rem;
  }
}
```

#### **Tipografia Responsiva**
```css
.responsive-heading {
  font-size: 1.5rem; /* Mobile */
}

@media (min-width: 768px) {
  .responsive-heading {
    font-size: 2rem; /* Tablet */
  }
}

@media (min-width: 1024px) {
  .responsive-heading {
    font-size: 2.5rem; /* Desktop */
  }
}
```

## ♿ ACESSIBILIDADE

### Diretrizes WCAG 2.1

#### **Contraste de Cores**
- **AA Normal**: Mínimo 4.5:1 para texto normal
- **AA Large**: Mínimo 3:1 para texto grande (18px+ ou 14px+ bold)
- **AAA**: Mínimo 7:1 para texto normal (objetivo)

#### **Navegação por Teclado**
```css
/* Indicadores de foco visíveis */
*:focus-visible {
  outline: 2px solid var(--primary-blue);
  outline-offset: 2px;
}

/* Skip links */
.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: var(--primary-blue);
  color: var(--white);
  padding: 8px;
  text-decoration: none;
  border-radius: 4px;
  z-index: 1000;
}

.skip-link:focus {
  top: 6px;
}
```

#### **Texto Alternativo e Labels**
```html
<!-- Imagens sempre com alt -->
<img src="..." alt="Descrição significativa" />

<!-- Formulários com labels associados -->
<label for="email">E-mail</label>
<input id="email" type="email" name="email" />

<!-- Botões com texto ou aria-label -->
<button aria-label="Fechar modal">×</button>
```

### Tecnologias Assistivas

#### **ARIA Labels e Roles**
```html
<!-- Landmarks -->
<nav role="navigation" aria-label="Menu principal">
<main role="main">
<aside role="complementary">

<!-- Estados dinâmicos -->
<button aria-expanded="false" aria-controls="menu">
<div aria-live="polite" id="status">
<div aria-hidden="true"> <!-- Para elementos decorativos -->
```

#### **Estrutura Semântica**
```html
<!-- Hierarquia de headings -->
<h1>Título Principal</h1>
  <h2>Seção</h2>
    <h3>Subseção</h3>

<!-- Listas estruturadas -->
<ul role="list">
  <li role="listitem">Item</li>
</ul>
```

## 🎨 IMPLEMENTAÇÃO EM FLUTTER

### Theme Configuration

#### **Material Theme**
```dart
// theme/app_theme.dart
class AppTheme {
  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: const Color(0xFF2563EB), // primary-blue
        brightness: Brightness.light,
      ),
      fontFamily: 'Inter',
      textTheme: _textTheme,
      elevatedButtonTheme: _elevatedButtonTheme,
      inputDecorationTheme: _inputDecorationTheme,
    );
  }
  
  static const TextTheme _textTheme = TextTheme(
    displayLarge: TextStyle(
      fontSize: 36,
      fontWeight: FontWeight.w700,
      height: 1.2,
      letterSpacing: -0.025,
    ),
    headlineLarge: TextStyle(
      fontSize: 30,
      fontWeight: FontWeight.w600,
      height: 1.3,
      letterSpacing: -0.025,
    ),
    // ... outros estilos
  );
}
```

#### **Color Palette**
```dart
// theme/app_colors.dart
class AppColors {
  // Primary Colors
  static const Color primaryBlue = Color(0xFF2563EB);
  static const Color primaryBlueLight = Color(0xFF3B82F6);
  static const Color primaryBlueDark = Color(0xFF1D4ED8);
  
  // Success Colors
  static const Color successGreen = Color(0xFF10B981);
  static const Color successGreenLight = Color(0xFF34D399);
  static const Color successGreenDark = Color(0xFF059669);
  
  // Neutral Colors
  static const Color gray50 = Color(0xFFF9FAFB);
  static const Color gray100 = Color(0xFFF3F4F6);
  static const Color gray200 = Color(0xFFE5E7EB);
  // ... outras cores
}
```

### Componentes Customizados

#### **Custom Button**
```dart
// widgets/custom_button.dart
class CustomButton extends StatelessWidget {
  final String text;
  final VoidCallback? onPressed;
  final ButtonType type;
  final ButtonSize size;
  
  const CustomButton({
    Key? key,
    required this.text,
    this.onPressed,
    this.type = ButtonType.primary,
    this.size = ButtonSize.medium,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      style: _getButtonStyle(),
      child: Text(text),
    );
  }
  
  ButtonStyle _getButtonStyle() {
    // Implementação baseada no type e size
  }
}
```

## 📊 MÉTRICAS E VALIDAÇÃO

### KPIs de Design System

#### **Consistência Visual**
- **Métrica**: % de componentes seguindo o style guide
- **Target**: 95%
- **Medição**: Auditoria visual semanal

#### **Performance de Carregamento**
- **Métrica**: Tempo de carregamento de assets visuais
- **Target**: < 2 segundos
- **Medição**: Lighthouse e ferramentas de performance

#### **Acessibilidade**
- **Métrica**: Score de acessibilidade (WAVE, axe)
- **Target**: 100% conformidade WCAG 2.1 AA
- **Medição**: Testes automatizados e manuais

#### **Usabilidade**
- **Métrica**: Taxa de conclusão de tarefas
- **Target**: > 90%
- **Medição**: Testes de usabilidade

### Ferramentas de Validação

#### **Automatizadas**
- **Lighthouse**: Performance e acessibilidade
- **axe-core**: Testes de acessibilidade
- **Chromatic**: Testes visuais de componentes
- **Percy**: Regressão visual

#### **Manuais**
- **Testes de contraste**: WebAIM Contrast Checker
- **Navegação por teclado**: Testes manuais
- **Leitores de tela**: NVDA, JAWS, VoiceOver
- **Dispositivos reais**: Testes em múltiplos dispositivos

## 🔄 EVOLUÇÃO E MANUTENÇÃO

### Versionamento

#### **Semantic Versioning**
- **Major (1.0.0)**: Mudanças que quebram compatibilidade
- **Minor (0.1.0)**: Novas funcionalidades compatíveis
- **Patch (0.0.1)**: Correções e melhorias menores

#### **Changelog**
```markdown
## [1.1.0] - 2025-06-25
### Added
- Novos componentes de data picker
- Suporte a modo escuro

### Changed
- Atualização da paleta de cores
- Melhoria na responsividade

### Fixed
- Correção de contraste em botões secundários
```

### Processo de Atualização

#### **Ciclo de Revisão**
1. **Semanal**: Pequenos ajustes e correções
2. **Mensal**: Novos componentes e melhorias
3. **Trimestral**: Revisão estratégica completa
4. **Anual**: Atualização major com breaking changes

#### **Stakeholder Review**
- **Design Team**: Validação visual e UX
- **Development Team**: Viabilidade técnica
- **Product Team**: Alinhamento com objetivos
- **Accessibility Team**: Conformidade e inclusão

## 📚 Referências e Recursos

### Documentos Relacionados
- **ESTRATEGIA_MOMENTO_AHA_para_RAG.md**: Estratégia de experiência
- **HLD_para_RAG.md**: Arquitetura técnica
- **ERS_para_RAG.md**: Requisitos funcionais
- **AGENTES_IA_MENTORES_OVERVIEW_para_RAG.md**: Equipe de desenvolvimento

### Recursos Externos
- **WCAG 2.1 Guidelines**: https://www.w3.org/WAI/WCAG21/quickref/
- **Material Design 3**: https://m3.material.io/
- **Inter Font**: https://rsms.me/inter/
- **Lucide Icons**: https://lucide.dev/
- **Flutter Material**: https://docs.flutter.dev/ui/widgets/material

### Ferramentas Recomendadas
- **Figma**: Design e prototipagem
- **Storybook**: Documentação de componentes
- **Chromatic**: Testes visuais
- **Lighthouse**: Auditoria de performance
- **axe DevTools**: Testes de acessibilidade

---

**Documento**: STYLE_GUIDE_para_RAG.md (v1.0)
**Otimizado para**: Sistema RAG - Consulta de padrões visuais e de interação
**Palavras-chave RAG**: style guide, design system, ui components, visual identity, brand guidelines, color palette, typography system, iconography, layout patterns, interaction design, accessibility standards, responsive design, flutter components, pwa design, mobile first

--- FIM DO DOCUMENTO STYLE_GUIDE_para_RAG.md (v1.0) ---