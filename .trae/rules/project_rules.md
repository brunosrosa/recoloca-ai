```
---
# METADADOS DO PROJETO 
project_name: 'Recoloca.AI'
codex_framework_version: '3.0' # Baseado na versão do Codex Prime Framework
tech_lead: 'Bruno S. Rosa'
status: 'ativo'
document_version: '1.0'
repository_url: 'https://github.com/brunosrosa/recoloca-ai'
---
```

# Regras do Projeto: Recoloca.AI

## 1. Diretrizes Gerais e Metodologia

- **Objetivo Principal:** Desenvolver o `Recoloca.AI`, um Micro-SaaS focado em ser o "cockpit" para profissionais brasileiros em busca de recolocação. Este projeto é o primeiro produto a ser construído pela "Fábrica Janus" (na Arandu PoC), por meio do Maestro.AI e servirá como a validação final da nossa metodologia de desenvolvimento aumentado por IA.
    
- **Metodologia:** Desenvolvimento Full-Stack Ágil Aumentado por IA, com foco na entrega de valor contínuo para o usuário final, seguindo o roadmap do MVP.
    
- **Repositório Principal:** `https://github.com/brunosrosa/recoloca-ai`
    
- **Caminho da Documentação:** A documentação viva deste projeto é uma instância do `Codex Prime Framework` e reside na pasta `/Recoloca.AI/.codex/`.

## 2. Stack de Tecnologia e Ferramentas

- **Linguagem Principal (Backend):** Python 3.11+
    
- **Framework Principal (Backend):** FastAPI
    
- **Linguagem Principal (Frontend):** Dart
    
- **Framework Principal (Frontend):** Flutter (para Web, com futura expansão para Mobile)
    
- **Banco de Dados:** PostgreSQL (via Supabase)
    
- **Plataforma de Deploy Alvo:** Backend como contêiner Docker em VPS (Ubuntu); Frontend como aplicação web estática.
    
- **Ferramentas de Qualidade:**
    
    - **Backend:** Pytest, Black, Flake8, MyPy
        
    - **Frontend:** Testes de Widget e Integração do Flutter
        

## 3. Padrões de Código e Versionamento

- **Convenção de Nomenclatura:**
    
    - **Arquivos de Documentação:** `MAIUSCULA_COM_UNDERLINE`
        
    - **Arquivos de Código Python:** `snake_case` (ex: `user_service.py`)
        
    - **Arquivos de Código Dart:** `snake_case` (ex: `user_profile_screen.dart`)
        
- **Estilo de Commits:** Utilizar estritamente o padrão de **Conventional Commits** (ex: `feat(kanban):`, `fix(auth):`, `docs:`) para manter um histórico claro e automatizável.
    
- **Guia de Estilo de Código:** Aderir rigorosamente aos guias de estilo oficiais: **PEP 8** para Python e as diretrizes do **Effective Dart** para Flutter.
    

## 4. Hierarquia e Delegação de Agentes

- **Agente Estratégico (Chefe de Gabinete):** `@Janus`
    
- **Agente Tático (Gerente de Projetos):** `@Orquestrador`
    
- **Agentes Especialistas Principais:**
    
    - `@DevPython_FastAPI` (Desenvolvimento do Backend e da lógica de negócio)
        
    - `@DevFlutter` (Desenvolvimento da interface e componentes do frontend)
        
    - `@Designer_UI_UX` (Projeta a experiência do usuário e o design visual do produto)
        
    - `@QA_Tester_FullStack` (Responsável pelos testes de integração ponta-a-ponta)
        

## 5. Protocolo de Resolução de Conflitos

Em caso de conflito ou ambiguidade entre diferentes fontes de regras, a seguinte hierarquia de prioridade **DEVE** ser seguida:

1. **Decisão explícita e atual do Maestro:** Uma instrução direta de Bruno S. Rosa sempre tem a maior prioridade.
    
2. **`project_rules.md` (Este Documento):** As regras específicas para o projeto `Recoloca.AI`.
    
3. **`user_rules.md`:** As regras e preferências globais do Maestro.
    
4. **`CONSTITUICAO-PRINCIPIOS_FUNDAMENTAIS-v1.0.md`:** A constituição geral do ecossistema.
    
5. **Documentação Técnica Viva do Projeto:** Decisões formalizadas em ADRs, HLDs e outros documentos na pasta `./docs/`.
    
6. **Padrões Gerais da Indústria e da Linguagem.**
    

O agente que identificar um conflito tem a responsabilidade de sinalizá-lo e solicitar orientação para garantir o alinhamento.