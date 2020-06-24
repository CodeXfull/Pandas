"""
São usados para criar novas representações a partir dos dados existentes ou transformar dados do formato em que estão agora para o formato em que queremos que seja mais tarde

Esses operadores (>, <, == etc.) são mais rápidos que map () ou apply ()

No entanto, map () ou apply () podem fazer coisas mais avançadas, como aplicar lógica condicional com adição e subtração...
"""
import pandas as pd 
reviews = pd.read_csv("./summary_maps/maps/census3.csv")


media = reviews.hour_per_week.mean()
# não passa para o DataFrame, só é executado
# p recebe como dado as hour_per_week
print(reviews.hour_per_week.map(lambda p: p - media))
# recebe como uma serie se eu colocar
base = reviews.hour_per_week.map(lambda p: p - media)

# outra maneira de fazer a mesma coisa anterior
x =reviews.hour_per_week - media
