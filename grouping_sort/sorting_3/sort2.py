"""
Saiba que você pode classificar mais de uma coluna por vez:

"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by=['country', 'len']))