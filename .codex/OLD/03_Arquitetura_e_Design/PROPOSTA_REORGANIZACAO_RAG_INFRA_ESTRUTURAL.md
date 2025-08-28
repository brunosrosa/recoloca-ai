---
sticker: lucide//folder-tree
---
# PROPOSTA DE REORGANIZAÇÃO ESTRUTURAL - RAG_INFRA

**Versão:** 1.0
**Data de Criação:** Junho de 2025
**Autor:** @AgenteM_ArquitetoTI
**Baseado em:** Análise da estrutura atual e padrões arquiteturais do projeto
**Status:** PROPOSTA - Aguardando aprovação do Maestro

## 🎯 CONTEXTO E PROBLEMA IDENTIFICADO

### Situação Atual
A pasta `rag_infra/` apresenta alguns desafios organizacionais:
- **Arquivos dispersos na raiz:** logs, READMEs, configurações misturadas
- **Cache duplicado:** Múltiplas pastas de cache em diferentes locais
- **Arquivos temporários:** Espalhados sem organização clara
- **Falta de separação clara:** Entre arquivos permanentes e temporários

### Impacto
- **Manutenibilidade reduzida:** Dificuldade para localizar arquivos específicos
- **Risco de conflitos:** Cache e logs podem sobrescrever dados importantes
- **Escalabilidade comprometida:** Estrutura não preparada para crescimento
- **Experiência de desenvolvimento prejudicada:** Navegação confusa na estrutura

## 🏗️ PROPOSTA DE NOVA ESTRUTURA

### Estrutura Reorganizada ("Future-Proof")

```
rag_infra/
├── 📁 src/                          # Código fonte principal
│   ├── core/                        # Lógica central do RAG
│   │   ├── indexer/                 # Módulos de indexação
│   │   ├── retriever/               # Módulos de recuperação
│   │   ├── embeddings/              # Gestão de embeddings
│   │   └── mcp_server/              # Servidor MCP
│   ├── utils/                       # Utilitários organizados
│   │   ├── demos/
│   │   ├── optimization/
│   │   └── maintenance/
│   └── tests/                       # Testes organizados
│       ├── unit/
│       ├── integration/
│       └── performance/
├── 📁 config/                       # Configurações centralizadas
│   ├── environments/                # Configs por ambiente
│   │   ├── development.yaml
│   │   ├── staging.yaml
│   │   └── production.yaml
│   ├── models/                      # Configurações de modelos
│   └── logging/                     # Configurações de log
├── 📁 data/                         # Dados persistentes
│   ├── indexes/                     # Índices FAISS e PyTorch
│   │   ├── faiss/
│   │   └── pytorch/
│   ├── source_documents/            # Documentação fonte
│   │   ├── arquitetura/
│   │   ├── requisitos/
│   │   ├── guias/
│   │   ├── kanban/
│   │   ├── agentes/
│   │   └── tech_stack/
│   └── embeddings/                  # Embeddings persistentes
├── 📁 temp/                         # Arquivos temporários (gitignored)
│   ├── cache/                       # Cache unificado
│   │   ├── embeddings/
│   │   ├── indexes/
│   │   └── queries/
│   ├── logs/                        # Logs centralizados
│   │   ├── application/
│   │   ├── performance/
│   │   └── errors/
│   └── processing/                  # Arquivos de processamento temporário
├── 📁 docs/                         # Documentação específica do RAG
│   ├── api/                         # Documentação da API
│   ├── architecture/                # Diagramas e decisões arquiteturais
│   ├── deployment/                  # Guias de deploy
│   └── troubleshooting/             # Guias de resolução de problemas
├── 📁 scripts/                      # Scripts de automação
│   ├── setup/                       # Scripts de configuração inicial
│   ├── deployment/                  # Scripts de deploy
│   ├── maintenance/                 # Scripts de manutenção
│   └── monitoring/                  # Scripts de monitoramento
├── 📁 reports/                      # Relatórios e métricas
│   ├── performance/                 # Relatórios de performance
│   ├── usage/                       # Relatórios de uso
│   └── quality/                     # Relatórios de qualidade
├── 📄 README.md                     # Documentação principal
├── 📄 CHANGELOG.md                  # Histórico de mudanças
├── 📄 .gitignore                    # Exclusões do Git
└── 📄 requirements.txt              # Dependências Python
```

## 🔧 PRINCÍPIOS DA REORGANIZAÇÃO

### 1. Separação de Responsabilidades
- **`src/`:** Código fonte e lógica de negócio
- **`config/`:** Configurações centralizadas e versionadas
- **`data/`:** Dados persistentes e importantes
- **`temp/`:** Arquivos temporários e cache (não versionados)
- **`docs/`:** Documentação específica do componente
- **`scripts/`:** Automação e ferramentas
- **`reports/`:** Saídas e relatórios

