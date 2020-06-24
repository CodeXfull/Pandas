import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")

x = reviews.groupby(['variety']).price.agg([min,max])
sorted_varieties = x.sort_values(by=['min','max'],ascending=False)
print(sorted_varieties)

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
print(reviewer_mean_ratings)