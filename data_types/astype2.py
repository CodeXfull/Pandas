"""
float64 significa que está usando um número de ponto flutuante de 64 bits; int64 significa um número inteiro de tamanho semelhante.

Uma peculiaridade é que as colunas constituídas inteiramente por cadeias não têm seu próprio tipo; eles recebem o tipo de objeto.

É possível converter uma coluna de um tipo em outro, sempre que essa conversão fizer sentido usando a função astype (). Por exemplo, podemos transformar a coluna points do tipo de dados int64 existente em um tipo de dados float64:
"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

print(reviews.points.astype('float64'))
# point_strings = reviews.points.astype('str')
# print(reviews.index.dtype)