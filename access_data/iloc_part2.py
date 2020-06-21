"""
Seleção de colunas com iloc 

Saída estoque:
        Frutas  Valor Fornecedor
    0    Abacaxi    5.0     Serasa
    1      Mamão    6.0        Mix
    2      Manga    4.0      Feira
    3    Abacate    3.0    Mercado
    4  Bergamota    0.6        Lux

Saída 1º print:
    0     Serasa
    1        Mix
    2      Feira
    3    Mercado
    4        Lux
    Name: Fornecedor, dtype: object

Saída 2º print:
    0    5.0
    1    6.0
    2    4.0
    Name: Valor, dtype: float64

Saída 3º print:
    1      Mamão
    2      Manga
    3    Abacate
    Name: Frutas, dtype: object

Saída 4º print:
    2        Manga
    3      Abacate
    4    Bergamota
    Name: Frutas, dtype: object

Saída 5º print:
        Frutas  Valor Fornecedor
    3    Abacate    3.0    Mercado
    4  Bergamota    0.6        Lux
"""
import pandas as pd 

estoque = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão","Manga","Abacate","Bergamota"], 
                        "Valor": [5.00, 6.00, 4.00,3.00, 0.60],
                        "Fornecedor": ["Serasa", "Mix","Feira","Mercado","Lux"]})

print(estoque.iloc[:,2]) # imprimi tudo da coluna 2(Fornecedor)
print(estoque.iloc[:3,1]) # imprimi tudo coluna 1(Valor) até o índice 3(não incluído)
print(estoque.iloc[1:4,0]) # imprimi tudo coluna 0(Frutas) do índice 1 até o 4
print(estoque.iloc[[2,3,4],0]) # imprimi o indice 2,3 e 4 da coluna 0
print(estoque.iloc[-2:]) # todas as listas imprimi os ultimos 2 elementos do final