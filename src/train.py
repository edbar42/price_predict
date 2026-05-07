# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
import seaborn as sns
pd.set_option('display.max_rows', 500)
pd.set_option("display.max_columns", 100)
# %%
# Importando dados 
data = pd.read_csv('../data/treino.csv')
data.head()
# %%
# Separando minha variaveis da target
X = data.columns[1:-1].tolist()
X
# %%
y = 'SalePrice'
y
# %%
# EXPLORE
df_analise = data[X].copy()
df_analise
# %%
df_analise.shape
qnt_amostras = df_analise.shape[0]
qnt_features = df_analise.shape[1]
print(f'Quantidade de linhas: {qnt_amostras}')
print(f'Quantidade de features: {qnt_features}')
# %%
df_analise.dtypes
# %%
# Features categoricas
cat = df_analise.columns[df_analise.dtypes == 'object'].to_list()
cat
# %%
# Features numericas
num = df_analise.columns[df_analise.dtypes != 'object'].to_list()
num
# %%
# Colunas com dados nulos
null_columns = df_analise.columns[df_analise.isna().mean()>0].to_list()
null_columns
# %%
df_analise['SalePrice'] = data[y]
df_analise
# %%
df_analise[num].describe()
# %%
df_analise[cat].describe()
# %%
# Distribuição da variavel target
plt.hist(df_analise[y])
plt.show()
# %%
# Descobrindo minhas best features
X_model = pd.get_dummies(
    df_analise[X],
    drop_first=True
)
# %%
# Preenchendo NaN
X_model = X_model.fillna(0)
# %%
# Target
y_model = data['SalePrice']
# %%
model_best_features = tree.DecisionTreeRegressor(random_state=42,
                                                 max_depth=5,
                                                 min_samples_leaf=20)

model_best_features
# %%
# Treinando minha arvore 
model_best_features.fit(X_model,y_model)
# %%
importance = pd.Series(
    model_best_features.feature_importances_,
    index=X_model.columns
).sort_values(ascending=False)
importance
# %%
best_features = importance[importance > 0].index.tolist()
best_features
# %%
importance.head(15).sort_values().plot(
    kind='barh',
    figsize=(10,6)
)

plt.title('Top Features Mais Importantes')
plt.xlabel('Importância')
plt.show()
# %%
# Verificando outliers na vaeriavel target
plt.figure(figsize=(10, 4))

sns.boxplot(x=data['SalePrice'])

plt.title('Boxplot SalePrice')
plt.show()
# %%

# Pegando apenas features numéricas originais
best_num_features = [
    col for col in best_features
    if col in num
]

# Top 10
best_num_features = best_num_features[:10]

for col in best_num_features:

    plt.figure(figsize=(6,4))

    sns.scatterplot(
        x=data[col],
        y=data['SalePrice']
    )

    plt.title(f'{col} vs SalePrice')

    plt.xlabel(col)
    plt.ylabel('SalePrice')

    plt.show()
# %%
