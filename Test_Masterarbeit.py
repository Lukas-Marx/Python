#Lukas Marx 219 167 48
#Lukas.Marx@fau.de

import matplotlib.pyplot as plt  # Die Nr.1 der Bibliotheken zur Datenvisualisierung
import numpy as np               # Bibliothek "Nummerisches Python"
import pandas as pd              # Bibliothek "Panel Data"
from sklearn import linear_model
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.diagnostic import het_breuschpagan

dataset = pd.read_excel("Variablen_Regression.xlsx")
print(dataset.head())
print(dataset.info())
cols_ratio=['Size','SRI','Impact','ESG','Social','SIB','GBF','GBE','GBV','Environment_Score','F1','F2','F3',
            'F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17',
            'F18','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29','F30','F31',
            'F32','F33','F34','F35','F36','F37','F38','F39','F40','F41','F42','F43','F44','F45',
            'F46','F47','F48','F49','F50','F51','F52','F53','F54','F55','F56','F57','F58',
            'F59','F60','F61','F62','F63','F64','F65','F66','F67','F68','F69','F70','F71',
            'F72','F73','F74','F75','F76','F77','F78','F79','F80','F81','F82','F83','F84',
            'F85','F86','F87','F88','F89','F90','F91','F92','F93','F94','F95','F96','F97',
            'F98','F99','F100']
cols_target=['Social_Score']
print(cols_ratio)
X = dataset[['Size','SRI','Impact','ESG','Social','SIB','GBF','GBE','GBV','Environment_Score','F1','F2','F3',
            'F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17',
             'F18','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29','F30','F31',
             'F32','F33','F34','F35','F36','F37','F38','F39','F40','F41','F42','F43','F44','F45',
             'F46','F47','F48','F49','F50','F51','F52','F53','F54','F55','F56','F57','F58',
             'F59','F60','F61','F62','F63','F64','F65','F66','F67','F68','F69','F70','F71',
             'F72','F73','F74','F75','F76','F77','F78','F79','F80','F81','F82','F83','F84',
             'F85','F86','F87','F88','F89','F90','F91','F92','F93','F94','F95','F96','F97',
             'F98','F99','F100']]
print(X)
y = dataset[['Social_Score']]
print(y)
regr = linear_model.LinearRegression()
result = regr.fit(X,y)

print ('R-Quadrat ', regr.score(X, y))
print ('Koeffizienten: ', result.coef_)

regr2 = sm.OLS(y, X)

regr2_result = regr2.fit()
print(regr2_result.summary())

f='Social_Score~Size+SRI+Impact+ESG+Social+SIB+GBF+GBE+GBV+Environment_Score+F1+F2+F3+F4+F5+F6+F7+F8+F9+F10+F11+F12' \
  '+F13+F14+F15+F16+F17+F18+F19+F20+F21+F22+F23+F24+F25+F26+F27+F28+F29+F30+F31+F32+F33+F34+F35+F36+F37+F38+F39+F40' \
  '+F41+F42+F43+F44+F45+F46+F47+F48+F49+F50+F51+F52+F53+F54+F55+F56+F57+F58+F59+F60+F61+F62+F63+F64+F65+F66+F67+F68' \
  '+F69+F70+F71+F72+F73+F74+F75+F76+F77+F78+F79+F80+F81+F82+F83+F84+F85+F86+F87+F88+F89+F90+F91+F92+F93+F94+F95+F96' \
  '+F97+F98+F99+F100'

reg_model= ols(formula=f, data=dataset).fit()
print(reg_model.summary())
white_test=het_white(reg_model.resid, reg_model.model.exog)

labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
print(dict(zip(labels, white_test)))