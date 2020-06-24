import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)