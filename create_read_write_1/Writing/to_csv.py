"""
Converter um DataFrame para CSV
"""
import pandas as pd

dataset = pd.DataFrame({'Frutas': ["Abacaxi", "Mamão"],
                     "Nomes": ["Éverton", "Márcia"]},
                     index=["Linha 1", "Linha 2"])

dataset.to_csv("dataset.csv")