#Lukas Marx, 11.09.2020 Fürth, Friedrich-Alexander-Universität Erlangen-Nuernberg
#Lukas.Marx@Fau.de
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib as matplot
data1 = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")
data1

data2 = yf.download("AMZN AAPL GOOG", start="2017-01-01",
                    end="2017-04-30", group_by='tickers')
data2

print(data1)
print(data2)
data = data1 + data2

print (data)

Amazon_stock = yf.download("AMZN", start="2020-09-01", end="2020-09-15")
print(Amazon_stock)
