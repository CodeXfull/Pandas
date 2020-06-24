import pandas as pd 
reviews = pd.read_csv("./summary_maps/maps/census3.csv")

print(reviews.education +"-"+reviews.workclass)
"""
# unindo apply e concatenação

def remean_points(row):
    row.age = str(row.age)
    return row

# axis = index teríamos que passar uma função para transformar cada coluna
x = reviews.apply(remean_points, axis='columns')
# print(x)
new = (x.education+"-"+x.age)
print(new.value_counts())

"""
