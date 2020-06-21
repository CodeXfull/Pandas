"""
Podemos acessar os dados de um DataFrame de 2 formas
usando a sintaxe:
nome_DataFrame.nome_coluna
nome_DataFrame["nome_coluna"]

Saída:
    Frutas  Valor Fornecedor
0  Abacaxi    5.0     Serasa
1    Mamão    6.0        Mix
"""
import pandas as pd 

estoque = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão"], 
                        "Valor": [5.00, 6.00],
                        "Fornecedor": ["Serasa", "Mix"]})
print(estoque.Frutas)
print(estoque.Valor)

print("-"*20)

# Posso acessar os dados em um DataFrame dessa maneira tbm
print(estoque["Fornecedor"])

