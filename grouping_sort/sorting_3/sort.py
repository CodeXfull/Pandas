"""
Olhand para countries_reviewed na pasta multi_index_2 em multi.py, podemos ver que o agrupamento retorna dados em ordem de índice, ou seja, como imprimiu. 

Para obter os dados na ordem desejada,por exemplo pelo len, podemos classificá-los nós mesmos. O método sort_values() é útil para isso."""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by='len'))

"""
sort_values ​​() uma classificação crescente, onde os valores mais baixos são os primeiros. 
Para fazermos uma classificação decrescente, onde os números mais altos vão primeiro podemos fazer de 2 formas diferentes 
"""
# 1 Forma escolhendo uma coluna como índice 
print(countries_reviewed.sort_values(by='len', ascending=False)) 

# 2 Forma com índice padrão
print(countries_reviewed.sort_index())