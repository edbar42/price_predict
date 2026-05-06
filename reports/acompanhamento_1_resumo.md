# Acompanhamento 1 - EDA e estrategia inicial

## Visao geral do dataset

O projeto usa o dataset House Prices de Ames, Iowa, com objetivo de prever `SalePrice`. O arquivo de treino possui **1168 linhas e 81 colunas**; o arquivo de teste publico possui **1459 linhas e 80 colunas**. A coluna `SalePrice` esta presente apenas no treino, como esperado, e `Id` aparece nos dois arquivos apenas como identificador, portanto nao deve ser usada como variavel preditiva.

Foram identificadas **38 variaveis numericas** e **43 variaveis categoricas** no treino. O baseline informado pelo professor fica como referencia inicial:

```text
RESULTADOS MODELO BASELINE (LINEAR REGRESSION)
=======================================================
Metrica RMSLE: 0.17543
Metrica RMSE:  $ 36,061.40
Metrica MAE:   $ 22,186.99
Metrica R2:    0.83046
-------------------------------------------------------
Total de amostras avaliadas: 292
```

## Variavel alvo

`SalePrice` apresenta assimetria positiva: poucos imoveis muito caros puxam a cauda direita da distribuicao. Estatisticas principais:

| Estatistica | Valor |
|---|---:|
| Contagem | 1168 |
| Media | 181441.54 |
| Mediana | 165000 |
| Desvio padrao | 77263.58 |
| Minimo | 34900 |
| Q1 | 130000 |
| Q3 | 214900 |
| Maximo | 745000 |

A transformacao `np.log1p(SalePrice)` deixa a distribuicao mais proxima de uma forma simetrica e conversa diretamente com a metrica RMSLE, que penaliza erros relativos em escala logaritmica. No pipeline futuro, se o modelo for treinado no log, as predicoes precisam voltar para dolares com `np.expm1`; o retorno final nao deve ser em log.

## Correlacoes numericas

Correlacoes positivas mais fortes com `SalePrice`:

- `OverallQual`: 0.786
- `GrLivArea`: 0.696
- `GarageCars`: 0.641
- `GarageArea`: 0.624
- `TotalBsmtSF`: 0.598
- `1stFlrSF`: 0.588
- `FullBath`: 0.553
- `TotRmsAbvGrd`: 0.520
- `YearBuilt`: 0.517
- `YearRemodAdd`: 0.509

Correlacoes negativas mais fortes:

- `EnclosedPorch`: -0.150
- `KitchenAbvGr`: -0.143
- `MSSubClass`: -0.088
- `OverallCond`: -0.074
- `BsmtHalfBath`: -0.048
- `MiscVal`: -0.020
- `Id`: -0.020
- `LowQualFinSF`: -0.011

As variaveis `OverallQual`, `GrLivArea`, `GarageCars`, `GarageArea`, `TotalBsmtSF`, `1stFlrSF`, `YearBuilt`, `FullBath` e `TotRmsAbvGrd` aparecem como bons pontos de partida para modelagem. A interpretacao geral e coerente: qualidade geral, area util, garagem, porao e idade da construcao estao fortemente ligadas ao preco.

## Variaveis categoricas

Variaveis como `Neighborhood`, `ExterQual`, `KitchenQual`, `BsmtQual`, `GarageType`, `SaleCondition` e `MSZoning` devem ser preservadas e codificadas no pipeline futuro. `Neighborhood` mostra diferencas relevantes de mediana entre bairros; variaveis ordinais de qualidade, como `ExterQual` e `KitchenQual`, tambem tendem a separar faixas de preco. Para graficos e analises, categorias numerosas devem ser ordenadas por mediana de `SalePrice` ou limitadas as mais frequentes para evitar visualizacoes poluidas.

## Dados faltantes

Principais colunas com nulos no treino:

- `PoolQC`: 1162 nulos (99.49%), categorica, sem piscina
- `MiscFeature`: 1122 nulos (96.06%), categorica, sem recurso extra
- `Alley`: 1094 nulos (93.66%), categorica, sem acesso por beco
- `Fence`: 935 nulos (80.05%), categorica, sem cerca
- `MasVnrType`: 683 nulos (58.48%), categorica, sem revestimento de alvenaria
- `FireplaceQu`: 547 nulos (46.83%), categorica, sem lareira
- `LotFrontage`: 217 nulos (18.58%), numerica, frente do lote ausente ou nao medida
- `GarageQual`: 64 nulos (5.48%), categorica, possivelmente sem garagem
- `GarageType`: 64 nulos (5.48%), categorica, possivelmente sem garagem
- `GarageFinish`: 64 nulos (5.48%), categorica, possivelmente sem garagem
- `GarageYrBlt`: 64 nulos (5.48%), numerica, possivelmente sem garagem
- `GarageCond`: 64 nulos (5.48%), categorica, possivelmente sem garagem
- `BsmtQual`: 28 nulos (2.40%), categorica, possivelmente sem porao
- `BsmtExposure`: 28 nulos (2.40%), categorica, possivelmente sem porao
- `BsmtFinType2`: 28 nulos (2.40%), categorica, possivelmente sem porao
- `BsmtFinType1`: 28 nulos (2.40%), categorica, possivelmente sem porao
- `BsmtCond`: 28 nulos (2.40%), categorica, possivelmente sem porao
- `MasVnrArea`: 6 nulos (0.51%), numerica, sem revestimento de alvenaria
- `Electrical`: 1 nulo (0.09%), categorica, dado faltante pontual

