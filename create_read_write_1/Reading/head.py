"""
Podemos examinar o conteúdo do DataFrame resultante usando o comando head (), que captura as cinco primeiras linhas:
"""
import pandas as pd 

censo = pd.read_csv(".\\Reading\\census.csv")

print(censo.head())