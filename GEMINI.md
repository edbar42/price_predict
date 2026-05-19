# 🏡 Projeto de Ciência de Dados: Predição de Preços de Imóveis

Este documento (`GEMINI.md`) serve como guia de contexto, estrutura e diretrizes para o desenvolvimento do projeto de Machine Learning voltado à predição de preços de casas (`SalePrice`). O objetivo principal é superar o desempenho do modelo base (`metricas_baseline.txt`) em uma competição acadêmica utilizando a linguagem **Python**.

---

## 📌 1. Visão Geral do Projeto

O desafio consiste em construir um modelo preditivo robusto utilizando técnicas avançadas de Engenharia de Recursos (*Feature Engineering*) e algoritmos de machine learning para estimar o valor de venda de habitações.

* **Variável Alvo (Target):** `SalePrice` (O preço de venda da propriedade em dólares).
* **Gerenciador de Pacotes:** `uv` (Para adicionar novas dependências ao projeto, utilize o comando `uv add <pacote>`).
* **Ambiente de Execução:** Notebooks Jupyter (`.ipynb`) para análise exploratória, experimentos e modelagem rápida.
* **Abordagem:** Aprendizado de Máquina Supervisionado (Regressão).

---

## 📂 2. Estrutura do Diretório

De acordo com a estrutura atual do repositório, os arquivos estão organizados da seguinte forma:

```text
├── .venv/                     # Ambiente virtual gerenciado pelo uv
├── data/                      # Diretório contendo os dados do projeto
│   ├── descricao_dados.txt    # Documentação oficial com o significado de cada feature
│   ├── metricas_baseline.txt  # Desempenho do modelo base (métrica a ser superada)
│   ├── teste_publico.csv      # Conjunto de dados de teste para avaliação da competição
│   └── treino.csv             # Conjunto de dados estruturado para treino e validação
├── notebooks/
│   └── notebook.ipynb         # Notebook para análise exploratória, testes e modelagem
├── outputs/                   # Pasta destinada a salvar predições geradas ou modelos exportados
├── reports/                   # Pasta destinada a relatórios ou gráficos salvos
├── .python-version            # Definição da versão do Python utilizada pelo uv
├── GEMINI.md                  # Este arquivo de contexto para a IA
├── main.py                    # Script principal de execução do projeto
├── modelo_baseline.joblib     # Arquivo binário contendo o modelo base treinado
├── pipeline.py                # Script contendo funções de pré-processamento e engenharia de features
├── pyproject.toml             # Configurações de dependências do projeto gerenciadas pelo uv
├── README.md                  # Documentação principal do repositório para o usuário
├── requirements.txt           # Dependências legadas (se necessário exportar)
└── uv.lock                    # Arquivo de trava de versões estritas do uv
```