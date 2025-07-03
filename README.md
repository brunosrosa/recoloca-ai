# 💼 Recoloca.AI

> **O Cockpit Inteligente para a Recolocação Profissional no Brasil**
> 
> _Um produto nascido da Metodologia de Desenvolvimento Aumentado por IA_

[![Status do Projeto](https://img.shields.io/badge/status-em_desenvolvimento-yellow)](https://github.com/) [![Versão Alvo](https://img.shields.io/badge/versão-MVP_v0.1-blue)](./docs/01_PRODUTO_PRODUCT/01_ROADMAP_ESTRATEGICO.md) [![Python](https://img.shields.io/badge/python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Flutter](https://img.shields.io/badge/flutter-3.x-02569B?logo=flutter&logoColor=white)](https://flutter.dev/) [![FastAPI](https://img.shields.io/badge/fastapi-^0.111-009688?logo=fastapi)](https://fastapi.tiangolo.com/) [![PostgreSQL](https://img.shields.io/badge/postgresql-^16-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![Docker](https://img.shields.io/badge/docker-^25.0-2496ED?logo=docker&logoColor=white)](https://www.docker.com/) [![Licença](https://img.shields.io/badge/licença-pendente-lightgrey)](./LICENSE)

## 🎯 Sobre o Projeto: Duas Histórias

O `Recoloca.AI` tem duas histórias a serem contadas.

**Para o utilizador final,** é um Micro-SaaS projetado para ser o centro de controlo definitivo para profissionais brasileiros em busca de uma nova oportunidade no mercado de trabalho. A nossa missão é transformar um processo muitas vezes caótico e desorganizado numa jornada estratégica, clara e eficiente. A plataforma oferece:

- **📊 Gestão Visual Unificada:** Um Kanban intuitivo para organizar, rastrear e gerir todas as suas candidaturas.
    
- **🤖 Otimização de CV com IA:** Uma ferramenta que analisa a descrição de uma vaga e ajuda a refatorar o seu currículo para maximizar a compatibilidade.
    
- **💬 Coaching de Carreira com IA:** Um assistente proativo que fornece dicas e prepara para entrevistas.
    
- **🇧🇷 Foco no Mercado Brasileiro:** Conteúdo e análises adaptadas às nuances do Brasil.
    

**Para a comunidade de engenharia,** o `Recoloca.AI` é algo mais profundo. Ele é a **primeira Prova de Conceito** de um novo paradigma de desenvolvimento de software. Este projeto é o "carro" construído pela "fábrica" do futuro: um ecossistema onde a maior parte do ciclo de vida de desenvolvimento é executada por uma equipa de agentes de IA autónomos.

## 🏗️ A Arquitetura Real: O Ecossistema Maestro.AI

A verdadeira arquitetura do `Recoloca.AI` não é apenas o seu stack tecnológico, mas o ecossistema que o constrói e o mantém.

```
graph TD
    M[Maestro.AI] -- Orquestra --> AG(Equipa de Agentes IA);
    SE[Synapse Engine] -- Alimenta com Conhecimento --> AG;
    CP[Codex Prime Framework] -- Define as Regras --> M;
    AG -- Desenvolve e Mantém --> R(Recoloca.AI);
```

- **`Maestro.AI` (O Orquestrador):** O cockpit de engenharia onde o "Maestro Humano" supervisiona, governa e delega tarefas de alto nível para a equipa de agentes de IA. É o cérebro operacional.
    
- **`Synapse Engine` (O Cérebro Cognitivo):** A nossa plataforma de memória e conhecimento. Utilizando uma arquitetura GraphRAG, ele fornece aos agentes o contexto profundo e a memória histórica necessários para tomar decisões inteligentes.
    
- **`Codex Prime Framework` (A Constituição):** O repositório de conhecimento que contém os padrões, templates e regras que guiam todo o ecossistema. É a fonte da verdade para a cultura de engenharia.
    
- **`Recoloca.AI` (A Prova de Conceito):** O produto final. O seu desenvolvimento serve como o teste de stresse e a validação de todo o ecossistema. Seu stack de implementação é **FastAPI (Python)** para o backend, **Flutter (Dart)** para o frontend e **PostgreSQL** para a base de dados.
    

## ✅ Objetivos do MVP (Versão 0.1)

O nosso foco inicial é validar a proposta de valor central do produto com um conjunto de funcionalidades essenciais, construídas pela nossa equipa de agentes:

1. **Autenticação Segura:** Login e gestão de contas de utilizador.
    
2. **Kanban Funcional:** Gestão de vagas com funcionalidade de arrastar e soltar.
    
3. **Análise de CV (Core):** Upload de currículo e análise inicial de compatibilidade com uma vaga.
    
4. **Coach IA Básico:** Primeiras interações de coaching baseadas em prompts.
    

## 🚀 Como Começar (Getting Started)

Instruções para configurar e executar o **produto `Recoloca.AI`** localmente.

### Pré-requisitos

- Python 3.11+
    
- Flutter SDK
    
- Docker (para o banco de dados)
    
- Git
    

### Instalação

1. **Clone o repositório:**
    
    ```
    git clone [URL_DO_REPOSITORIO]
    cd Recoloca.AI
    ```
    
2. **Configure e inicie o backend:**
    
    ```
    cd src/backend_fastapi
    python -m venv .venv
    source .venv/bin/activate  # ou .\.venv\Scripts\Activate.ps1 no Windows
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    
3. **Configure e inicie o frontend:**
    
    ```
    cd src/frontend_flutter
    flutter pub get
    flutter run -d chrome
    ```
    

## 📖 Documentação

A documentação completa e viva deste projeto é uma instância do **`Codex Prime Framework`** e pode ser encontrada na pasta `/docs`.

- [**🎯 Especificação de Requisitos (ERS)**](https://gemini.google.com/app/docs/01_PRODUTO_PRODUCT/02_ESPECIFICACAO_DE_REQUISITOS.md "null")
    
- [**🗺️ Roadmap Estratégico**](https://gemini.google.com/app/docs/01_PRODUTO_PRODUCT/01_ROADMAP_ESTRATEGICO.md "null")
    
- [**🏗️ Arquitetura de Alto Nível (HLD)**](https://gemini.google.com/app/docs/03_TECNOLOGIA_ENGINEERING/01_VISAO_GERAL_DA_ARQUITETURA.md "null")
    

## 🤝 Como Contribuir

A contribuição para este projeto ocorre em dois níveis:

1. **Contribuição para o Produto (`Recoloca.AI`):** A melhor forma de contribuir é usando a aplicação, reportando bugs e sugerindo melhorias através da criação de **`Issues`** detalhadas no nosso repositório. Este é o canal principal para o feedback humano que alimenta o nosso ciclo de desenvolvimento.
    
2. **Contribuição para o Ecossistema:** Se estiver interessado na metodologia de desenvolvimento por IA, a colaboração mais valiosa é no desenvolvimento dos projetos `Codex Prime`, `Synapse Engine` e `Maestro.AI`. Consulte os respetivos repositórios e guias de contribuição.
    

## 📄 Licença

Distribuído sob a licença [Nome da Licença]. Veja `LICENSE.txt` para mais informações.

## 📞 Contato

Maestro (Desenvolvedor Principal): Bruno S. Rosa

LinkedIn: [/In/BrunoSRosa](https://linkedin.com/in/brunosrosa)