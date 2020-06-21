"""
index_col eu escolho qual coluna vai servir como índice
"""
import pandas as pd 

censo = pd.read_csv(".\\Reading\\census.csv",index_col=3)
print(censo.head())
print(censo.shape)