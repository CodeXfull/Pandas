import pandas as pd 

base = pd.read_csv("./index_select_assign/access_data_1/census.csv")

# print(base.loc[base.native_country.notnull()]) # Os que não são nulos
print(base.loc[base.native_country.isnull()]) # identificar NaN
