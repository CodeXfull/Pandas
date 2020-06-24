"""
Para um controle ainda mais refinado, você também pode agrupar por mais de uma coluna. Por exemplo, eis como escolheríamos o melhor student por level_education e math_score selecionando pelo writing_score

eis como escolheríamos o melhor vinho por país e província:
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")
base = pd.read_csv("./grouping_sort/groupby/students_performance.csv")

print(base.groupby(['parental_level_of_education', 'math_score']).apply(lambda df: df.loc[df.writing_score.idxmax()]))

print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))