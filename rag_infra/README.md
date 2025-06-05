# README - Pasta `rag_infra` do Projeto Recoloca.ai

**Versão:** 1.1
**Data de Criação:** 03 de junho de 2025
**Data de Última Atualização:** 03 de junho de 2025
**Responsável:** Maestro (Bruno S. Rosa)

## 1. Propósito

Esta pasta (`rag_infra/`) contém o núcleo da infraestrutura de **Retrieval Augmented Generation (RAG)** para o projeto Recoloca.ai. O sistema RAG é projetado para fornecer contexto relevante e atualizado da "Documentação Viva" e outros materiais curados do projeto aos Agentes de IA Mentores, melhorando a precisão e a relevância de suas respostas e artefatos gerados.

Os principais componentes e funcionalidades gerenciados aqui incluem:
* Configuração do ambiente Python dedicado para RAG.
* Scripts para indexação da base de conhecimento.
* Scripts para teste e consulta do índice vetorial.
* Armazenamento do índice vetorial FAISS-GPU.
* Documentos fonte preparados para o RAG.

## 2. Estrutura da Pasta

```
🧑🏻‍💼 Recoloca.AI/
├── ... (outras pastas do projeto)
├── rag_infra/
│ ├── core_logic/ # Código fonte dos scripts Python para o RAG
│ │ ├── init.py
│ │ ├── constants.py # Constantes (ex: caminhos, nome do modelo)
│ │ ├── data_loader.py # Módulo para carregar e pré-processar documentos
│ │ ├── embedding_model.py # Módulo para carregar e usar o modelo de embedding
│ │ ├── rag_indexer.py # Script principal para criar/atualizar o índice FAISS
│ │ ├── rag_retriever.py # Módulo ou script para realizar consultas ao índice
│ │ └── verificar_faiss_gpu.py # Script para verificar a disponibilidade da GPU para FAISS
│ ├── data_index/ # Local para armazenar o índice FAISS e metadados associados
│ │ └── faiss_index_bge_m3/ # Subpasta específica do índice
│ ├── notebooks/ # Jupyter notebooks para experimentação e testes - OPCIONAL
│ ├── source_documents/ # Documentos fonte para o RAG
│ │ ├── PM_Knowledge/ # Materiais sobre Product Management
│ │ ├── API_Specs_Sumario_para_RAG.md
│ │ ├── ERS_para_RAG.md
│ │ ├── GUIA_AVANCADO_para_RAG.md
│ │ ├── HLD_para_RAG.md
│ │ └── STYLE_GUIDE_para_RAG.md
│ ├── environment.yml # Definição do ambiente Conda para o RAG
│ └── README.md # Este arquivo
├── ... (outras pastas do projeto)
```

**Observações sobre a estrutura:**
* A pasta `rag_infra/source_documents/` é a fonte primária dos documentos a serem indexados. Os scripts em `rag_infra/core_logic/` farão referência a este caminho.
* O índice FAISS será criado e gerenciado pelos scripts na pasta `rag_infra/data_index/faiss_index_bge_m3/`.
* **Importante:** Adicione `rag_infra/data_index/` ao seu arquivo `.gitignore` para evitar versionar os arquivos de índice binários, que podem ser grandes.
## 3. Configuração do Ambiente de Desenvolvimento (Conda)

Para garantir a reprodutibilidade e gerenciar as dependências complexas (especialmente PyTorch com CUDA e FAISS-GPU), utilizaremos um ambiente Conda definido no arquivo `rag_infra/environment.yml`.

**Pré-requisitos:**
* **NVIDIA GPU** com drivers compatíveis instalados.
* **CUDA Toolkit 12.1+** (ou a versão compatível com o **PyTorch** e **FAISS-GPU** escolhidos) instalado.
* **cuDNN** instalado e configurado corretamente.
* Miniconda ou **Anaconda** instalado.

**Passos para configurar o ambiente:**

1.  **Navegue até a pasta `rag_infra/` no seu terminal.**
2.  **Crie o ambiente Conda a partir do arquivo `environment.yml`:**
    ```bash
    conda env create -f environment.yml
    ```
    Isso criará um novo ambiente chamado `rag_env_recolocai` (ou o nome definido no `environment.yml`) com todas as dependências listadas.

3.  **Ative o ambiente recém-criado:**
    ```bash
    conda activate rag_env_recolocai
    ```

4.  **Verifique a instalação (Opcional, mas recomendado):**
    * Execute o script `verificar_faiss_gpu.py` para confirmar se o PyTorch e o FAISS conseguem acessar a GPU:
        ```bash
        conda activate rag_env_recolocai
        python rag_infra/core_logic/verificar_faiss_gpu.py
        ```
    * O script deve indicar se a GPU está disponível para PyTorch e FAISS.
## 4. Scripts Principais

(Localizados em `rag_infra/core_logic/`)

