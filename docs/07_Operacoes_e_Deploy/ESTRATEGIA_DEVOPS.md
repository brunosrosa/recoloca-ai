# Estratégia de DevOps para o Recoloca.ai (MVP)

**Versão:** 0.1
**Data:** 2025-06-07
**Autores:** `@AgenteOrquestrador`, `@Maestro`

## 1. Visão Geral e Objetivos

Esta estratégia de DevOps visa estabelecer um processo de Integração Contínua (CI) e Entrega Contínua (CD) simples, eficaz e confiável para o MVP do Recoloca.ai, utilizando GitHub Actions. O foco principal é automatizar tarefas repetitivas, garantir a qualidade do código e agilizar o processo de deploy para o backend (FastAPI) e frontend (Flutter PWA).

**Objetivos Principais para o MVP:**

*   **Agilidade:** Reduzir o tempo e esforço manual nos deploys.
*   **Qualidade:** Integrar verificações básicas de qualidade (linting, formatação) no pipeline.
*   **Consistência:** Garantir que os deploys sejam feitos de forma padronizada.
*   **Simplicidade:** Manter a configuração do pipeline o mais simples possível, evoluindo conforme a necessidade.

## 2. Ferramentas e Tecnologias

*   **Orquestrador de CI/CD:** GitHub Actions.
*   **Controle de Versão:** Git (com repositório no GitHub).
*   **Backend:** Python com FastAPI.
*   **Frontend:** Flutter (Dart) para PWA.
*   **Hospedagem (a definir/confirmar):**
    *   Backend FastAPI: (Ex: Vercel, Render, Heroku, Google Cloud Run, AWS Elastic Beanstalk)
    *   Frontend Flutter PWA: (Ex: Firebase Hosting, Vercel, Netlify, GitHub Pages)
    *   Banco de Dados: Supabase (já definido).

## 3. Estrutura dos Pipelines (GitHub Actions)

Serão configurados pipelines separados para o backend e o frontend.

### 3.1. Pipeline de CI/CD para o Backend (FastAPI)

**Gatilhos:**

*   Push para a branch `main` (ou `master`).
*   Push para branches de `feature/*` (para CI, sem deploy automático para produção).
*   Pull Requests para `main`.

**Etapas (Workflow):**

1.  **Checkout do Código:** Obter a versão mais recente do código da branch correspondente.
2.  **Configuração do Ambiente Python:**
    *   Selecionar a versão do Python (conforme `environment.yml` ou `requirements.txt`).
    *   Instalar dependências (usando `pip install -r requirements.txt`).
3.  **Linting e Formatação:**
    *   Executar `flake8` ou similar para linting.
    *   Executar `black` ou `autopep8` para verificação de formatação (ou aplicar formatação).
4.  **Testes Unitários:**
    *   Executar testes com `pytest`.
    *   (Opcional MVP) Gerar relatório de cobertura de testes.
5.  **Testes de Integração (Pós-MVP Inicial):**
    *   Prever a inclusão de testes de integração automatizados que verifiquem a interação entre o backend e o Supabase, e potencialmente entre diferentes módulos do backend.
    *   Estes testes seriam executados após os testes unitários em branches de feature e antes do deploy para staging/produção.
5.  **Build (se aplicável):**
    *   Para FastAPI, geralmente não há um passo de "build" explícito como em linguagens compiladas, mas pode envolver a criação de uma imagem Docker se essa for a estratégia de deploy.
6.  **Deploy (condicional, apenas para a branch `main` após merge de PR aprovado):**
    *   **Estratégia Inicial Simples:** Deploy direto para a plataforma de hospedagem escolhida (ex: usando CLI da Vercel, Render, etc.).
    *   **Credenciais:** Utilizar GitHub Secrets para armazenar tokens de API e outras credenciais necessárias para o deploy.

### 3.2. Pipeline de CI/CD para o Frontend (Flutter PWA)

**Gatilhos:**

*   Push para a branch `main` (ou `master`).
*   Push para branches de `feature/*` (para CI, sem deploy automático para produção).
*   Pull Requests para `main`.

**Etapas (Workflow):**

1.  **Checkout do Código:** Obter a versão mais recente do código da branch correspondente.
2.  **Configuração do Ambiente Flutter/Dart:**
    *   Selecionar a versão do Flutter SDK.
3.  **Instalar Dependências:**
    *   Executar `flutter pub get`.
4.  **Análise Estática e Formatação:**
    *   Executar `flutter analyze`.
    *   Executar `dart format --set-exit-if-changed .`
5.  **Testes Unitários e de Widgets:**
    *   Executar `flutter test`.
    *   (Opcional MVP) Gerar relatório de cobertura de testes.
