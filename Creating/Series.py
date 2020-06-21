"""
Serie é uma única coluna de um DataFrame, isto é, uma lista.
Como o DataFrame acrescenta rótulos em ordem crescente.
Não tem um nome de coluna apenas um nome geral

Saída:
0    Valor 1
1    Valor 2
2    Valor 3
3    Valor 4
4    Valor 5

Saída:
Fruta 1    Abacaxi
Fruta 2      Mamão

IMPORTANTE: DataFrames são um monte de séries "coladas"
"""
import pandas as pd 

print(pd.Series(["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5"]))
print("-"*20)
print(pd.Series(["Abacaxi", "Mamão"], 
                index=["Fruta 1", "Fruta 2"],
                name = "Frutas" ))