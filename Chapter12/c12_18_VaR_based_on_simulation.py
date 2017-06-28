
"""
  Name     : c12_18_VaR_based_on_simulation.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import scipy as sp
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
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
ret = x.aclose[1:]/x.aclose[:-1]-1
#
position=n_shares*x.close[0] 
mean=np.mean(ret)
std=np.std(ret)
#
n_simulation=5000
sp.random.seed(12345) 
ret2=sp.random.normal(mean,std,n_simulation) 
ret3=np.sort(ret2) 
m=int(n_simulation*(1-confidence_level))
VaR=position*(ret3[m])
print("Holding=",position, "VaR=", round(VaR,4), "tomorrow")
