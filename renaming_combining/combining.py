"""
Combinando
Ao executar operações em um conjunto de dados, às vezes precisaremos combinar DataFrames e / ou séries diferentes de maneiras não triviais. 

O Pandas possui três métodos principais para fazer isso. Em ordem crescente de complexidade, são concat (), join () e merge (). A maior parte do que merge () pode fazer também pode ser feita de maneira mais simples com join ().

O método de combinação mais simples é concat (). Dada uma lista de elementos, essa função agrupará esses elementos ao longo de um eixo.

Isso é útil quando temos dados em diferentes objetos DataFrame ou Series, mas com os MESMOS CAMPOS (colunas). 
"""
import pandas as pd

canadian_youtube = pd.read_csv("./renaming_combining/CAvideos.csv")
british_youtube = pd.read_csv("./renaming_combining/GBvideos.csv")

x = pd.concat([canadian_youtube, british_youtube])
print(x)

"""join() permite combinar diferentes objetos DataFrame que têm um índice em comum. Por exemplo, para exibir vídeos que estavam em alta no mesmo dia no Canadá e no Reino Unido, poderíamos fazer o seguinte:

Os parâmetros lsuffix e rsuffix são necessários aqui porque os dados têm os mesmos nomes de coluna nos conjuntos de dados britânicos e canadenses. Se isso não fosse verdade (porque, digamos, nós os renomeamos antes), não precisaríamos deles."""

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

y = left.join(right, lsuffix='_CAN', rsuffix='_UK')
print(y)