* **`rag_indexer.py`:**
    * **Propósito:** Script principal para o processo de indexação. Ele carrega documentos da pasta `rag_infra/source_documents/`, os divide em chunks, gera embeddings usando o modelo `BAAI/bge-m3` (via Sentence Transformers) e cria/atualiza o índice vetorial FAISS-GPU, salvando-o em `rag_infra/data_index/faiss_index_bge_m3/`.
    * **Como usar (exemplo):**
        ```bash
        conda activate rag_env_recolocai
        python rag_infra/core_logic/rag_indexer.py
        ```
        Pode incluir argumentos para forçar reindexação completa, especificar fontes de dados, etc.

* **`rag_retriever.py` (ou funcionalidade similar):**
    * **Propósito:** Módulo ou script que carrega o índice FAISS existente e fornece uma interface para realizar buscas por similaridade. Permite que o Maestro ou outros sistemas (como os Agentes de IA) insiram consultas de texto para recuperar os chunks de documentos mais relevantes.
    * **Como usar (exemplo, se for um script CLI para teste):**
        ```bash
        conda activate rag_env_recolocai
        python rag_infra/core_logic/rag_retriever.py --query "Sua pergunta aqui"
        ```
        Para integração, este módulo provavelmente exporá funções a serem chamadas por outros scripts ou pelo sistema de orquestração dos agentes.

* **Outros módulos (`constants.py`, `data_loader.py`, `embedding_model.py`, `vector_store.py` - nomes podem variar):**
    * Contêm a lógica reutilizável para definições de constantes (caminhos, nome do modelo), carregamento e pré-processamento de dados, manipulação do modelo de embedding e interação com o FAISS, respectivamente. São importados pelo `rag_indexer.py` e `rag_retriever.py`.
## 5. Tecnologias Chave Utilizadas

* **Linguagem:** Python 3.10
* **Gerenciamento de Ambiente:** Conda
* **Framework de Orquestração (conceitual para os scripts):** LangChain (para carregadores de documentos, text splitters, e pipeline de consulta).
* **Modelo de Embedding:** `BAAI/bge-m3` (via biblioteca Sentence Transformers).
* **Vector Store:** FAISS-GPU (para armazenamento e busca eficiente de vetores de embedding, com aceleração por GPU).
* **Processamento de PDF:** `pymupdf`
* **Outras bibliotecas:** `sentence-transformers`, `torch` (com suporte CUDA), `numpy`, `python-dotenv`, `unstructured`.
## 6. Como Usar o Sistema RAG

1.  **Configurar o Ambiente:** Siga as instruções na Seção 3.
2.  **Preparar a Base de Conhecimento:** Certifique-se de que seus documentos Markdown e outros formatos estejam atualizados e organizados na pasta `rag_infra/source_documents/`.
3.  **Executar a Indexação:**
    ```bash
    conda activate rag_env_recolocai
    python rag_infra/core_logic/rag_indexer.py
    ```
    Execute este script sempre que houver atualizações significativas na sua base de conhecimento.
4.  **Testar Consultas (Opcional, usando `rag_retriever.py` se implementado como CLI ou notebooks):**
    Use para verificar a qualidade da recuperação.
5.  **Integração com Agentes de IA (via Trae IDE ou outros scripts):**
    * Os Agentes de IA configurados no Trae IDE (ou outros sistemas de orquestração) precisarão de uma lógica para:
        1.  Receber uma pergunta/tarefa.
        2.  Formular uma consulta relevante para o RAG.
        3.  Chamar funções do módulo `rag_retriever.py` (ou similar) que carrega o índice FAISS de `rag_infra/data_index/faiss_index_bge_m3/`, gera o embedding da consulta usando `BAAI/bge-m3`, e realiza a busca por similaridade no índice.
        4.  Receber os chunks de texto recuperados.
        5.  Injetar esses chunks no prompt do LLM (Gemini) para fornecer contexto.
## 7. Considerações e Próximos Passos

* **Gerenciamento de Variáveis de Ambiente:** Considere usar um arquivo `.env` na raiz de `rag_infra/` (e adicioná-lo ao `.gitignore`) para armazenar caminhos de pastas ou outras configurações sensíveis, carregando-as com `python-dotenv` nos scripts.
* **Monitoramento de Alterações na Documentação:** Para automação, pode-se criar um script que monitora alterações na pasta `rag_infra/source_documents/` e dispara a reindexação automaticamente (possivelmente integrado com Pipedream ou hooks de Git).
* **Estratégia de Chunking:** A qualidade do RAG depende muito da estratégia de divisão de texto (chunking). Experimente diferentes tamanhos de chunk e sobreposições (overlap) no `data_loader.py` ou `rag_indexer.py`.
* **Otimização de Metadados:** Adicionar metadados aos chunks durante a indexação (ex: nome do arquivo fonte, seção do documento, data da última modificação) pode melhorar a filtragem e a relevância da recuperação.
* **Avaliação da Qualidade do RAG:** Implementar métricas mais formais para avaliar a precisão e o recall do sistema RAG (ex: usando LangSmith ou frameworks de avaliação de RAG).
* **Segurança do Índice:** Certifique-se de que o acesso à pasta `rag_infra/data_index/` seja restrito, se aplicável.

--- FIM DO DOCUMENTO README.md (rag_infra v1.1) ---