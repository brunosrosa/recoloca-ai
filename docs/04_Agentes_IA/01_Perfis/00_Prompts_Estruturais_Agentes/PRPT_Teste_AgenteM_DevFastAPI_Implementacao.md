# 🧪 Prompt de Teste - @AgenteM_DevFastAPI (Implementação)

**Versão:** 1.0  
**Data:** Junho 2025  
**Tipo:** Teste de Caso de Uso Real e Implementação Prática  
**Agente Alvo:** @AgenteM_DevFastAPI  
**Objetivo:** Validar capacidades de implementação, desenvolvimento de código e aplicação prática

---

## 🎯 Prompt de Teste

```
@AgenteM_DevFastAPI, vamos trabalhar juntos numa implementação real e crítica:

**Contexto:** Preciso que você implemente o primeiro endpoint crítico do Recoloca.ai - o sistema de autenticação de usuários. Esta é uma funcionalidade fundamental que outros componentes dependem.

**Sua missão como desenvolvedor backend sênior:**

## 1. 🎯 Análise de Requisitos
- Esta implementação está alinhada com as prioridades da Fase 0?
- Que requisitos do ERS.md são relevantes para autenticação?
- Quais são as dependências técnicas (Supabase, JWT, etc.)?
- Que considerações de segurança são críticas?

## 2. 📋 Design da API
**Projete e implemente os endpoints de autenticação:**
- POST /auth/register - Registro de usuários
- POST /auth/login - Login com email/senha
- POST /auth/refresh - Renovação de token
- GET /auth/me - Perfil do usuário autenticado
- POST /auth/logout - Logout seguro

**Para cada endpoint, defina:**
- Modelos Pydantic de request/response
- Validações de entrada
- Códigos de status HTTP apropriados
- Documentação OpenAPI

## 3. 🛠️ Implementação Técnica
**Desenvolva o código FastAPI completo:**
- Estrutura de diretórios adequada
- Modelos de dados com Pydantic
- Routers e dependências
- Integração com Supabase Auth
- Middleware de autenticação
- Tratamento de erros

## 4. 🔒 Segurança e Validação
- Implementar hash seguro de senhas
- Validação robusta de email e senha
- Rate limiting para endpoints sensíveis
- Sanitização de dados de entrada
- Logs de segurança apropriados

## 5. 🧪 Testes Automatizados
**Crie testes abrangentes:**
- Testes unitários para cada função
- Testes de integração para endpoints
- Testes de segurança (tentativas de invasão)
- Mocks para Supabase
- Fixtures de dados de teste

## 6. 📊 Observabilidade
- Logs estruturados com contexto
- Métricas de performance
- Health checks
- Monitoramento de erros
- Alertas para falhas de autenticação

## 7. 📚 Documentação
- Docstrings detalhadas
- README com instruções de setup
- Exemplos de uso da API
- Guia de troubleshooting
- Documentação de deployment

**Entregáveis Esperados:**
1. Código Python/FastAPI completo e funcional
2. Testes automatizados com boa cobertura
3. Documentação técnica clara
4. Configuração de ambiente de desenvolvimento
5. Scripts de deployment e migração

**Importante:** Use nossa documentação como base e siga os padrões estabelecidos no projeto.
```

---

## ✅ Critérios de Sucesso Esperados

### **Qualidade do Código**
- [ ] Código Python limpo e bem estruturado
- [ ] Seguimento de padrões PEP 8 e type hints
- [ ] Aplicação de princípios SOLID e Clean Architecture
- [ ] Uso adequado de async/await
- [ ] Tratamento robusto de erros

### **Implementação FastAPI**
- [ ] Endpoints bem definidos e documentados
- [ ] Modelos Pydantic apropriados
- [ ] Validação adequada de dados
- [ ] Códigos de status HTTP corretos
- [ ] Documentação OpenAPI automática

### **Integração e Segurança**
- [ ] Integração correta com Supabase
- [ ] Implementação segura de autenticação
- [ ] Validações de segurança adequadas
- [ ] Rate limiting implementado
- [ ] Logs de segurança apropriados

