#Lukas Marx 219 167 48
#Lukas.Marx@fau.de

import matplotlib.pyplot as plt  # Die Nr.1 der Bibliotheken zur Datenvisualisierung
import numpy as np               # Bibliothek "Nummerisches Python"
import pandas as pd              # Bibliothek "Panel Data"
from sklearn import linear_model
import statsmodels.api as sm


dataset = pd.read_excel("Variablen_Regression.xlsx")
print(dataset.head())
print(dataset.info())
cols_ratio=['Size','Social','SIB','SIB_Vol','Impact','Impact_Vol','SII_Vol','GBF','GBE','GBV']
cols_target=['Social_Score']
print(cols_ratio)
X = dataset[['Size','SRI','Impact','ESG','Social','SIB','GBF','GBE','GBV','Environment_Score','F1','F2','F3']]
print(X)
y = dataset[['Social_Score']]
print(y)
regr = linear_model.LinearRegression()
regr.fit(X,y)

print ('R-Quadrat ', regr.score(X, y))
print ('Koeffizienten: ', regr.coef_)

regr2 = sm.OLS(X, y)

regr2_result = regr2.fit()
print(regr2_result.summary())
