---
sticker: lucide//check
---
# ADR 001: Escolha das Ferramentas e Tecnologias Core do Projeto Recoloca.ai

**Status**: Aprovado

**Data**: 03 de junho de 2025

**Data de Última Atualização**: Junho de 2025

**Versão**: 1.1 (Orquestração Inteligente e Specialized Intelligence)

**Decisor**: Bruno S. Rosa (Maestro)

**Consultados**: @AgenteOrquestrador (para análise de alternativas e alinhamento estratégico), Documentação Oficial das ferramentas, Comunidade de Desenvolvedores.
## Contexto e Problema

O projeto Recoloca.ai, um Micro-SaaS para auxiliar na recolocação profissional, exige uma stack tecnológica robusta, escalável e alinhada com a metodologia de "Desenvolvimento Solo Ágil Aumentado por IA". As escolhas devem considerar:

1. **Produtividade do Desenvolvedor Solo (Maestro):** Ferramentas que maximizem a eficiência e minimizem a sobrecarga de aprendizado e manutenção.
    
2. **Capacidades de IA:** Integração nativa ou facilitada com LLMs e tecnologias de RAG.
    
3. **Escalabilidade e Custo:** Capacidade de atender a um número crescente de usuários com custos operacionais gerenciáveis para um modelo Freemium.
    
4. **Comunidade e Ecossistema:** Disponibilidade de bibliotecas, documentação e suporte da comunidade.
    
5. **Experiência do Usuário (UX):** Tecnologias que permitam criar uma interface rica, responsiva e agradável.
    
6. **Segurança:** Ferramentas com boas práticas de segurança incorporadas.
    
7. **Alinhamento com a Metodologia:** Ferramentas que suportem a "Documentação Viva", a gestão de Agentes de IA e o fluxo de trabalho ágil adaptado.
    

Este ADR visa documentar as decisões sobre as principais ferramentas e tecnologias que formarão o núcleo da arquitetura do Recoloca.ai.
## Alternativas Consideradas e Decisão

Foram consideradas diversas alternativas para cada componente da stack. As decisões tomadas e suas justificativas são detalhadas abaixo.
### 1. Stack de Desenvolvimento Principal

- **Frontend (PWA):**
    
    - **Decisão:** **Flutter (Dart)**
        
    - **Justificativa:**
        
        - **Produtividade:** Desenvolvimento rápido de UI com hot reload/restart, vasta biblioteca de widgets customizáveis.
            
        - **Multiplataforma Real:** Permite compilar para Web (PWA), Mobile (iOS/Android) e Desktop a partir de uma única base de código, oferecendo flexibilidade futura com baixo retrabalho.
            
        - **Performance:** Compila para código nativo (mobile/desktop) e otimizado para web, oferecendo boa performance.
            
        - **Comunidade e Ecossistema:** Grande e crescente comunidade, vasta documentação e muitos pacotes (pub.dev).
            
        - **UX:** Permite criar interfaces ricas e consistentes com o Material Design 3.
            
    - **Alternativas Consideradas:** React (com Next.js/Remix), Vue.js, Svelte. Embora poderosas, a curva de aprendizado para gerenciar o estado de forma eficiente e a complexidade do build para PWA robusta foram consideradas maiores para um desenvolvedor solo em comparação com a experiência integrada do Flutter.
        
- **Backend:**
    
    - **Decisão:** **Python com FastAPI**
        
    - **Justificativa:**
        
        - **Produtividade e Simplicidade:** FastAPI é moderno, rápido (baseado em Starlette e Pydantic) e permite criar APIs robustas com poucas linhas de código.
            
        - **Performance:** Alta performance, comparável a Node.js e Go para I/O bound tasks.
            
        - **Ecossistema Python para IA:** Integração natural com bibliotecas de IA/ML como LangChain, Sentence Transformers, PyTorch, FAISS, etc.
            
        - **Tipagem e Validação:** Uso de type hints do Python e Pydantic para validação automática de dados, reduzindo erros.
            
        - **Documentação Automática:** Geração automática de documentação interativa da API (Swagger UI, ReDoc).
            
    - **Alternativas Consideradas:** Node.js (Express/NestJS), Django. Node.js é performático, mas a integração com o ecossistema Python de IA seria menos direta. Django é robusto, mas considerado mais "pesado" e com uma curva de aprendizado maior para APIs simples em comparação com FastAPI.
        