### **Testes e Qualidade**
- [ ] Testes unitários abrangentes
- [ ] Testes de integração funcionais
- [ ] Cobertura de código > 80%
- [ ] Testes de casos extremos
- [ ] Mocks e fixtures adequados

### **Documentação e Manutenibilidade**
- [ ] Documentação técnica clara
- [ ] Comentários e docstrings úteis
- [ ] README com instruções completas
- [ ] Configuração de ambiente documentada
- [ ] Guias de deployment

---

## 🔍 Indicadores de Falha

### **Problemas Críticos**
- [ ] Código não funcional ou com erros graves
- [ ] Falhas de segurança evidentes
- [ ] Não integra com Supabase
- [ ] Ausência de testes básicos
- [ ] Documentação inexistente ou inadequada

### **Problemas Menores**
- [ ] Código mal estruturado ou difícil de manter
- [ ] Validações insuficientes
- [ ] Testes com baixa cobertura
- [ ] Documentação incompleta
- [ ] Performance inadequada

---

## 📊 Métricas de Avaliação Detalhadas

### **Implementação Técnica (1-5)**
- Qualidade do código: ___/5
- Arquitetura e estrutura: ___/5
- Uso correto do FastAPI: ___/5
- Integração com Supabase: ___/5
- Performance e otimização: ___/5

### **Segurança e Robustez (1-5)**
- Implementação de autenticação: ___/5
- Validações de segurança: ___/5
- Tratamento de erros: ___/5
- Rate limiting: ___/5
- Logs e monitoramento: ___/5

### **Testes e Qualidade (1-5)**
- Cobertura de testes: ___/5
- Qualidade dos testes: ___/5
- Testes de integração: ___/5
- Mocks e fixtures: ___/5
- Testes de segurança: ___/5

### **Documentação e Manutenibilidade (1-5)**
- Documentação do código: ___/5
- README e guias: ___/5
- Documentação da API: ___/5
- Configuração de ambiente: ___/5
- Facilidade de manutenção: ___/5

**Score Total:** ___/100

---

## 🎯 Checklist de Entregáveis

### **Código Fonte**
- [ ] `/app/auth/` - Módulo de autenticação
- [ ] `/app/models/` - Modelos Pydantic
- [ ] `/app/routers/` - Endpoints da API
- [ ] `/app/core/` - Configurações e dependências
- [ ] `/app/middleware/` - Middleware de autenticação

### **Testes**
- [ ] `/tests/unit/` - Testes unitários
- [ ] `/tests/integration/` - Testes de integração
- [ ] `/tests/fixtures/` - Dados de teste
- [ ] `conftest.py` - Configuração de testes
- [ ] Relatório de cobertura

### **Documentação**
- [ ] `README.md` - Guia principal
- [ ] `SETUP.md` - Configuração de ambiente
- [ ] `API.md` - Documentação da API
- [ ] `SECURITY.md` - Considerações de segurança
- [ ] `DEPLOYMENT.md` - Guia de deployment

### **Configuração**
- [ ] `requirements.txt` - Dependências Python
- [ ] `.env.example` - Variáveis de ambiente
- [ ] `docker-compose.yml` - Ambiente de desenvolvimento
- [ ] `pytest.ini` - Configuração de testes
- [ ] `.gitignore` - Arquivos ignorados

---

## 📝 Notas de Avaliação

**Data do Teste:** ___________  
**Duração da Implementação:** ___________  
**Status:** [ ] Aprovado [ ] Reprovado [ ] Necessita Ajustes  

**Pontos Fortes:**
```
[Aspectos que se destacaram positivamente]
```

**Áreas de Melhoria:**
```
[Aspectos que precisam ser aprimorados]
```

**Feedback Específico:**
```
[Comentários detalhados sobre a implementação]
```

**Próximos Passos:**
- [ ] Agente aprovado para produção
- [ ] Implementar melhorias sugeridas
- [ ] Testar integração com outros agentes
- [ ] Configurar ambiente de desenvolvimento
- [ ] Iniciar desenvolvimento do próximo módulo

---

**Criado por:** @AgenteM_Orquestrador  
**Baseado em:** PRPT_Teste_AgenteM_Orquestrador_Orquestracao.md