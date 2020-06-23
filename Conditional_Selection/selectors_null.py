import pandas as pd 

base = pd.read_csv("./access_data/census.csv")

# print(base.loc[base.native_country.notnull()]) # Os que não são nulos
print(base.loc[base.native_country.isnull()]) # identificar NaN
