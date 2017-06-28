
"""
  Name     : c12_25_long_term_forecast.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import numpy as np
import pandas as pd
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
#
# input area
ticker='IBM'           # input value 1 
begdate=(1926,1,1)     # input value 2 
enddate=(2013,12,31)   # input value 3 
n_forecast=25          # input value 4
#
def geomean_ret(returns): 
    product = 1
    for ret in returns: 
        product *= (1+ret)
    return product ** (1.0/len(returns))-1
#
x=getData(ticker,begdate,enddate,asobject=True, adjusted=True)
logret = np.log(x.aclose[1:]/x.aclose[:-1]) 
date=[]
d0=x.date
for i in range(0,np.size(logret)):
    date.append(d0[i].strftime("%Y"))
#
y=pd.DataFrame(logret,date,columns=['logret'],dtype=float)
ret_annual=np.exp(y.groupby(y.index).sum())-1 
ret_annual.columns=['ret_annual']
n_history=len(ret_annual) 
a_mean=np.mean(np.array(ret_annual))
g_mean=geomean_ret(np.array(ret_annual))
w=n_forecast/n_history
future_ret=w*g_mean+(1-w)*a_mean
print('Arithmetric mean=',round(a_mean,3), 'Geomean=',round(g_mean,3),'forecast=',future_ret)


