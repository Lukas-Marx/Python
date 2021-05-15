#Lukas Marx 219 167 48
#Lukas.Marx@fau.de

import pandas as pd              # Bibliothek "Panel Data"
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import het_white

dataset = pd.read_excel("Variablen_Regression.xlsx")
print(dataset.head())
print(dataset.info())

f='Social_Score~Size+SRI+Impact+ESG+Social+SIB+GBF+GBE+GBV+Environment_Score'
reg_model= ols(formula=f, data=dataset).fit()
print(reg_model.summary())
white_test=het_white(reg_model.resid, reg_model.model.exog)

labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
print(dict(zip(labels, white_test)))