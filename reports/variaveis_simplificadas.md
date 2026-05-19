# Variáveis Simplificadas - Predição de Preços de Imóveis

Abaixo está a documentação simplificada das 81 variáveis presentes no dataset `treino.csv`.


| Variável | Tipo | Min | Max | Nulos? | Explicação e Tratamento para Nulos |
|----------|------|-----|-----|--------|------------------------------------|
| `Id` | Numérica Discreta | 1 | 1460 | Não | Identificador único da propriedade |
| `MSSubClass` | Numérica Discreta | 20 | 190 | Não | Classe do tipo de construção |
| `MSZoning` | Categórica Nominal/Ordinal | N/A | N/A | Não | Classificação de zoneamento geral |
| `LotFrontage` | Numérica Discreta | 21.0 | 313.0 | Sim | Metragem linear da rua conectada à propriedade <br>*(Nulos reais: sugere-se imputar com **0** ou com a Mediana para simular o valor faltante)* |
| `LotArea` | Numérica Discreta | 1300 | 215245 | Não | Tamanho do lote em pés quadrados |
| `Street` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipo de acesso rodoviário à propriedade |
| `Alley` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Tipo de acesso ao beco da propriedade <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `LotShape` | Categórica Nominal/Ordinal | N/A | N/A | Não | Formato geral da propriedade |
| `LandContour` | Categórica Nominal/Ordinal | N/A | N/A | Não | Nivelamento da propriedade |
| `Utilities` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipos de utilitários disponíveis |
| `LotConfig` | Categórica Nominal/Ordinal | N/A | N/A | Não | Configuração do lote |
| `LandSlope` | Categórica Nominal/Ordinal | N/A | N/A | Não | Inclinação da propriedade |
| `Neighborhood` | Categórica Nominal/Ordinal | N/A | N/A | Não | Localização física dentro da cidade de Ames |
| `Condition1` | Categórica Nominal/Ordinal | N/A | N/A | Não | Proximidade a vias ou ferrovias |
| `Condition2` | Categórica Nominal/Ordinal | N/A | N/A | Não | Proximidade a vias ou ferrovias (se houver uma segunda) |
| `BldgType` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipo de habitação |
| `HouseStyle` | Categórica Nominal/Ordinal | N/A | N/A | Não | Estilo da residência |
| `OverallQual` | Numérica Discreta | 1 | 10 | Não | Qualidade geral do material e do acabamento |
| `OverallCond` | Numérica Discreta | 1 | 9 | Não | Condição geral da residência |
| `YearBuilt` | Numérica Discreta | 1872 | 2010 | Não | Ano de construção original |
| `YearRemodAdd` | Numérica Discreta | 1950 | 2010 | Não | Ano de remodelação (igual ao ano de construção se não houve) |
| `RoofStyle` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipo de telhado |
| `RoofMatl` | Categórica Nominal/Ordinal | N/A | N/A | Não | Material do telhado |
| `Exterior1st` | Categórica Nominal/Ordinal | N/A | N/A | Não | Revestimento externo da casa |
| `Exterior2nd` | Categórica Nominal/Ordinal | N/A | N/A | Não | Revestimento externo da casa (se houver um segundo) |
| `MasVnrType` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Tipo de folheado de alvenaria <br>*(Nulos reais: sugere-se imputar com a Moda para simular o valor faltante)* |
| `MasVnrArea` | Numérica Discreta | 0.0 | 1378.0 | Sim | Área do folheado de alvenaria em pés quadrados <br>*(Nulos reais: sugere-se imputar com **0** ou com a Mediana para simular o valor faltante)* |
| `ExterQual` | Categórica Nominal/Ordinal | N/A | N/A | Não | Qualidade do material externo |
| `ExterCond` | Categórica Nominal/Ordinal | N/A | N/A | Não | Condição atual do material externo |
| `Foundation` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipo de fundação |
| `BsmtQual` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Altura do porão <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `BsmtCond` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Condição geral do porão <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `BsmtExposure` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Paredes de nível de passagem ou de jardim do porão <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `BsmtFinType1` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Qualidade da área acabada do porão <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `BsmtFinSF1` | Numérica Discreta | 0 | 5644 | Não | Pés quadrados da área acabada tipo 1 |
| `BsmtFinType2` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Qualidade da segunda área acabada do porão <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `BsmtFinSF2` | Numérica Discreta | 0 | 1127 | Não | Pés quadrados da segunda área acabada tipo 2 |
| `BsmtUnfSF` | Numérica Discreta | 0 | 2336 | Não | Pés quadrados de área não acabada do porão |
| `TotalBsmtSF` | Numérica Discreta | 0 | 6110 | Não | Total de pés quadrados da área do porão |
| `Heating` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipo de aquecimento |
| `HeatingQC` | Categórica Nominal/Ordinal | N/A | N/A | Não | Qualidade e condição do aquecimento |
| `CentralAir` | Categórica Nominal/Ordinal | N/A | N/A | Não | Ar condicionado central |
| `Electrical` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Sistema elétrico <br>*(Nulos reais: sugere-se imputar com a Moda para simular o valor faltante)* |
| `1stFlrSF` | Numérica Discreta | 334 | 4692 | Não | Pés quadrados do primeiro andar |
| `2ndFlrSF` | Numérica Discreta | 0 | 2065 | Não | Pés quadrados do segundo andar |
| `LowQualFinSF` | Numérica Discreta | 0 | 572 | Não | Pés quadrados com acabamento de baixa qualidade |
| `GrLivArea` | Numérica Discreta | 334 | 5642 | Não | Pés quadrados de área útil acima do nível do solo |
| `BsmtFullBath` | Numérica Discreta | 0 | 3 | Não | Banheiros completos no porão |
| `BsmtHalfBath` | Numérica Discreta | 0 | 2 | Não | Lavabos no porão |
| `FullBath` | Numérica Discreta | 0 | 3 | Não | Banheiros completos acima do solo |
| `HalfBath` | Numérica Discreta | 0 | 2 | Não | Lavabos acima do solo |
| `BedroomAbvGr` | Numérica Discreta | 0 | 8 | Não | Quartos acima do porão |
| `KitchenAbvGr` | Numérica Discreta | 0 | 3 | Não | Cozinhas acima do nível do solo |
| `KitchenQual` | Categórica Nominal/Ordinal | N/A | N/A | Não | Qualidade da cozinha |
| `TotRmsAbvGrd` | Numérica Discreta | 2 | 14 | Não | Total de cômodos acima do solo (sem banheiros) |
| `Functional` | Categórica Nominal/Ordinal | N/A | N/A | Não | Funcionalidade geral da casa |
| `Fireplaces` | Numérica Discreta | 0 | 3 | Não | Número de lareiras |
| `FireplaceQu` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Qualidade da lareira <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `GarageType` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Localização da garagem <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `GarageYrBlt` | Numérica Discreta | 1900.0 | 2010.0 | Sim | Ano em que a garagem foi construída <br>*(Nulos reais: sugere-se imputar com **0** ou com a Mediana para simular o valor faltante)* |
| `GarageFinish` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Acabamento interior da garagem <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `GarageCars` | Numérica Discreta | 0 | 4 | Não | Tamanho da garagem em capacidade de carros |
| `GarageArea` | Numérica Discreta | 0 | 1418 | Não | Tamanho da garagem em pés quadrados |
| `GarageQual` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Qualidade da garagem <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `GarageCond` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Condições da garagem <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `PavedDrive` | Categórica Nominal/Ordinal | N/A | N/A | Não | Estrada de acesso pavimentada |
| `WoodDeckSF` | Numérica Discreta | 0 | 857 | Não | Área de deck de madeira em pés quadrados |
| `OpenPorchSF` | Numérica Discreta | 0 | 547 | Não | Área de varanda aberta em pés quadrados |
| `EnclosedPorch` | Numérica Discreta | 0 | 552 | Não | Área de varanda fechada em pés quadrados |
| `3SsnPorch` | Numérica Discreta | 0 | 508 | Não | Área de varanda três estações em pés quadrados |
| `ScreenPorch` | Numérica Discreta | 0 | 480 | Não | Área de varanda com tela em pés quadrados |
| `PoolArea` | Numérica Discreta | 0 | 738 | Não | Área da piscina em pés quadrados |
| `PoolQC` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Qualidade da piscina <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `Fence` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Qualidade da cerca <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `MiscFeature` | Categórica Nominal/Ordinal | N/A | N/A | Sim | Características diversas não incluídas em outras categorias <br>*(Nulos aqui indicam a ausência do atributo, ex: Sem Garagem. Preencher com 'None')* |
| `MiscVal` | Numérica Discreta | 0 | 15500 | Não | Valor da característica diversa em dólares |
| `MoSold` | Numérica Discreta | 1 | 12 | Não | Mês da venda |
| `YrSold` | Numérica Discreta | 2006 | 2010 | Não | Ano da venda |
| `SaleType` | Categórica Nominal/Ordinal | N/A | N/A | Não | Tipo de venda |
| `SaleCondition` | Categórica Nominal/Ordinal | N/A | N/A | Não | Condição da venda |
| `SalePrice` | Numérica Discreta | 34900 | 745000 | Não | Preço de venda da propriedade (Target) |