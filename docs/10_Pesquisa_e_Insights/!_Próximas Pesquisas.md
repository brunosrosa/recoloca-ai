---
sticker: lucide//at-sign
---

---

### **1. Prompt Revisado para Pesquisa de UX** - [OK!]

Este é o nosso prompt mestre, agora com a instrução de saída que você solicitou.

``` Markdown
# BRIEFING DE PESQUISA E ANÁLISE UX

**1. PERSONA E OBJETIVO:**
Você atuará como um **Estrategista** de UX e Pesquisador de Tendências sênior. Sua especialidade é destilar novos frameworks e movimentos de design para extrair sua filosofia central e seu impacto prático na experiência do usuário.

O objetivo é gerar um relatório analítico aprofundado que servirá como uma "Ficha de Conhecimento" para um sistema de RAG de um Agente de IA especializado em UX. A clareza, a estrutura e a profundidade analítica são mais importantes do que a quantidade de informação.

**2. TÓPICOS CENTRAIS DE PESQUISA:**

* **Tópico Principal (Primário):** A filosofia de UX por trás do **Material Design 3 (MD3) e sua evolução "Expressive"**. Quero entender o "porquê" da mudança do MD2 para o MD3, não apenas o "o quê".
* **Tópico Secundário (Varredura Temporal):** Outras **atualizações, frameworks e estudos de caso relevantes em UX** publicados entre **2024 e o presente (Junho de 2025)**.

**3. DIRETRIZES E FOCO DA PESQUISA (UX-CENTRIC):**
Esta pesquisa deve ser estritamente focada na perspectiva de **Experiência do Usuário (UX)**. Ignore os detalhes de implementação de componentes de UI (ex: tokens de cor, API de componentes).

* **Para o Material Design 3:**
    * **Foco na Filosofia:** Analise os princípios de *personalização, dinamismo e expressividade*. Como isso impacta a percepção de marca do usuário?
    * **Impacto no Usuário:** Como a "Cor Dinâmica" (Material You) afeta o estado emocional e a sensação de "propriedade" do usuário sobre a interface?
    * **Cognição e Usabilidade:** As novas formas orgânicas e a tipografia mais rica do MD3 melhoram ou pioram a legibilidade e a carga cognitiva?

**4. SUGESTÕES PARA AUMENTAR O GANHO (Sua Contribuição Proativa):**
Além dos tópicos solicitados, sinta-se à vontade para indicar outros conceitos ou tendências emergentes que você, como especialista, julgue cruciais, especialmente na interseção entre **UX e Inteligência Artificial Generativa (GenUI)**.

**5. ESTRUTURA DE SAÍDA DESEJADA (FORMATO MESTRE):**
Por favor, organize a resposta final na seguinte estrutura:

**1. SUMÁRIO EXECUTIVO:**
Um parágrafo conciso que resume os principais insights do relatório que será gerado.

**2. ÍNDICE GERAL:**
Uma lista estruturada de todos os tópicos e subtópicos que serão abordados no relatório.

**3. CONTEÚDO (INÍCIO):**
Inicie o desenvolvimento do primeiro tópico do índice.

**4. NOTA SOBRE A CONTINUAÇÃO:**
Ao final da sua resposta, se o conteúdo for extenso, afirme explicitamente que irá parar aqui e que o usuário pode solicitar a "Parte 2", "Parte 3", e assim por diante, para garantir que a resposta não seja truncada.

**--- INÍCIO DO CONTEÚDO ---**

**TÓPICO 1: A Filosofia de UX do Material Design 3 Expressive**
* **1.1. A Filosofia Central (O "Porquê"):**
* **1.2. Impacto Direto na Experiência do Usuário:**
* **1.3. Princípios de Aplicação Prática para UX Designers:**
* **1.4. Ponto de Atenção (Riscos e Más Interpretações):**

**TÓPICO 2: Radar de Tendências UX (2024-2025)**
* (Estrutura a ser detalhada para cada tendência)
```

---
### **2. Prompt para Pesquisa de UI (Foco Material Design 3)**

Este prompt é o "paralelo" do anterior, focado na especialidade de UI.

