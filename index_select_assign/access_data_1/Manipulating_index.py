"""
Escolhendo uma coluna específica para servir como índice

Isso é útil se você puder criar um índice para o conjunto de dados que seja melhor que o atual.

Saída estoque:
        Frutas  Valor Fornecedor
    0    Abacaxi    5.0     Serasa
    1      Mamão    6.0        Mix
    2      Manga    4.0      Feira
    3    Abacate    3.0    Mercado
    4  Bergamota    0.6        Lux

"""

import pandas as pd 

estoque = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão","Manga","Abacate","Bergamota"], 
                        "Valor": [5.00, 6.00, 4.00,3.00, 0.60],
                        "Fornecedor": ["Serasa", "Mix","Feira","Mercado","Lux"]})

x = estoque.set_index("Fornecedor") # manipulando o index
print(estoque) # sem manipução
print(x)