O dicionario de dados indica que varios `NaN` nao significam erro de coleta, mas ausencia real do recurso. Exemplos importantes: `PoolQC` indica sem piscina; `MiscFeature`, sem recurso extra; `Alley`, sem acesso por beco; `Fence`, sem cerca; `FireplaceQu`, sem lareira; colunas de garagem indicam possivel ausencia de garagem; e colunas de porao indicam possivel ausencia de porao.

Separacao recomendada:

- Nulos com significado de ausencia: `PoolQC`, `MiscFeature`, `Alley`, `Fence`, `FireplaceQu`, campos de `Garage*`, campos de `Bsmt*`, `MasVnrType`.
- Nulos numericos que podem receber 0 quando representam ausencia do recurso: `GarageYrBlt`, `GarageArea`, `GarageCars`, `BsmtFinSF1`, `BsmtFinSF2`, `BsmtUnfSF`, `TotalBsmtSF`, `MasVnrArea`, quando aplicavel.
- Nulos que parecem faltantes reais ou medida indisponivel: `LotFrontage` e `Electrical`.
- Categorizacao futura: preencher ausencia estrutural com `"None"`; dados faltantes reais com `"Missing"` ou mediana/moda, conforme o tipo.

## Outliers

Foram investigadas `GrLivArea`, `LotArea`, `TotalBsmtSF`, `GarageArea` e `SalePrice`. Pontos extremos existem e nao devem ser removidos automaticamente neste acompanhamento.

Casos extremos em `GrLivArea`:

- Id 1183: `GrLivArea=4476`, `SalePrice=745000`, `OverallQual=10`
- Id 524: `GrLivArea=4676`, `SalePrice=184750`, `OverallQual=10`
- Id 1299: `GrLivArea=5642`, `SalePrice=160000`, `OverallQual=10`

Maiores lotes por `LotArea`:

- Id 314: `LotArea=215245`, `SalePrice=375000`, `Neighborhood=Timber`
- Id 336: `LotArea=164660`, `SalePrice=228950`, `Neighborhood=Timber`
- Id 250: `LotArea=159000`, `SalePrice=277000`, `Neighborhood=ClearCr`
- Id 707: `LotArea=115149`, `SalePrice=302000`, `Neighborhood=ClearCr`
- Id 1299: `LotArea=63887`, `SalePrice=160000`, `Neighborhood=Edwards`

Casos de area muito alta com preco relativamente baixo podem distorcer regressao linear e aumentar erro em validacao. A estrategia para o Acompanhamento 2 deve testar remocao ou tratamento apenas com justificativa e validacao cruzada.

## Estrategia de limpeza para o Acompanhamento 2

- Remover `Id` das features.
- Separar `X` e `y`; aplicar `np.log1p` em `SalePrice` durante o treino.
- Preencher categoricas com `"None"` quando o nulo significa ausencia do recurso e `"Missing"` quando for dado faltante real.
- Aplicar `OneHotEncoder(handle_unknown="ignore")` nas categoricas.
- Preencher numericas com mediana ou 0 conforme o significado do atributo.
- Considerar `StandardScaler` para modelos lineares.
- Usar `ColumnTransformer` e `Pipeline` do Scikit-Learn.
- Evitar data leakage: imputadores, scaler e encoder devem ser ajustados somente no treino.
- Usar validacao cruzada e comparar Linear Regression, Ridge, Lasso, ElasticNet, Random Forest, Gradient Boosting e XGBoost se a dependencia for viavel.
- Salvar futuramente o modelo final como `.joblib` ou `.pkl`.
- Manter `pipeline.py` retornando apenas `np.array`, `list` ou `pd.Series` com valores continuos preditos, na mesma ordem do arquivo de teste.

## Proximos passos

No Acompanhamento 2, implementar o pipeline de treino/validacao com preprocessamento dentro de `Pipeline`, comparar modelos contra o baseline RMSLE `0.17543` e decidir criterios de tratamento de outliers com base em validacao cruzada.
