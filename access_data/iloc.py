"""
Usamo iloc quando queremos selecionar dados de linhas e colunas pelo seu valor numérico de índice. Senão usamos loc

Seleção de linhas com iloc 

Saída estoque:
    Frutas  Valor Fornecedor
0  Abacaxi    5.0     Serasa
1    Mamão    6.0        Mix


"""
import pandas as pd 

estoque = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão"], 
                        "Valor": [5.00, 6.00],
                        "Fornecedor": ["Serasa", "Mix"]})

data = estoque.iloc[0] # Abacaxi    5.0     Serasa
print(type(data))
print(estoque.iloc[1]) # Mamão    6.0        Mix

"""
data.to_csv("data.csv") # passa o nome das colunas como índice

Saída:          
                0
Frutas        Abacaxi
Valor            5.0
Fornecedor     Serasa
"""