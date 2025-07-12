---
sticker: lucide//folder-tree
---
# ADR-008: Reorganização Estrutural do RAG_INFRA

**Status:** PROPOSTO  
**Data:** Junho de 2025  
**Autor:** @AgenteM_ArquitetoTI  
**Revisores:** @AgenteM_Orquestrador, @AgenteM_DevFastAPI  
**Relacionado a:** [[ADR-007-Reorganizacao-RAG-Infra.md]], [[docs/03_Arquitetura_e_Design/01_HLD.md]]  

## Contexto

Após a reorganização funcional do RAG_INFRA (ADR-007), identificamos problemas estruturais na organização física dos arquivos e diretórios:

### Problemas Identificados
1. **Arquivos dispersos na raiz:** Logs, READMEs, configurações misturadas dificultam navegação
2. **Cache duplicado:** Múltiplas pastas de cache em diferentes locais causam confusão e desperdício de espaço
3. **Arquivos temporários espalhados:** Sem organização clara, dificultando limpeza e manutenção
4. **Falta de separação clara:** Entre arquivos permanentes e temporários compromete versionamento
5. **Escalabilidade comprometida:** Estrutura atual não suporta crescimento futuro do sistema

### Impacto nos Requisitos
- **RNF-MAN-001:** Manutenibilidade prejudicada pela desorganização
- **RNF-PER-002:** Performance impactada por cache fragmentado
- **RNF-ESC-001:** Escalabilidade limitada pela estrutura atual

## Decisão

Implementaremos uma **reorganização estrutural completa** do diretório `rag_infra/` seguindo princípios de Clean Architecture e padrões enterprise, criando uma estrutura "future-proof" que suporte o crescimento e evolução do sistema.

### Nova Estrutura Proposta

```
rag_infra/
├── 📁 src/                          # Código fonte principal
│   ├── core/                        # Lógica central do RAG
│   ├── utils/                       # Utilitários organizados
│   └── tests/                       # Testes organizados
├── 📁 config/                       # Configurações centralizadas
│   ├── environments/                # Configs por ambiente
│   ├── models/                      # Configurações de modelos
│   └── logging/                     # Configurações de log
├── 📁 data/                         # Dados persistentes
│   ├── indexes/                     # Índices FAISS e PyTorch
│   ├── source_documents/            # Documentação fonte
│   └── embeddings/                  # Embeddings persistentes
├── 📁 temp/                         # Arquivos temporários (gitignored)
│   ├── cache/                       # Cache unificado
│   ├── logs/                        # Logs centralizados
│   └── processing/                  # Arquivos de processamento temporário
├── 📁 docs/                         # Documentação específica do RAG
├── 📁 scripts/                      # Scripts de automação
└── 📁 reports/                      # Relatórios e métricas
```

### Princípios Arquiteturais

1. **Separação de Responsabilidades**
   - Código fonte isolado em `src/`
   - Configurações centralizadas em `config/`
   - Dados persistentes em `data/`
   - Temporários em `temp/` (não versionados)

2. **Gestão de Arquivos Temporários**
   - Cache unificado em localização única
   - Logs centralizados por categoria
   - Pasta `temp/` completamente ignorada pelo Git
   - Scripts de limpeza automática

3. **Escalabilidade e Manutenibilidade**
   - Estrutura modular para fácil extensão
   - Configuração por ambiente (dev/staging/prod)
   - Documentação integrada por componente
   - Automação através de scripts organizados

4. **Conformidade com Padrões**
   - Clean Architecture: separação clara de camadas
   - Repository Pattern: organização de dados
   - Observabilidade: logs e métricas estruturados
   - Segurança: configurações sensíveis isoladas

## Alternativas Consideradas

### 1. Manter Estrutura Atual
- **Prós:** Sem impacto imediato, sem risco de quebra
- **Contras:** Problemas persistem e se agravam com crescimento
- **Decisão:** Rejeitada - problemas se tornarão críticos

### 2. Reorganização Incremental
- **Prós:** Menor risco, mudanças graduais
- **Contras:** Período prolongado de inconsistência, complexidade de gestão
- **Decisão:** Rejeitada - inconsistência temporária seria problemática

### 3. Reorganização Completa (Escolhida)
- **Prós:** Solução definitiva, estrutura future-proof, alinhamento com padrões
- **Contras:** Risco de quebra temporária, necessita migração cuidadosa
- **Decisão:** Aceita - benefícios superam riscos com migração controlada

## Consequências

### Positivas

1. **Organização Clara**
   - Cada arquivo em localização apropriada e intuitiva
   - Navegação facilitada para desenvolvedores
   - Estrutura autoexplicativa

