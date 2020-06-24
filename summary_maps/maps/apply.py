"""
apply () é o método equivalente se quisermos transformar um DataFrame inteiro chamando um método personalizado em cada linha.

Aplico no DataFrame a transformação, mas não o original

Observe que map () e apply () retornam novos Series e DataFrames transformados, respectivamente. Eles não modificam os dados originais em que são chamados. Se olharmos para a primeira linha de resenhas, podemos ver que ela ainda possui seu valor original de pontos.
"""
import pandas as pd 
reviews = pd.read_csv("./summary_maps/maps/census3.csv")

media = reviews.hour_per_week.mean()

def remean_points(row):
    row.hour_per_week = row.hour_per_week - media
    return row

# axis = index teríamos que passar uma função para transformar cada coluna
print(reviews.apply(remean_points, axis='columns'))

print(reviews.head())