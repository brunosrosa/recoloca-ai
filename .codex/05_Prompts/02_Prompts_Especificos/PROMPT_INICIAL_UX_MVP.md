# Prompt Inicial para @AgenteM_UXDesigner - MVP Recoloca.ai

**Versão:** 1.0  
**Data:** 06 de junho de 2025  
**Objetivo:** Prompt específico para iniciar o trabalho UX nos fluxos críticos do MVP

## Contexto Estratégico

**Prioridade Atual:** Validar e refinar a jornada do usuário do MVP, com foco especial no "Momento AHA!" e onboarding eficaz.

**Status do Projeto:**
- MVP definido com fluxo central: Upload CV → Kanban de vagas → Otimização por IA
- Documentação técnica em desenvolvimento
- RAG de UX Knowledge em construção (será alimentado em paralelo)
- Agentes de desenvolvimento serão configurados posteriormente

## Prompt Inicial Estruturado

```markdown
Olá @AgenteM_UXDesigner! 

Preciso da sua expertise UX para validar e refinar os fluxos críticos do MVP do Recoloca.ai. Vamos focar nos pontos que mais impactam a experiência do usuário e o sucesso do produto.

**CONTEXTO IMEDIATO:**
- **Produto:** Recoloca.ai - PWA para recolocação profissional de devs brasileiros
- **MVP Objetivo:** Demonstrar valor em <60 segundos ("Momento AHA!")
- **Usuário-alvo:** Dev Pleno/Sênior, 25-45 anos, ansioso com a busca de emprego
- **Fluxo Central:** Upload CV → Análise IA → Kanban personalizado → Insights acionáveis

**TAREFA PRIORITÁRIA:**
Analise e proponha melhorias para os 3 fluxos críticos do MVP:

1. **ONBOARDING & PRIMEIRO USO**
   - Como reduzir friction no cadastro/login?
   - Qual a sequência ideal para demonstrar valor rapidamente?
   - Como gerenciar expectativas durante o processamento do CV?
   - Que informações mínimas precisamos vs. nice-to-have?

2. **"MOMENTO AHA!" - REVELAÇÃO DE VALOR**
   - Como apresentar o Kanban personalizado de forma impactante?
   - Que insights da análise de CV geram mais "wow"?
   - Como mostrar o potencial de otimização sem sobrecarregar?
   - Qual sequência de revelação maximiza o impacto?

3. **ENGAJAMENTO CONTÍNUO - GESTÃO DO KANBAN**
   - Como tornar a gestão de vagas intuitiva e motivadora?
   - Que feedback visual mantém o usuário engajado?
   - Como balancear informação vs. simplicidade?
   - Que ações devem ser mais proeminentes?

**ENTREGÁVEIS SOLICITADOS:**

Para cada fluxo, forneça:

1. **Análise Heurística** (Nielsen's 10)
   - Identifique potenciais problemas de usabilidade
   - Priorize por impacto na experiência

2. **Fluxo de Usuário Otimizado** (Mermaid)
   - Mapeie jornada passo-a-passo
   - Inclua pontos de decisão e possíveis desvios
   - Marque momentos críticos de valor

3. **Wireframes Conceituais** (Descrição detalhada)
   - Foque nas telas/momentos mais críticos
   - Descreva layout, hierarquia de informação
   - Justifique escolhas UX

4. **UX Writing Guidelines**
   - Microcopy para reduzir ansiedade
   - Tom de voz apropriado para devs brasileiros
   - CTAs que motivam ação

5. **Métricas de Validação**
   - KPIs específicos para cada fluxo
   - Como medir sucesso do "Momento AHA!"

**RESTRIÇÕES E CONSIDERAÇÕES:**

- **Técnicas:** PWA Flutter, mobile-first, performance crítica
- **Contextuais:** Usuário pode estar no transporte público, com pressa
- **Emocionais:** Reduzir ansiedade, aumentar confiança
- **Negócio:** Conversão freemium → premium no futuro

**FONTES DE REFERÊNCIA:**
- Consulte [[docs/02_Requisitos/ERS.md]] para requisitos detalhados
- Veja [[docs/02_Requisitos/HU_AC/HU_MVP_Jornada_Usuario.md]] para jornada atual
- Use [[docs/03_Arquitetura_e_Design/STYLE_GUIDE.md]] para tom de voz
- Referencie conhecimento UX geral (quando disponível no RAG)

**ABORDAGEM SUGERIDA:**
1. Comece analisando a jornada atual documentada
2. Identifique gaps e oportunidades de melhoria
3. Proponha soluções baseadas em heurísticas estabelecidas
4. Priorize mudanças por impacto vs. esforço
5. Documente rationale por trás das decisões

**PERGUNTA INICIAL:**
Antes de começar, você gostaria de esclarecer algum aspecto específico do produto, usuário ou contexto técnico? Ou prefere que eu forneça informações adicionais sobre algum dos fluxos?

Vamos criar uma experiência que transforme a ansiedade da busca por emprego em confiança e progresso tangível! 🚀
```

## Instruções de Uso

1. **Copie o prompt** acima e cole no chat com o @AgenteM_UXDesigner configurado
2. **Aguarde a análise inicial** e responda às perguntas de esclarecimento
3. **Itere baseado no feedback** do agente
4. **Documente os resultados** para alimentar o desenvolvimento
5. **Compartilhe insights** com outros agentes quando relevante

## Próximos Passos Após Esta Tarefa

1. **Validar propostas UX** com @AgenteM_UIDesigner
2. **Refinar requisitos técnicos** baseado nas descobertas UX
3. **Atualizar documentação** com as melhorias identificadas
4. **Preparar especificações** para os agentes de desenvolvimento
5. **Planejar testes de usabilidade** quando o protótipo estiver pronto

---
**FIM DO DOCUMENTO PROMPT_INICIAL_UX_MVP.md (v1.0)**