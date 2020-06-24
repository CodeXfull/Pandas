import pandas as pd 

base = pd.read_csv("./index_select_assign/access_data_1/census.csv")


def remean_points(row):
    if row.age >=30:
        return "Legal"
    return "novo"

# axis = index teríamos que passar uma função para transformar cada coluna
x = base.apply(remean_points, axis='columns')
print(x)

"""
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
"""