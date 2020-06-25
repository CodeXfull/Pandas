"""
Missing Data ou Dados ausentes

Os valores ausentes das entradas recebem o valor NaN, abreviação de "Not a Number". Por razões técnicas, esses valores de NaN são sempre do tipo float64.

O Pandas fornece alguns métodos específicos para a falta de dados. Para selecionar entradas NaN, você pode usar pd.isnull () (ou seu companheiro pd.notnull ())
"""
import pandas as pd 

reviews = pd.read_csv("./grouping_sort/groupby/wine.csv")
print(reviews[pd.isnull(reviews.country)])

"""
O Pandas fornece um método realmente útil para esse problema: fillna ().
fillna () fornece algumas estratégias diferentes para mitigar esses dados. Por exemplo, podemos simplesmente substituir cada NaN por um "Desconhecido":
"""
print(reviews.country.fillna("Desconhecido"))

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
"""
Podemos preencher cada valor ausente com o primeiro valor não nulo que aparece algum tempo após o registro fornecido no banco de dados. Isso é conhecido como estratégia de preenchimento.
"""
v = reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
print(v)

"""
O método replace () vale a pena mencionar  porque é útil para substituir dados ausentes, que recebem algum tipo de valor no conjunto de dados: coisas como "Desconhecido", "Não Divulgado", "Inválido" etc.
"Unknown", "Undisclosed", "Invalid"
"""

"""
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
print(n_missing_prices)

# Solução alternativa atraente: se somarmos uma série booleana, True será tratado como 1 e False como 0
# n_missing_prices = reviews.price.isnull().sum()

# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()
print(n_missing_prices)"""