6.  **Testes de Integração (Frontend-Backend - Pós-MVP Inicial):**
    *   Planejar a adição de testes de integração que simulem o consumo da API do backend pelo frontend em um ambiente de teste.
7.  **Testes End-to-End (E2E - Pós-MVP):**
    *   No MVP, os testes E2E podem ser manuais.
    *   Para Pós-MVP, considerar a automação de fluxos críticos do usuário utilizando ferramentas como o `integration_test` do Flutter ou soluções baseadas em Selenium/Puppeteer para PWAs.
6.  **Build da PWA:**
    *   Executar `flutter build web --pwa-strategy=offline-first` (ou a estratégia PWA desejada).
7.  **Deploy (condicional, apenas para a branch `main` após merge de PR aprovado):**
    *   **Estratégia Inicial Simples:** Deploy dos artefatos de build (pasta `build/web`) para a plataforma de hospedagem escolhida (ex: Firebase Hosting, Vercel CLI).
    *   **Credenciais:** Utilizar GitHub Secrets.

## 4. Estratégia de Branching

*   **`main` (ou `master`):** Branch principal, reflete o estado de **produção**. Deploys para produção são feitos exclusivamente a partir desta branch, idealmente após um merge bem-sucedido da branch `develop`.
*   **`develop`:** Branch de **staging/integração**. Todas as branches de `feature` e `fix` são mergeadas aqui. Deploys para um ambiente de staging são feitos a partir desta branch para testes finais antes de promover para `main`.
*   **`feature/<nome-da-feature>`:** Branches para desenvolvimento de novas funcionalidades. São criadas a partir de `develop` e mergeadas de volta em `develop` via Pull Request.
*   **`fix/<nome-da-correcao>`:** Branches para correções de bugs. Criadas a partir de `develop` (para bugs encontrados em staging/desenvolvimento) ou `main` (para hotfixes urgentes em produção, que depois devem ser mergeados em `develop` também).
*   **`hotfix/<nome-do-hotfix>`:** Para correções críticas em produção. Criadas a partir de `main`, mergeadas de volta em `main` e depois em `develop`.

## 5. Gestão de Segredos e Configurações

*   **GitHub Secrets:** Todas as chaves de API, tokens de acesso, senhas de banco de dados e outras informações sensíveis necessárias para os pipelines (especialmente para deploy) serão armazenadas como GitHub Secrets no repositório.
*   **Arquivos de Configuração:** Configurações específicas de ambiente (ex: URLs de API, chaves públicas) que não são secretas podem ser gerenciadas em arquivos de configuração versionados (ex: `.env.example`, com os valores reais fornecidos via secrets no pipeline para criar os arquivos `.env` necessários em tempo de execução/deploy).

## 6. Monitoramento e Alertas (Pós-MVP Inicial)

*   Inicialmente, o monitoramento será focado nas saídas dos workflows do GitHub Actions para identificar falhas de build, teste ou deploy.
*   A integração com ferramentas de monitoramento de aplicação (ex: Sentry, Google Analytics para o frontend, logs da plataforma de hospedagem para o backend) será planejada para fases posteriores, alinhada com o documento [[docs/07_Metricas_e_Analytics/METRICAS_SUCESSO_BASE_MERCADO.md]].

## 7. Próximos Passos e Evolução

*   **MVP Inicial:**
    *   Configurar os workflows básicos de CI (build e teste unitário) para backend e frontend no GitHub Actions, acionados por pushes em `feature/*`, `develop` e `main`.
    *   Definir e configurar a hospedagem para backend (produção e staging) e frontend (produção e staging).
    *   Implementar o deploy manual inicial para as plataformas escolhidas (ambientes de staging e produção).
    *   Configurar o deploy automatizado via GitHub Actions:
        *   Para a branch `develop` (ambiente de staging) após merge de PR aprovado.
        *   Para a branch `main` (ambiente de produção) após merge de PR de `develop` para `main` (ou hotfix para `main`).
*   **Pós-MVP:**
    *   Implementar e automatizar testes de integração (Backend e Frontend-Backend) nos pipelines.
    *   Iniciar a automação de testes E2E para fluxos críticos.
    *   Adicionar mais etapas de qualidade (ex: análise de segurança de dependências, SAST/DAST básicos).
    *   Explorar Infraestrutura como Código (IaC) se necessário (ex: Terraform para configurações mais complexas de ambiente).
    *   Integrar com sistemas de alerta e monitoramento avançado.

## 8. Considerações de Segurança no Pipeline

*   Revisar permissões dos workflows do GitHub Actions para seguir o princípio do menor privilégio.
*   Não expor segredos nos logs.
*   Manter as actions utilizadas nos workflows atualizadas.

---
FIM DO DOCUMENTO ESTRATEGIA_DEVOPS.md (v0.1)
---