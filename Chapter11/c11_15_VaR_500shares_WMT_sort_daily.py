
"""
  Name     : c11_15_VaR_500shares_VMT_sort_daily.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
ticker='WMT'            # input 1
n_shares=500            # input 2
confidence_level=0.99   # input 3
begdate=(2012,1,1)      # input 4
enddate=(2016,12,31)    # input 5
#
z=norm.ppf(1-confidence_level) 
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
ret = np.array(x.aclose[1:]/x.aclose[:-1]-1)
ret2=np.sort(ret) 
#
position=n_shares*x.close[0] 
n=np.size(ret2)
m=int(n*(1-confidence_level))
print("m=",m)
#
sum=0.0
for i in np.arange(m):
    sum+=ret2[i]
ret3=sum/m
ES=position*ret3
print("Holding=",position, "Expected Shortfall=", round(ES,4), "tomorrow")