- **Banco de Dados e BaaS (Backend as a Service):**
    
    - **Decisão:** **Supabase (utilizando PostgreSQL)**
        
    - **Justificativa:**
        
        - **Produtividade:** Oferece autenticação, banco de dados PostgreSQL, storage, Functions (Edge/Serverless) e Realtime em uma plataforma integrada, acelerando o desenvolvimento.
            
        - **PostgreSQL:** Banco de dados relacional robusto, confiável e com funcionalidades avançadas (como pgvector para RAG Pós-MVP).
            
        - **Autenticação:** Solução de autenticação completa e segura (JWT, RLS, OAuth providers).
            
        - **Escalabilidade e Custo:** Plano gratuito generoso para MVP e planos pagos escaláveis.
            
        - **RLS (Row-Level Security):** Permite implementar políticas de acesso granulares diretamente no banco, simplificando a lógica de autorização no backend.
            
    - **Alternativas Consideradas:** Firebase, AWS Amplify, Backend auto-hospedado com PostgreSQL. Firebase é uma boa opção, mas a preferência por PostgreSQL e a integração mais aberta do Supabase foram decisivas. Auto-hospedagem aumentaria a carga de DevOps.
        
### 2. Ferramentas e Tecnologias de Inteligência Artificial

- **Modelos de Linguagem Ampla (LLMs):**
    
    - **Decisão:** **Google Gemini Pro e Flash**
        
    - **Justificativa:**
        
        - **Capacidades Multimodais e de Raciocínio:** Modelos poderosos com bom desempenho em tarefas de geração de texto, compreensão, tradução e raciocínio.
            
        - **Custo-Benefício:** Gemini Flash oferece uma opção mais econômica para tarefas de menor complexidade ou alto volume, enquanto Gemini Pro pode ser usado para tarefas mais exigentes.
            
        - **Integração:** APIs bem documentadas e acessíveis.
            
    - **Gateway de Acesso:** **OpenRouter** (primário) ou APIs diretas do Google.
        
        - **Justificativa OpenRouter:** Flexibilidade para testar e alternar entre diferentes modelos (incluindo de outros provedores) sem grandes alterações no código, gerenciamento de custos e rate limits.
            
    - **Alternativas Consideradas:** Modelos da OpenAI (GPT-3.5/4), Anthropic Claude. A combinação de performance, custo e a familiaridade com o ecossistema Google foram favoráveis ao Gemini para este projeto.
        
- **Ambiente de Desenvolvimento Integrado (IDE) com Foco em IA:**
    
    - **Decisão:** **Trae IDE**
        
    - **Justificativa:**
        
        - **Orquestração de Agentes:** Capacidade de configurar e gerenciar Agentes de IA Mentores customizados.
            
        - **Contextualização:** Funcionalidades para fornecer contexto do projeto aos agentes (RAG, MCP/Context7).
            
        - **Produtividade:** Integração de ferramentas de desenvolvimento com capacidades de IA.
            
    - **Alternativas Consideradas:** VS Code com plugins de IA (Copilot, Codeium). Embora poderosos para assistência de código, o Trae IDE foi escolhido pela sua promessa de orquestração de agentes e gerenciamento de contexto mais profundo, alinhado com a metodologia do projeto.
        
