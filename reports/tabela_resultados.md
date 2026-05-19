| Modelo            | RMSE Treino   |   RMSE CV (RMSLE) | Superou o Baseline?   |
|:------------------|:--------------|------------------:|:----------------------|
| Baseline          | -             |           0.17543 | Benchmark             |
| Ridge (L2)        | 0.11565       |           0.14232 | Sim                   |
| Lasso (L1)        | 0.11845       |           0.14562 | Sim                   |
| Árvore de Decisão | 0.00000       |           0.21941 | Não                   |
| Random Forest     | 0.05386       |           0.14796 | Sim                   |
| XGBoost           | 0.06487       |           0.12724 | Sim                   |