"""
Os índices múltiplos têm vários métodos para lidar com sua estrutura hierárquica, ausentes nos índices de nível único. Eles também exigem dois níveis de rótulos para recuperar um valor. Instruções sobre como usá-los na seção MultiIndex / Advanced Selection da documentação do pandas.

No entanto, em geral, o método de vários índices que você usará com mais frequência é o de conversão para um índice normal, o método reset_index ():
"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

print(countries_reviewed.reset_index())