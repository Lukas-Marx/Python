#Lukas Marx 219 167 48
#Lukas.Marx@fau.de

import matplotlib.pyplot as plt  # Die Nr.1 der Bibliotheken zur Datenvisualisierung
import numpy as np               # Bibliothek "Nummerisches Python"
import pandas as pd              # Bibliothek "Panel Data"

dataset = pd.read_excel("Variablen_Regression.xlsx")
print(dataset.head())
print(dataset.info())
cols_ratio=['Size','Social','SIB','SIB_Vol','Impact','Impact_Vol','SII_Vol','GBF','GBE','GBV']