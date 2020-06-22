"""
Nesse paradigma, é o valor do índice de dados, não a sua posição, o que importa.

Saída estoque:
        Frutas  Valor Fornecedor
    0    Abacaxi    5.0     Serasa
    1      Mamão    6.0        Mix
    2      Manga    4.0      Feira
    3    Abacate    3.0    Mercado
    4  Bergamota    0.6        Lux

.loc[índice_coluna, "nome_da_coluna"]

OBS: o iloc usa o índice pra pegar a posição.
loc pega índice e nome das colunas.
"""
import pandas as pd 

estoque = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão","Manga","Abacate","Bergamota"], 
                        "Valor": [5.00, 6.00, 4.00,3.00, 0.60],
                        "Fornecedor": ["Serasa", "Mix","Feira","Mercado","Lux"]})

print(estoque.loc[0,"Frutas"])
print(estoque.loc[2,"Fornecedor"])

print(estoque.loc[:,["Valor", "Frutas"]])

print("-"*15) # muda nisso, mas em outra semântica funcionam da mesma maneira
print(estoque.loc[0:2]) # não incluído 0 2
print(estoque.iloc[0:2]) # incluído o 2