- **Stack Tecnológica para Retrieval Augmented Generation (RAG):**
    
    - **Framework de Orquestração RAG:** **LangChain (Python)**
        
        - **Justificativa:** Framework popular, flexível e com vasta documentação para construir aplicações com LLMs, incluindo pipelines RAG complexos. Grande comunidade e muitos módulos pré-construídos.
            
    - **Vector Store (Banco de Dados Vetorial):** **FAISS-GPU (Python, com CUDA)**
        
        - **Justificativa:** Alta performance para busca de similaridade em grandes volumes de vetores, especialmente com aceleração por GPU. Adequado para uma implementação local inicial robusta. A versão GPU foi escolhida para maximizar a velocidade de indexação e consulta, dada a disponibilidade de uma RTX 2060.
            
        - **Alternativas Consideradas:** ChromaDB, Weaviate, Supabase pgvector (Pós-MVP). FAISS oferece um bom equilíbrio entre performance e simplicidade para um setup local inicial.
            
    - **Modelo de Embedding:** **`BAAI/bge-m3` (via Sentence Transformers)**
        
        - **Justificativa:** Modelo de embedding multilíngue de última geração com excelente performance em benchmarks de recuperação. Sua capacidade de lidar com múltiplos idiomas e a qualidade dos embeddings são cruciais para o Recoloca.ai. A biblioteca Sentence Transformers simplifica seu uso.
            
        - **Alternativas Consideradas:** `all-MiniLM-L6-v2`, modelos da OpenAI (Ada). `bge-m3` foi escolhido por seu desempenho superior e capacidades multilíngues mais robustas.
            
    - **Ambiente de Desenvolvimento RAG:** **Conda (com Python 3.10)**
        
        - **Justificativa:** Conda facilita o gerenciamento de dependências complexas, especialmente para bibliotecas como PyTorch (necessário para Sentence Transformers e potencialmente para FAISS) e FAISS-GPU com suas dependências CUDA. Permite criar um ambiente isolado e reprodutível.
            
    - **Bibliotecas de Suporte RAG:**
        
        - **`pymupdf` (Fitz):** Para extração de texto de PDFs na base de conhecimento.
            
        - **`unstructured`:** Para pré-processamento e extração de dados de diversos tipos de arquivos.
            
        - **`python-dotenv`:** Para gerenciamento de variáveis de ambiente.
            
### 3. Ferramentas de Documentação e Gestão de Projeto

- **Documentação e Gestão de Conhecimento ("Documentação Viva"):**
    
    - **Decisão:** **Obsidian**
        
    - **Justificativa:** Excelente ferramenta de anotações e gestão de conhecimento baseada em Markdown. Suporte a links bidirecionais, grafos de conhecimento, plugins (Kanban, Git) e customização, ideal para a "Documentação Viva".
        
- **Controle de Versão:**
    
    - **Decisão:** **Git** (com repositório remoto no **GitHub** ou GitLab)
        
    - **Justificativa:** Padrão da indústria para controle de versão, essencial para rastreabilidade, colaboração (mesmo solo) e backup.
        
- **Gestão de Tarefas e Fluxo de Trabalho:**
    
    - **Decisão:** **Obsidian Kanban Plugin**
        
    - **Justificativa:** Integração direta com a "Documentação Viva" no Obsidian, permitindo que tarefas e documentação coexistam no mesmo ambiente.
        
### 4. Automação e DevOps

- **Automação de Fluxos de Trabalho (CI/CD, Gatilhos):**
    
    - **Decisão:** **Pipedream**
        
    - **Justificativa:** Plataforma de automação low-code/pro-code flexível para criar fluxos de trabalho que conectam diversas APIs e serviços. Útil para CI/CD, notificações, e automação de tarefas relacionadas ao RAG (ex: reindexação).
        
    - **Alternativas Consideradas:** GitHub Actions. Pipedream foi escolhido pela sua interface visual e facilidade de integração com uma gama mais ampla de serviços para um desenvolvedor solo.
        
- **Hospedagem:**
    
    - **Frontend PWA (Flutter Web):** **Vercel**
        
        - **Justificativa:** Excelente plataforma para deploy de aplicações web estáticas e PWAs, com CI/CD integrado, SSL automático e CDN global.
            
    - **Backend FastAPI (Python):** **Render**
        
        - **Justificativa:** Plataforma PaaS que simplifica o deploy de aplicações Python (e outras), com suporte a bancos de dados, cron jobs e SSL automático. Boa alternativa ao Heroku.
            
    - **BaaS (Supabase):** Gerenciado pela própria Supabase.
        
## Consequências

