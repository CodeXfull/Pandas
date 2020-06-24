'''
Existem 2 objetos principais no Pandas os DataFrames e as Séries

DataFrame é uma tabela. Ela contém a declaração da coluna e na lista cada indíce corresponde a uma linha naquela mesma coluna.

Saída:
    Yes | No
0   50  | 131
1   21  | 2

A entrada "0, Yes" tem um valor de 50

pd.DataFrame () para gerar DataFrame
Sintaxe: chaves são os nomes das colunas e os valores são uma lista de entradas.
'''
import pandas as pd 

print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))
print("-"*20)
print(pd.DataFrame({'Frutas': ["Abacaxi", "Mamão"], "Nomes": ["Éverton", "Márcia"]}))