2. **Performance Otimizada**
   - Cache unificado elimina duplicações
   - Acesso mais eficiente a arquivos temporários
   - Logs centralizados melhoram observabilidade

3. **Manutenibilidade Aprimorada**
   - Facilidade para localizar e modificar componentes
   - Separação clara entre código e configuração
   - Scripts organizados facilitam automação

4. **Escalabilidade Garantida**
   - Estrutura preparada para crescimento
   - Fácil adição de novos componentes
   - Suporte a múltiplos ambientes

5. **Conformidade Arquitetural**
   - Alinhamento com Clean Architecture
   - Padrões enterprise implementados
   - Base sólida para evoluções futuras

### Negativas

1. **Risco de Quebra Temporária**
   - Imports e referências podem falhar durante migração
   - Sistema pode ficar indisponível brevemente
   - **Mitigação:** Backup completo + migração controlada + testes

2. **Esforço de Migração**
   - Tempo necessário para execução (6-8 horas)
   - Atualização de documentação
   - **Mitigação:** Script automatizado + plano detalhado

3. **Curva de Aprendizado**
   - Desenvolvedores precisam se adaptar à nova estrutura
   - **Mitigação:** Documentação clara + READMEs explicativos

4. **Risco de Regressão**
   - Performance pode ser impactada inicialmente
   - **Mitigação:** Monitoramento contínuo + rollback plan

## Implementação

### Plano de Migração

#### Fase 1: Preparação (1-2 horas)
1. **Backup completo** da estrutura atual
2. **Criação da nova estrutura** de pastas
3. **Configuração do .gitignore** atualizado
4. **Documentação** da migração

#### Fase 2: Migração de Código (2-3 horas)
1. **Mover código fonte** para `src/`
2. **Reorganizar configurações** em `config/`
3. **Migrar dados persistentes** para `data/`
4. **Atualizar imports** e referências

#### Fase 3: Configuração de Temporários (1 hora)
1. **Configurar cache unificado** em `temp/cache/`
2. **Centralizar logs** em `temp/logs/`
3. **Criar scripts de limpeza** automática
4. **Testar funcionamento** do sistema

#### Fase 4: Validação e Documentação (1 hora)
1. **Testes de integração** completos
2. **Validação de performance** (não deve degradar)
3. **Atualização da documentação** (HLD, READMEs)
4. **Criação de ADR** documentando a decisão

### Ferramentas de Migração

- **Script automatizado:** `scripts/reorganize_structure.py`
- **Modo dry-run:** Para validação prévia
- **Backup automático:** Antes de qualquer mudança
- **Log detalhado:** Rastreamento de todas as operações
- **Rollback plan:** Procedimento de reversão documentado

### Critérios de Sucesso

1. **Funcionalidade preservada:** Todos os testes passam após migração
2. **Performance mantida:** Sem degradação significativa (<5%)
3. **Organização alcançada:** Estrutura conforme especificação
4. **Documentação atualizada:** HLD e guias refletem nova estrutura

## Monitoramento

### Métricas de Acompanhamento

1. **Performance**
   - Tempo de indexação
   - Tempo de consulta
   - Uso de memória
   - Uso de disco

2. **Manutenibilidade**
   - Tempo para localizar arquivos
   - Facilidade de navegação
   - Feedback de desenvolvedores

3. **Estabilidade**
   - Taxa de erros
   - Disponibilidade do sistema
   - Integridade dos dados

### Plano de Rollback

Em caso de problemas críticos:

1. **Parar sistema** imediatamente
2. **Restaurar backup** completo
3. **Validar funcionamento** do sistema restaurado
4. **Investigar causa raiz** do problema
5. **Ajustar plano** de migração
6. **Reagendar** nova tentativa

## Referências

- [[ADR-007-Reorganizacao-RAG-Infra.md]] - Reorganização funcional anterior
- [[docs/03_Arquitetura_e_Design/01_HLD.md]] - Arquitetura de alto nível
- [[docs/02_Requisitos/01_ERS.md]] - Requisitos não funcionais
- **Clean Architecture** - Robert C. Martin
- **Repository Pattern** - Domain-Driven Design
- **Enterprise Integration Patterns** - Gregor Hohpe

## Aprovação

- [ ] **@AgenteM_Orquestrador** - Aprovação estratégica
- [ ] **@AgenteM_DevFastAPI** - Validação técnica
- [ ] **Maestro** - Aprovação final para execução

---

**Nota:** Esta reorganização estrutural complementa a reorganização funcional (ADR-007) e estabelece uma base sólida para o crescimento futuro do sistema RAG, garantindo manutenibilidade, escalabilidade e conformidade com padrões arquiteturais enterprise.