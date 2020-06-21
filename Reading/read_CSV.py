"""
Os dados podem ser armazenados em várias formas e formatos diferentes. De longe, o mais básico deles é o humilde arquivo CSV. 

CSV: Arquivo separado por vírgula, porém, pode ser por ; -
A função pd.read_csv () é bem-dotada, com mais de 30 parâmetros opcionais

Saída censo.shape:
(32561,14)

Logo, temos 32561 registros(linhas) e 15 colunas
"""
import pandas as pd 

censo = pd.read_csv(".\\Reading\\census.csv")
print(censo.shape)