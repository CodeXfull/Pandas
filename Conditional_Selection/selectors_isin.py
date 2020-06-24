"""
Pandas vem com alguns seletores condicionais embutidos

1º .isin -> permite selecionar dados cujo valor "está em" uma lista de valores
Sintaxe:
base.loc[base.nome_coluna.isin(["nome_localizar",...,"nome_localizar"])]

paises = ["Australia","New Zealand"]
top_oceania_wines = reviews.loc[(reviews.country.isin(paises)) & (reviews.points >= 95) ]
"""
import pandas as pd 

base = pd.read_csv("./access_data/census.csv")

print(base.loc[base.native_country.isin([" Mexico", " Puerto-Rico"])])