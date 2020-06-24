"""
Os map permitem transformar dados em um DataFrame ou Series, um valor de cada vez, para uma coluna inteira. 
No entanto, muitas vezes queremos agrupar nossos dados e, em seguida, fazer algo específico ao grupo em que os dados estão.

value_counts() é apenas um atalho para esta operação groupby()
"""
import pandas as pd 

base = pd.read_csv("./grouping_sort/groupby/students_performance.csv")

# faz a msm coisa q o value.counts()
# size inclui NaN e valores count não:
# 1 Forma
print(base.groupby('parental_level_of_education').parental_level_of_education.count())

# 2 forma
print(base.groupby('parental_level_of_education').parental_level_of_education.size())

print("-"*20)
# students_performace com menor math_score na parental_level_of_education
print(base.groupby('parental_level_of_education').math_score.min())

# conferindo pra averiguar
# print(base.loc[(base.parental_level_of_education == "some college")])

print("-"*20)
# aqui está uma maneira de selecionar o nome do primeiro parental_level_of_education revisado de cada writing_score no conjunto de dados:
print(base.groupby('parental_level_of_education').apply(lambda df: df.writing_score.iloc[0]))



