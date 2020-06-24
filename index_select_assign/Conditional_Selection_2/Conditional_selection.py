import pandas as pd 

base = pd.read_csv("./index_select_assign/access_data_1/census.csv")


# print(base.marital_status)
print(base.education == ' Bachelors') # True/False para o resultado

#Usando o ==
print(base.loc[base.marital_status == 'Divorced'])
print(base.loc[base.native_country == ' ?'])

#Usando o &
print((base.education == " Bachelors") & (base.age >=45))

# substituindo o loop e usando o |
print(base.loc[(base.age >=45)| (base.relationship == " Husband")])

