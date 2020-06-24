"""
agg()  permite executar várias funções diferentes no DataFrame simultaneamente

reviews.groupby(['country']).price.agg([len, min, max])
"""
import pandas as pd 

base = pd.read_csv("./grouping_sort/groupby/students_performance.csv")

"""
Saída:
                                len  min  max
    parental_level_of_education
    associate's degree           222   26  100
    bachelor's degree            118   29  100
    high school                  196    8   99
    master's degree               59   40   95
    some college                 226   19  100
    some high school             179    0   97
"""
print(base.groupby(['parental_level_of_education']).math_score.agg([len,min,max]))

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")
print(reviews.groupby(['country']).price.agg([len, min, max]))