Olá! Estou iniciando um projeto de Ciência de Dados em Python para prever preços de casas (coluna target: 'SalePrice') em uma competição acadêmica da faculdade. Nosso ambiente de desenvolvimento utiliza o gerenciador de pacotes `uv` e rodamos nossos códigos em notebooks `.ipynb`.

O projeto já possui uma estrutura de diretórios definida:
- `./data/treino.csv` e `./data/teste_publico.csv` (os dados)
- `./data/descricao_dados.txt` (a documentação bruta das colunas)
- `./data/metricas_baseline.txt` (o benchmark a ser batido)
- `pipeline.py`, `main.py` e `notebooks/notebook.ipynb`

Preciso que você atue como um Engenheiro de Dados e Cientista de Dados Sênior para realizar a primeira etapa do projeto: a Análise Exploratória de Dados (EDA) e Documentação Simplificada. 

Por favor, execute as seguintes tarefas de forma sequencial:

---

### Tarefa 1: Criação da Documentação Simplificada (Markdown)
Antes de gerar o código, leia o arquivo `./data/descricao_dados.txt` e o arquivo `./data/treino.csv`. Com base neles, crie um arquivo chamado `reports/variaveis_simplificadas.md` contendo uma tabela ou lista estruturada explicando cada variável do dataset. 

Para cada variável, inclua rigorosamente os seguintes campos:
1. **Nome da variável**
2. **Tipo da variável** (Ex: Numérica Contínua, Numérica Discreta, Categórica Nominal, Categórica Ordinal)
3. **Menor valor** encontrado no dataset de treino
4. **Maior valor** encontrado no dataset de treino
5. Possui valores nulos?
6. **Breve explicação** do significado dela (traduzido/adaptado de forma simples em português)

---

### Tarefa 2: Desenvolvimento do Notebook de Análise Exploratória e Preparação
Após gerar o markdown, abra/crie o arquivo `notebooks/notebook.ipynb`. Desenvolva um pipeline de análise passo a passo, documentando cada bloco com células Markdown explicativas. O notebook deve conter as seguintes seções e análises:

1. **Análise de Valores Nulos e Dependências:**
   - Identifique quais colunas possuem valores nulos.
   - Explique, com base na documentação, quais nulos são de fato dados faltantes e quais apenas indicam a ausência de um atributo (ex: `NA` em Piscina significando "Não possui piscina").
   - Analise se a nulidade de uma variável depende de outra (ex: se os nulos de `GarageYrBlt` ocorrem exatamente onde `GarageType` é nulo).

2. **Estatísticas Descritivas Limites:**
   - Exiba os valores máximos e mínimos de cada variável (pode usar `.describe()` de forma organizada).

3. **Matriz de Correlação Global:**
   - Calcule e plote uma matriz de correlação (heatmap usando `seaborn`) entre todas as variáveis numéricas do dataset, incluindo o target `SalePrice`.
   - Guarde essa imagem da matriz na pasta `reports/`.

4. **Identificação de Colinearidade e Redução de Dimensionalidade:**
   - Identifique pares ou grupos de variáveis que possuem uma correlação linear muito forte entre si (ex: `GarageCars` e `GarageArea`, ou `GrLivArea` e `TotRmsAbvGrd`).
   - Sugira e demonstre como podemos juntá-las ou dropar uma delas para diminuir o número de variáveis e evitar multicolinearidade no modelo.

5. **Técnicas de Padronização e Ajuste:**
   - Avalie a assimetria (*skewness*) da variável alvo `SalePrice` e aplique a transformação logarítmica $\log(1+x)$ com `np.log1p` para deixá-la em uma distribuição normal.
   - Demonstre exemplos de como aplicar padronização/escala (`StandardScaler` ou `MinMaxScaler`) nas variáveis numéricas e codificação (One-Hot / Ordinal) nas categóricas para deixar os dados perfeitamente redondos para os futuros modelos de machine learning.

6. **Verificação de outliers**
   - Verifique a presença de outliers na variável alvo `SalePrice` e em outras variáveis que possam indicar problemas no dataset. Mostre como identificá-los e quais estratégias podem ser usadas para tratá-los. Por exemplo, SalePrice teve um valor muito alto e teve relação muito grande com uma outra variável do dataset que também ficou muito alta ou muito baixa.
   - Faça boxplots e scatterplots para que fique fácil verificar como está distribuído o 'SalePrice' e quais outliers podem ser tratados. Guarde as imagens na pasta 'reports/'.

---

### Diretrizes de Execução:
- Se precisar de alguma biblioteca de visualização (como `matplotlib` ou `seaborn`) que não esteja instalada, utilize internamente o comando `uv add <pacote>` para gerenciar o ambiente.
- Garanta que todo o código escrito no notebook seja limpo, modular, amplamente comentado e execute sem erros de ponta a ponta.
- Comece gerando o arquivo markdown explicativo conforme solicitado na Tarefa 1.