### 2. Gestão de Arquivos Temporários
- **Cache unificado:** Uma única localização em `temp/cache/`
- **Logs centralizados:** Organizados por tipo em `temp/logs/`
- **Gitignore estratégico:** Pasta `temp/` completamente ignorada
- **Limpeza automática:** Scripts para limpeza periódica

### 3. Escalabilidade e Manutenibilidade
- **Estrutura modular:** Fácil adição de novos componentes
- **Configuração por ambiente:** Suporte a dev/staging/prod
- **Documentação integrada:** Docs específicos do componente
- **Automação:** Scripts para tarefas repetitivas

### 4. Conformidade com Padrões do Projeto
- **Clean Architecture:** Separação clara de camadas
- **Repository Pattern:** Organização de dados e acesso
- **Observabilidade:** Logs e métricas estruturados
- **Segurança:** Configurações sensíveis isoladas

## 📋 PLANO DE MIGRAÇÃO

### Fase 1: Preparação (1-2 horas)
1. **Backup completo** da estrutura atual
2. **Criação da nova estrutura** de pastas
3. **Configuração do .gitignore** atualizado
4. **Documentação** da migração

### Fase 2: Migração de Código (2-3 horas)
1. **Mover código fonte** para `src/`
2. **Reorganizar configurações** em `config/`
3. **Migrar dados persistentes** para `data/`
4. **Atualizar imports** e referências

### Fase 3: Configuração de Temporários (1 hora)
1. **Configurar cache unificado** em `temp/cache/`
2. **Centralizar logs** em `temp/logs/`
3. **Criar scripts de limpeza** automática
4. **Testar funcionamento** do sistema

### Fase 4: Validação e Documentação (1 hora)
1. **Testes de integração** completos
2. **Validação de performance** (não deve degradar)
3. **Atualização da documentação** (HLD, READMEs)
4. **Criação de ADR** documentando a decisão

## 🎯 BENEFÍCIOS ESPERADOS

### Imediatos
- **Organização clara:** Cada arquivo em seu lugar apropriado
- **Cache unificado:** Eliminação de duplicações
- **Logs centralizados:** Melhor observabilidade
- **Navegação intuitiva:** Estrutura autoexplicativa

### Médio Prazo
- **Manutenibilidade:** Facilidade para localizar e modificar componentes
- **Escalabilidade:** Estrutura preparada para crescimento
- **Colaboração:** Novos desenvolvedores se orientam rapidamente
- **Automação:** Scripts organizados facilitam CI/CD

### Longo Prazo
- **Evolução arquitetural:** Base sólida para mudanças futuras
- **Conformidade:** Alinhamento com padrões enterprise
- **Observabilidade:** Monitoramento e debugging eficientes
- **Segurança:** Isolamento adequado de configurações sensíveis

## ⚠️ RISCOS E MITIGAÇÕES

### Riscos Identificados
1. **Quebra de funcionalidade:** Imports e referências podem falhar
2. **Perda de dados:** Cache e logs podem ser perdidos
3. **Downtime:** Sistema pode ficar indisponível durante migração
4. **Regressão de performance:** Nova estrutura pode impactar velocidade

### Mitigações
1. **Backup completo** antes da migração
2. **Migração incremental** com validação em cada etapa
3. **Testes automatizados** para validar funcionalidade
4. **Rollback plan** documentado e testado
5. **Monitoramento** de performance durante e após migração

## 🔄 PRÓXIMOS PASSOS

1. **Aprovação do Maestro:** Validação da proposta e autorização para execução
2. **Refinamento do plano:** Ajustes baseados no feedback
3. **Agendamento da migração:** Definição de janela de manutenção
4. **Execução controlada:** Implementação seguindo o plano de migração
5. **Validação e documentação:** Confirmação do sucesso e atualização de docs

## 📚 REFERÊNCIAS

- [[docs/03_Arquitetura_e_Design/01_HLD.md]] - Arquitetura atual do sistema
- [[docs/03_Arquitetura_e_Design/03_STYLE_GUIDE.md]] - Padrões do projeto
- [[docs/02_Requisitos/01_ERS.md]] - Requisitos não funcionais
- **Clean Architecture Principles** - Robert C. Martin
- **Repository Pattern** - Domain-Driven Design

---

**Nota:** Esta proposta visa criar uma estrutura "à prova de futuro" que suporte o crescimento e evolução do sistema RAG, mantendo a organização, performance e manutenibilidade como prioridades principais.