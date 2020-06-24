"""
Multi-índices
 Trabalhamos com objetos DataFrame ou Series com um índice de rótulo único. groupby () é um pouco diferente no fato de que, dependendo da operação que executamos, algumas vezes resulta no que é chamado de índice múltiplo.

Um índice múltiplo difere de um índice regular, pois possui vários níveis.
"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)
mi = countries_reviewed.index
print(type(mi)) # Saída: <class 'pandas.core.indexes.multi.MultiIndex'>


# transformando data frame em Series
x = countries_reviewed.reset_index()
x_new = pd.Series(x['country'].values, index=x['len'])
print(x_new)