"""
Os rótulos das linhas são inseridos de forma crescente(0,1,2,3...) 

Pra mudar isso usamos o index
"""
import pandas as pd

print(pd.DataFrame({'Frutas': ["Abacaxi", "Mamão"],
                     "Nomes": ["Éverton", "Márcia"]},
                     index=["Linha 1", "Linha 2"]))
