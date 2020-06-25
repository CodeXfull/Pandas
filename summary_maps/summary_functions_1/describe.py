"""
O Pandas fornece muitas "funções de resumo" simples  que reestruturam os dados de alguma maneira útil.
"""
import pandas as pd 

reviews = pd.read_csv("./summary_maps/summary_functions_1/census.csv")
print(reviews.describe())
# print(reviews.education.describe()) # faz sentido só com dados do tipo númerico
print(reviews.hour_per_week.describe())

# média
print(reviews.hour_per_week.mean())

# mediana
print(reviews.hour_per_week.median())

# ver lista(array) de valores possíveis
print(reviews.education.unique())
print(reviews.hour_per_week.unique())

# ver uma lista de valores possíveis e com que frequência eles ocorrem no conjunto de dados
print(reviews.education.value_counts())

# retorna o indice do valor máximo
print("Idxmax encontrado:")
print(reviews.iloc[reviews["final_weight"].idxmax()])

print("Testando:")
# usando uma proporção pegar indice do valor máximo
bargain_idx = (reviews.final_weight/ reviews.age).idxmax()
print(bargain_idx)
print('-'*20)
print(reviews.loc[bargain_idx])
bargain_wine = reviews.loc[bargain_idx, 'occupation']
print(bargain_wine)
