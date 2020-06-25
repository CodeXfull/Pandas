"""
Renomeando
rename() permite alterar nomes de índices e / ou nomes de colunas. 

"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

# Por exemplo, para alterar a coluna de pontos em nosso conjunto de dados, faríamos:
reviews.rename(columns={'points': 'score'})

