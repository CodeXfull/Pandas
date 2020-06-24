"""
Podemos acessar um dado específico de uma coluna em um DataFrame

Saída:
    Frutas  Valor Fornecedor
0  Abacaxi    5.0     Serasa
1    Mamão    6.0        Mix
"""
import pandas as pd 

estoque = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão"], 
                        "Valor": [5.00, 6.00],
                        "Fornecedor": ["Serasa", "Mix"]})

print(estoque["Frutas"][1]) # Saída: Mamão
print(estoque["Fornecedor"][0])
