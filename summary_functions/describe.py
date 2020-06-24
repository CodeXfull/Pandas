"""
O Pandas fornece muitas "funções de resumo" simples  que reestruturam os dados de alguma maneira útil.


"""
import pandas as pd 

reviews = pd.read_csv("./summary_functions/census.csv")
print(reviews.describe())
# print(reviews.education.describe()) # faz sentido só com dados do tipo númerico
print(reviews.hour_per_week.describe())

# média
print(reviews.hour_per_week.mean())

# ver lista(array) de valores possíveis
print(reviews.education.unique())
print(reviews.hour_per_week.unique())

# ver uma lista de valores possíveis e com que frequência eles ocorrem no conjunto de dados
print(reviews.education.value_counts())