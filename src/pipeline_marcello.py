# %%
import pandas as pd
from sklearn import tree
from sklearn import pipeline,metrics
from feature_engine import encoding, imputation, selection

# Importando dados
data = pd.read_csv('../data/treino.csv')
data_test = pd.read_csv('../data/teste_publico.csv')

# Features
X = data.columns[1:-1].tolist()
y = 'SalePrice'

# Features categóricas
cat = data[X].select_dtypes(include='object').columns.to_list()

# Features numéricas
num = [col for col in X if col not in cat]

# =========================
# CRIANDO DATAFRAME AUXILIAR
# =========================
X_model = pd.get_dummies(data[X], drop_first=True)
X_model = X_model.fillna(0)
y_model = data[y].copy()

# Modelo auxiliar
model_best_features = tree.DecisionTreeRegressor(
    random_state=42,
    max_depth=5,
    min_samples_leaf=20
)

model_best_features.fit(X_model, y_model)

# Importância
importance = pd.Series(
    model_best_features.feature_importances_,
    index=X_model.columns
).sort_values(ascending=False)

# Features para remover
remove = importance[importance <= 0].index.tolist()

# =========================
# PIPELINE
# =========================

# Missing numérico e categórico
# Imputação numérica
imputation_num = imputation.ArbitraryNumberImputer(
    arbitrary_number=0,
    variables=num
)

# Imputação categórica
imputation_cat = imputation.CategoricalImputer(
    fill_value='Missing',
    variables=cat
)

# One Hot
one = encoding.OneHotEncoder(
    variables=cat
)

# Remoção de features
drop = selection.DropFeatures(
    features_to_drop=remove
)

# Modelo final
model = tree.DecisionTreeRegressor(
    random_state=42,
    min_samples_leaf=20,
    max_depth=5
)

model_pipeline = pipeline.Pipeline(steps=[
    ("Imputação Num", imputation_num),
    ("Imputação Cat", imputation_cat),
    ("OneHot", one),
    ("DropFeatures", drop),
    ("Modelo", model)
])

# Treinando
model_pipeline.fit(data[X], data[y])
# %%
# Prevendo com dados treino
y_predict_train = model_pipeline.predict(data[X])
y_predict_train
# prevendo com dados teste
# %%
y_predict_test = model_pipeline.predict(data_test[X])
y_predict_test
# %%