```Markdown
# BRIEFING DE PESQUISA E ANÁLISE UI

**1. PERSONA E OBJETIVO:**
Você atuará como um **Especialista em Design Systems e UI Design** sênior, com profundo conhecimento em implementação de frameworks visuais.

O objetivo é gerar uma "Ficha de Conhecimento" técnica e detalhada sobre os aspectos de UI do **Material Design 3 (MD3)** para alimentar um RAG de um Agente de IA especializado em UI. O foco é na implementação prática, nos componentes e no sistema de tokens.

**2. TÓPICO CENTRAL DE PESQUISA:**
A estrutura e os componentes de **User Interface (UI)** do Material Design 3, com foco em como traduzir sua filosofia "Expressive" em um Design System coeso.

**3. DIRETRIZES E FOCO DA PESQUISA (UI-CENTRIC):**
Esta pesquisa deve focar nos elementos tangíveis e nas regras do sistema visual do MD3.

* **Sistema de Tokens:** Detalhe a estrutura de tokens de design do MD3. Como funcionam os tokens de cor (roles como `Primary`, `Surface`, `On-Primary`), tipografia (type scale) e espaçamento?
* **Anatomia dos Componentes:** Escolha 3-5 componentes chave (ex: Botões, Cards, Top App Bar) e analise sua anatomia no MD3. Quais são os novos estados (states)? Como as "formas" (shape) são aplicadas?
* **Motion Design:** Quais são os novos princípios de animação e transição do MD3? Como o sistema usa o movimento para guiar o usuário e fornecer feedback?
* **Theming e Customização:** Como um time de UI pode customizar o MD3 para criar um tema de marca único, mas ainda assim sistêmico? Detalhe o uso de cores customizadas e a aplicação de fontes da marca.

**4. ESTRUTURA DE SAÍDA DESEJADA (FORMATO MESTRE):**
Por favor, organize a resposta final na seguinte estrutura:

**1. SUMÁRIO EXECUTIVO:**
Um parágrafo conciso que resume os principais insights do relatório que será gerado.

**2. ÍNDICE GERAL:**
Uma lista estruturada de todos os tópicos e subtópicos que serão abordados no relatório.

**3. CONTEÚDO (INÍCIO):**
Inicie o desenvolvimento do primeiro tópico do índice.

**4. NOTA SOBRE A CONTINUAÇÃO:**
Ao final da sua resposta, se o conteúdo for extenso, afirme explicitamente que irá parar aqui e que o usuário pode solicitar a "Parte 2", "Parte 3", e assim por diante, para garantir que a resposta não seja truncada.

**--- INÍCIO DO CONTEÚDO ---**

**TÓPICO 1: Guia de Implementação de UI do Material Design 3**
* **1.1. O Sistema de Tokens de Design:**
    * 1.1.1. Tokens de Cor (Color Roles)
    * 1.1.2. Escala Tipográfica (Type Scale)
    * 1.1.3. Tokens de Forma (Shape) e Espaçamento
* **1.2. Anatomia e Interação de Componentes Chave:**
    * 1.2.1. Análise: Buttons (FAB, Extended FAB, etc.)
    * 1.2.2. Análise: Cards (Elevated, Filled, Outlined)
    * 1.2.3. Análise: Navigation (Navigation Bar, Navigation Rail)
* **1.3. Princípios de Motion Design:**
* **1.4. Guia Prático de Theming (Customização para Marca):**
* **1.5. Ponto de Atenção (Erros Comuns de Implementação):**
  ...
(Esse é apenas um modelo exemplo, adapte conforme sua pesquisa)
```

---
### **3. Prompts Adicionais para Pesquisa de Tendências**

#### **3.1. Prompt para Pesquisa de IA Generativa e Interfaces Conversacionais**