- **Curva de Aprendizado:** O Maestro precisará garantir proficiência ou aprofundar conhecimentos em Flutter/Dart, FastAPI, Supabase e nas ferramentas de IA/RAG (LangChain, FAISS, Sentence Transformers).
    
- **Configuração Inicial:** Haverá um esforço inicial para configurar o ambiente de desenvolvimento RAG com Conda, CUDA, PyTorch e FAISS-GPU.
    
- **Custos:**
    
    - **LLMs:** Os custos de API do Google Gemini (via OpenRouter ou direto) precisarão ser monitorados, especialmente com o crescimento do uso.
        
    - **Hospedagem:** Vercel e Render possuem planos gratuitos generosos, mas podem incorrer em custos com o aumento de tráfego/recursos. Supabase também tem um plano gratuito, com custos para maior uso.
        
    - **Pipedream:** Plano gratuito com limites, custos adicionais para maior volume de execuções.
        
- **Manutenção:** A manutenção do ambiente Conda e das dependências do RAG exigirá atenção periódica.
    
- **Integração:** Será necessário garantir uma integração fluida entre o Frontend Flutter, o Backend FastAPI e os serviços do Supabase. A comunicação entre os Agentes de IA no Trae IDE e o sistema RAG também é um ponto chave.
    
- **Flexibilidade:** A escolha do OpenRouter para LLMs e a natureza modular da stack (FastAPI para backend, Flutter para frontend) oferecem boa flexibilidade para futuras evoluções ou substituições de componentes.
    
- **Produtividade Esperada:** A combinação de FastAPI (Python rico em IA) e Flutter (UI rápida) com Supabase (BaaS completo) e Trae IDE (orquestração de IA) é esperada para maximizar a produtividade do desenvolvedor solo.
    
## Próximos Passos

- Implementar a configuração do ambiente de desenvolvimento RAG conforme definido.
    
- Começar a desenvolver o script de indexação RAG (`scripts/rag_indexer.py`).
    
- Refletir estas decisões nos documentos relevantes, como [[docs/03_Arquitetura_e_Design/01_HLD.md]] (v1.1) e [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.1).

## Considerações de Orquestração Inteligente

### Integração com Metodologia
- **Agentes de IA Mentores**: As ferramentas escolhidas suportam a orquestração de agentes especializados via Trae IDE
- **RAG Operacional**: Stack tecnológica RAG implementada e operacional para contextualização dos agentes
- **Documentação Viva**: Ferramentas integradas (Obsidian + Git) para manutenção da base de conhecimento
- **Medição Contínua**: Ferramentas permitem coleta de métricas de produtividade e qualidade

### Critérios de Validação
- ✅ **Produtividade**: Ferramentas aceleram desenvolvimento solo
- ✅ **IA-First**: Stack nativa para integração com LLMs e RAG
- ✅ **Escalabilidade**: Arquitetura suporta crescimento do produto
- ✅ **Metodologia**: Suporte completo à Orquestração Inteligente

## Histórico de Versões

### v1.1 (Junho 2025) - Orquestração Inteligente e Specialized Intelligence
- Atualização de status para "Aprovado"
- Adição de considerações de Orquestração Inteligente
- Alinhamento com metodologia v1.1
- Correção de referências para documentos atualizados

### v1.0 (Junho 2025) - Versão Inicial
- Definição inicial da stack tecnológica
- Análise de alternativas e justificativas
- Estabelecimento dos próximos passos

## Documentos Relacionados

- [[docs/03_Arquitetura_e_Design/01_HLD.md]] (v1.1) - High-Level Design
- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.1) - Plano Mestre
- [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v1.1) - Metodologia de Orquestração Inteligente
- [[docs/02_Requisitos/01_ERS.md]] (v1.1) - Especificação de Requisitos

**Nota:** Este ADR (v1.1) está totalmente alinhado com a metodologia de "Orquestração Inteligente" e "Specialized Intelligence" definida no [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v1.1), garantindo que as ferramentas escolhidas suportem efetivamente o desenvolvimento aumentado por IA.

--- FIM DO DOCUMENTO ADR_001_Ferramentas_Core_Recoloca.ai (v1.1) ---