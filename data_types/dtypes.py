"""
Dtypes
O tipo de dados para uma coluna em um DataFrame ou em uma Série é conhecido como dtype.

Você pode usar a propriedade dtype para obter o tipo de uma coluna específica.
"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

print(reviews.price.dtype)
print(reviews.province.dtype)
print(reviews.country.dtype)

print('-'*20)
# ver tds os tipos das colunas completos
print(reviews.dtypes)