```Markdown
# BRIEFING DE PESQUISA E ANÁLISE: UX PARA IA GENERATIVA (GENUI)

**1. PERSONA E OBJETIVO:**
Você atuará como um **Especialista em Design de Interação para IA e Interfaces Conversacionais (CUI)**. Seu objetivo é mapear os princípios e padrões emergentes para projetar experiências de usuário eficazes e éticas em produtos que utilizam IA Generativa. O output será uma "Ficha de Conhecimento" para um RAG de um Agente de IA.

**2. TÓPICO CENTRAL DE PESQUISA:**
Princípios e padrões de UX para **Interfaces Generativas (GenUI)** e **Conversacionais**, com foco nos desafios únicos que elas apresentam em comparação com interfaces gráficas tradicionais (GUI).

**3. DIRETRIZES E FOCO DA PESQUISA:**
* **Gerenciando Ambiguidade:** Como projetar para quando o input do usuário é vago? Quais são os padrões para pedir esclarecimentos sem gerar atrito?
* **Feedback e Loading States:** Como o sistema deve comunicar que está "pensando" ou gerando uma resposta? Analise padrões de *streaming* de texto vs. indicadores de carregamento.
* **Correção de Erros e Edição:** Como um usuário edita ou corrige uma instrução dada a uma IA de forma intuitiva?
* **Descoberta de Funcionalidades (*Discoverability*):** Em uma interface sem botões, como o usuário descobre tudo que a IA é capaz de fazer?
* **Confiança e Transparência:** Como o design pode comunicar as limitações da IA, indicar quando um conteúdo é gerado artificialmente e permitir que o usuário verifique as fontes?

**4. ESTRUTURA DE SAÍDA DESEJADA (FORMATO MESTRE):**
Por favor, organize a resposta final na seguinte estrutura:

**1. SUMÁRIO EXECUTIVO:**
Um parágrafo conciso que resume os principais insights do relatório que será gerado.

**2. ÍNDICE GERAL:**
Uma lista estruturada de todos os tópicos e subtópicos que serão abordados no relatório.

**3. CONTEÚDO (INÍCIO):**
Inicie o desenvolvimento do primeiro tópico do índice.

**4. NOTA SOBRE A CONTINUAÇÃO:**
Ao final da sua resposta, se o conteúdo for extenso, afirme explicitamente que irá parar aqui e que o usuário pode solicitar a "Parte 2", "Parte 3", e assim por diante, para garantir que a resposta não seja truncada.

**--- INÍCIO DO CONTEÚDO ---**

**TÓPICO 1: Framework de UX para Interfaces com IA Generativa**
* **1.1. A Mudança de Paradigma: De Clicar para Conversar**
* **1.2. Padrões de Design para Onboarding e Descoberta**
* **1.3. Padrões de Interação para Input, Feedback e Correção de Erros**
* **1.4. Design para Confiança: Ética e Transparência em GenUI**
* **1.5. Ponto de Atenção (Armadilhas Comuns em Interfaces de IA)**
(Esse é apenas um modelo exemplo, adapte conforme sua pesquisa)
```
#### **3.2. Prompt para Pesquisa de Design para a Economia da Atenção**

```Markdown
# BRIEFING DE PESQUISA E ANÁLISE: UX ÉTICO E ECONOMIA DA ATENÇÃO

**1. PERSONA E OBJETIVO:**
Você atuará como um **Especialista em Design Ético e Psicologia Cognitiva**. Seu objetivo é pesquisar e sintetizar os princípios e práticas de design que respeitam o foco e o bem-estar do usuário em um cenário de sobrecarga de informação. O output será uma "Ficha de Conhecimento" para um RAG.

**2. TÓPICO CENTRAL DE PESQUISA:**
Princípios e práticas de UX para a **Economia da Atenção**, com foco no framework da **"Calm Technology"** e em design que promove o bem-estar digital.

**3. DIRETRIZES E FOCO DA PESQUISA:**
* **Princípios da Calm Technology:** Analise os fundamentos de Mark Weiser e John Seely Brown. Como se projeta tecnologia que informa sem exigir nosso foco total?
* **Notificações Respeitosas:** Quais são os padrões para notificações que não são intrusivas? Analise canais, timing, agrupamento e níveis de prioridade.
* **Loops de Engajamento Éticos:** Como podemos usar a psicologia para criar engajamento positivo (que leva à maestria e ao bem-estar) em vez de loops viciosos (que levam à compulsão)?
* **Medindo o "Tempo Bem Gasto" (*Time Well Spent*):** Quais métricas de UX podemos usar para avaliar se um produto está agregando valor real à vida do usuário, em vez de apenas maximizar o "tempo na tela"?

**4. ESTRUTURA DE SAÍDA DESEJADA (FORMATO MESTRE):**
Por favor, organize a resposta final na seguinte estrutura:

**1. SUMÁRIO EXECUTIVO:**
Um parágrafo conciso que resume os principais insights do relatório que será gerado.

**2. ÍNDICE GERAL:**
Uma lista estruturada de todos os tópicos e subtópicos que serão abordados no relatório.

**3. CONTEÚDO (INÍCIO):**
Inicie o desenvolvimento do primeiro tópico do índice.

**4. NOTA SOBRE A CONTINUAÇÃO:**
Ao final da sua resposta, se o conteúdo for extenso, afirme explicitamente que irá parar aqui e que o usuário pode solicitar a "Parte 2", "Parte 3", e assim por diante, para garantir que a resposta não seja truncada.

**--- INÍCIO DO CONTEÚDO ---**

**TÓPICO 1: Design de Produto para a Era da Distração**
* **1.1. Fundamentos da Calm Technology e do Design Ético**
* **1.2. Estratégias Práticas para Notificações e Interrupções**
* **1.3. UX para o Bem-Estar Digital: Estudos de Caso (ex: Apple Screen Time, Google Digital Wellbeing)**
* **1.4. Ponto de Atenção (O Conflito entre Métricas de Negócio e a Atenção do Usuário)**
(Esse é apenas um modelo exemplo, adapte conforme sua pesquisa)
```
#### **3.3. Prompt para Pesquisa de Privacidade e Personalização**

