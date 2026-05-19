# Documentação de Preparação de Dados

Este documento descreve as etapas de pré-processamento executadas no conjunto de dados original (`data/treino.csv`) para a criação da versão pronta para modelagem (`data/treino_preparado.csv`).

## 1. Redução de Colinearidade (Feature Selection)

Para evitar os efeitos da multicolinearidade (onde features são altamente correlacionadas entre si, prestando as mesmas informações ao modelo de Machine Learning), adotamos uma limiar de **Pearson > 0.6**. 

Após a análise do *Heatmap*, as seguintes variáveis foram **descartadas**:
- `GarageArea` (Alta correlação com `GarageCars`)
- `1stFlrSF` (Alta correlação com `TotalBsmtSF`)
- `TotRmsAbvGrd` (Alta correlação com `GrLivArea` e `BedroomAbvGr`)
- `GarageYrBlt` (Alta correlação com `YearBuilt`)
- `2ndFlrSF` (Alta correlação com `GrLivArea`)
- `BsmtFullBath` (Alta correlação com `BsmtFinSF1`)
- `FullBath` (Alta correlação com `GrLivArea`)

A variável remanescente de cada par foi selecionada baseando-se em sua correlação individual (maior impacto) com a variável alvo `SalePrice`.

## 2. Imputação de Valores Nulos

Nenhum registro (linha) foi descartado. Para preencher os valores nulos, as seguintes estratégias foram utilizadas:

- **Nulos Estruturais (Categóricos)**: 
  Variáveis em que `NA` possui significado léxico de "Ausência do atributo" (ex: "Sem Piscina", "Sem Garagem") foram substituídos pela string literal `"None"`. 
  *Aplica-se a: Alley, BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinType2, FireplaceQu, GarageType, GarageFinish, GarageQual, GarageCond, PoolQC, Fence, MiscFeature.*
- **Nulos Reais (Categóricos)**: 
  Variáveis categóricas genéricas que possuíam valores vazios reais (ex: `Electrical`, `MasVnrType`) foram preenchidas com o valor mais comum da coluna (**Moda**).
- **Nulos (Numéricos)**: 
  Todas as variáveis numéricas com valores faltantes (ex: `LotFrontage`, `MasVnrArea`) foram preenchidas com o valor **0**.

## 3. Codificação Categórica (One-Hot Encoding)

Dado que os modelos matemáticos aceitam apenas números, as variáveis em formato texto precisaram ser convertidas. Utilizamos **One-Hot Encoding** (variáveis dummy).
Para prevenir a "Armadilha das Variáveis Dummy" (onde as colunas derivadas são perfeitamente colineares), aplicamos o conceito de descartar a primeira classe originada (`drop_first=True`).

## Resultado Final e Evolução das Variáveis

O conjunto final foi exportado para `data/treino_preparado.csv` e possui **0 valores faltantes**, sendo composto inteiramente por colunas numéricas prontas para bibliotecas como *scikit-learn* e *XGBoost*.

Abaixo está o resumo numérico de como o dataset evoluiu em quantidade de variáveis:

* **Variáveis Originais (Total: 81)**:
  * 38 Numéricas (incluindo `Id` e `SalePrice`)
  * 43 Categóricas (Texto)
* **Remoção de Colinearidade (-7 Numéricas)**:
  * Descartamos 7 colunas numéricas redundantes
  * Passamos a ter 74 variáveis (31 Numéricas e 43 Categóricas)
* **One-Hot Encoding (+222 Dummies, -43 Categóricas)**:
  * As 43 variáveis categóricas restantes foram transformadas em binárias.
  * O método gerou 222 novas colunas binárias representativas (usando `drop_first=True`).
* **Dataset Final (Total: 253)**:
  * O arquivo final preparado contém exatamente **253 variáveis** (31 numéricas conservadas + 222 binárias geradas).


## 4. Métricas Finais dos Modelos (Cross-Validation)

Abaixo apresentamos os resultados consolidados (formato comparativo com o Baseline) extraídos através de Validação Cruzada (5 folds) no conjunto de treino preparado.












## 4. Métricas Finais dos Modelos (Cross-Validation)

Abaixo apresentamos os resultados consolidados (formato comparativo com o Baseline) extraídos através de Validação Cruzada (5 folds) no conjunto de treino preparado.

```text
RESULTADOS MODELO RIDGE (L2)
=======================================================
Métrica RMSLE: 0.14622
Métrica RMSE:  $ 55,753.49
Métrica MAE:   $ 17,421.75
Métrica R²:    0.85975
-------------------------------------------------------
Total de amostras avaliadas: 1168
```

```text
RESULTADOS MODELO LASSO (L1)
=======================================================
Métrica RMSLE: 0.14968
Métrica RMSE:  $ 57,193.52
Métrica MAE:   $ 18,009.73
Métrica R²:    0.85303
-------------------------------------------------------
Total de amostras avaliadas: 1168
```

```text
RESULTADOS MODELO DECISION TREE
=======================================================
Métrica RMSLE: 0.22049
Métrica RMSE:  $ 47,678.43
Métrica MAE:   $ 28,063.84
Métrica R²:    0.68109
-------------------------------------------------------
Total de amostras avaliadas: 1168
```

```text
RESULTADOS MODELO RANDOM FOREST
=======================================================
Métrica RMSLE: 0.14910
Métrica RMSE:  $ 32,107.35
Métrica MAE:   $ 18,453.85
Métrica R²:    0.85417
-------------------------------------------------------
Total de amostras avaliadas: 1168
```

```text
RESULTADOS MODELO XGBOOST
=======================================================
Métrica RMSLE: 0.12829
Métrica RMSE:  $ 27,956.27
Métrica MAE:   $ 15,645.09
Métrica R²:    0.89204
-------------------------------------------------------
Total de amostras avaliadas: 1168
```

