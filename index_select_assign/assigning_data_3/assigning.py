"""
Atribuindo dados em um DataFrame

"""
import pandas as pd 

base = pd.read_csv("./index_select_assign/assigning_data_3/census2.csv")

print(base.loc[base.occupation == " ?"])
# OBS: não alterei o arquivo original, modifiquei a base
base.loc[base.occupation == " ?", "occupation"] = "Não informado"
print(base.loc[base.occupation == " ?"])