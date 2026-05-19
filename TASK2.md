# 🤖 Planejamento de Modelagem Preditiva (Ajustado)

Este documento define a estratégia prática de experimentos de Machine Learning para prever o `SalePrice`, utilizando o conjunto de dados já tratado e padronizado em `data/treino_preparado.csv` (composto por **253 variáveis numéricas/binárias**). O objetivo é construir uma linha de complexidade incremental para superar o modelo base (`metricas_baseline.txt`).

---

## 🧭 Estratégia de Validação e Métrica

* **Variável Alvo (Target):** `SalePrice`.
* **Transformação Logarítmica:** Para estabilizar a variância e aproximar os dados de uma distribuição normal, o modelo será treinado utilizando o logaritmo do preço: `y = np.log1p(df['SalePrice'])`.
* **Métrica Local:** RMSE (Root Mean Squared Error) calculado sobre o logaritmo. Para a avaliação final contra o baseline do professor, faremos a inversão com `np.expm1()`.
* **Validação Cruzada:** Utilizaremos um `KFold(n_splits=5, shuffle=True, random_state=42)` para monitorar o balanço entre **Viés e Variância**, evitando que modelos complexos sofram *overfitting* devido às 253 dimensões.

---

## 🏃‍♂️ Fase 1: Modelos Lineares Regularizados (Baixa/Média Complexidade)

Como o dataset passou por um processo agressivo de One-Hot Encoding (gerando 222 variáveis dummy), a Regressão Linear comum (OLS) corre o risco de sofrer instabilidade matemática mesmo após a remoção prévia de colinearidade. Por isso, focaremos em **Regularização**.

### 1. Regressão Ridge (Penalização L2)
* **Objetivo:** Adicionar uma penalidade ao quadrado dos coeficientes para encolher pesos de variáveis menos importantes, lidando bem com a alta dimensionalidade (253 colunas).
* **Hiperparâmetro:** Ajustar o parâmetro de força `alpha` via validação cruzada (`RidgeCV`).

### 2. Regressão Lasso (Penalização L1)
* **Objetivo:** Como o Lasso consegue zerar coeficientes, ele funcionará como uma segunda camada de *Feature Selection*, identificando quais das 222 dummies geradas realmente têm impacto no preço.
* **Hiperparâmetro:** Ajustar `alpha` via `LassoCV`.

---

## 🪵 Fase 2: Modelos de Árvore (Média Complexidade)

Os modelos baseados em árvores ignoram a escala dos dados e lidam de forma nativa com interações complexas entre as variáveis numéricas remanescentes e as dummies binárias.

### 3. Árvore de Decisão (`DecisionTreeRegressor`)
* **Objetivo:** Treinar uma árvore de decisão pura para servir de benchmark não-linear.
* **Análise de Viés/Variância:** Espera-se um erro quase zero na base de treino e um erro alto na validação cruzada devido ao tamanho do espaço amostral (253 colunas), evidenciando um cenário de **alta variância (overfitting)**.

---

## 🌲 Fase 3: Aprendizado Ensemble (Alta Complexidade)

Combinação de múltiplos preditores para alcançar a estabilidade e performance necessárias para vencer a competição.

### 4. Floresta Aleatória (`RandomForestRegressor`)
* **Objetivo:** Criar um comitê de árvores em paralelo (*Bagging*). Reduz drasticamente a variância encontrada na árvore única da Fase 2.
* **Métrica:** Avaliar o ganho de performance em relação aos modelos lineares.

### 5. Gradient Boosting (XGBoost ou LightGBM)
* **Objetivo:** Modelo sequencial (*Boosting*) onde cada árvore corrige os resíduos (erros) da anterior. É o estado da arte para dados tabulares com muitas colunas esparsas (binárias).
* **Implementação:** Como os dados já estão em formato 100% numérico, o casamento com o XGBoost/LightGBM será imediato e de altíssimo desempenho.

---

## 📊 Tabela de Experimentos do Notebook

O notebook `02_modelagem_preditiva.ipynb` computará e organizará os resultados na tabela abaixo:

| Fase | Algoritmo | RMSE (Treino) | RMSE (Validação Cruzada) | Superou o Baseline? | Notas / Próximos Passos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **-** | *Baseline do Professor* | - | *[Preencher]* | - | Alvo principal da competição |
| **1.1** | Regressão Ridge (L2) | | | | Testar diferentes Alphas |
| **1.2** | Regressão Lasso (L1) | | | | Quantas colunas ele zerou? |
| **2.1** | Árvore de Decisão | | | | Avaliar o nível de overfitting |
| **3.1** | Random Forest | | | | Ajustar `n_estimators` |
| **3.2** | Gradient Boosting | | | | Modelo final candidato à submissão |

---

## 🚀 Estrutura de Código Sugerida para o Início do Notebook

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.metrics import root_mean_squared_error

# 1. Carregar os dados preparados
df = pd.read_csv('../data/treino_preparado.csv')

# 2. Separar as features e o target (removendo também o Id se houver)
X = df.drop(columns=['SalePrice', 'Id'], errors='ignore')
y = np.log1p(df['SalePrice']) # Aplicação do logaritmo no target

# 3. Definir validação cruzada estável
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print(f"Dados prontos para modelagem! Shape: {X.shape}")