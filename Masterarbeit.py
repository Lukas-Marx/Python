# Lukas Marx 219 167 48
# Lukas.Marx@fau.de

import pandas as pd  # Bibliothek "Panel Data"
import numpy as np  # Bibliothek "Nummerisches Python"
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.diagnostic import normal_ad
from statsmodels.stats.outliers_influence import variance_inflation_factor

dataset = pd.read_excel("/Users/LukasMarx/PycharmProjects/Python/Variablen_Regression.xlsx")
print(dataset.head())
print(dataset.info())
X = dataset[['Size','SRI','Impact','ESG','Social','SIB','GBF','GBE','GBV','Environment_Score']]
#y = dataset[['Social_Score']]
f = 'Social_Score~Size+SRI+Impact+ESG+Social+SIB+GBF+GBE+GBV+Environment_Score'
reg_model = ols(formula=f, data=dataset).fit()
print(reg_model.summary())

#heteroskedastie

white_test = het_white(reg_model.resid, reg_model.model.exog)
labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
print(dict(zip(labels, white_test)))

#multikollinearität

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                   for i in range(len(X.columns))]
print(vif_data)