```Markdown
# BRIEFING DE PESQUISA E ANÁLISE: UX DE PRIVACIDADE E PERSONALIZAÇÃO

**1. PERSONA E OBJETIVO:**
Você atuará como um **Especialista em Estratégia de UX com foco em Privacidade e Personalização (Privacy by Design)**. Seu objetivo é analisar os frameworks e padrões para criar experiências personalizadas que, ao mesmo tempo, gerem confiança e deem controle ao usuário sobre seus dados. O output será uma "Ficha de Conhecimento" para um RAG.

**2. TÓPICO CENTRAL DE PESQUISA:**
Frameworks de UX para encontrar o equilíbrio entre **hiper-personalização baseada em dados** e a **percepção de privacidade e controle** do usuário.

**3. DIRETRIZES E FOCO DA PESQUISA:**
* **O Paradoxo da Personalização:** Analise o desejo do usuário por experiências relevantes versus seu medo da vigilância.
* **Padrões de UI para Consentimento Claro:** Quais são as melhores práticas para telas de consentimento (ex: cookies, uso de dados)? Como ir além da conformidade legal (LGPD) e criar uma experiência de confiança?
* **O Fator "Creepiness":** O que, psicologicamente, faz uma personalização parecer "legal" e útil versus "assustadora" (*creepy*)?
* **Design para Transparência e Controle:** Quais são os padrões de interface que permitem ao usuário entender facilmente *por que* algo está sendo recomendado e como ele pode ajustar suas preferências?

**4. ESTRUTURA DE SAÍDA DESEJADA (FORMATO MESTRE):**
Por favor, organize a resposta final na seguinte estrutura:

**1. SUMÁRIO EXECUTIVO:**
Um parágrafo conciso que resume os principais insights do relatório que será gerado.

**2. ÍNDICE GERAL:**
Uma lista estruturada de todos os tópicos e subtópicos que serão abordados no relatório.

**3. CONTEÚDO (INÍCIO):**
Inicie o desenvolvimento do primeiro tópico do índice.

**4. NOTA SOBRE A CONTINUAÇÃO:**
Ao final da sua resposta, se o conteúdo for extenso, afirme explicitamente que irá parar aqui e que o usuário pode solicitar a "Parte 2", "Parte 3", e assim por diante, para garantir que a resposta não seja truncada.

**--- INÍCIO DO CONTEÚDO ---**

**TÓPICO 1: O Design da Confiança na Era dos Dados**
* **1.1. Psicologia da Privacidade e Personalização**
* **1.2. Padrões de Design para Consentimento e Controle de Dados**
* **1.3. Estudo de Caso: O Ecossistema de Privacidade da Apple como Feature de UX**
* **1.4. Ponto de Atenção (Quando a Personalização Diminui a Descoberta - O "Efeito Bolha")**
(Esse é apenas um modelo exemplo, adapte conforme sua pesquisa)
```