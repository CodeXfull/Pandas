"""
Contar o número de ocorrências de algo
"""

import pandas as pd 

reviews = pd.read_csv("./summary_maps/summary_functions_1/census.csv")

n_educ = reviews.education.map(lambda desc: " Masters" in desc).sum()
n_occup = reviews.occupation.map(lambda desc: " Prof-specialty" in desc).sum()
descriptor_counts = pd.Series([n_educ, n_occup], index=['Educação', 'Ocupação'])
print(descriptor_counts)