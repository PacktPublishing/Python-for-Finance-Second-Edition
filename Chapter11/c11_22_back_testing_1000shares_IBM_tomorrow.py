"""
  Name     : c11_30_back_testing_1000shares_IBM_tomorrow.py
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
# input area
ticker='IBM'              # input 1
n_shares=1000             # input 2
confidence_level=0.99     # input 3
begdate=(2016,2,7)        # input 4
enddate=(2017,2,7)        # input 5
#
z=norm.ppf(1-confidence_level) 
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
print(x[0])
ret = x.aclose[1:]/x.aclose[:-1]-1
#
position=n_shares*x.close[0] 
mean=np.mean(ret)
z=norm.ppf(1-confidence_level)
std=np.std(ret)
#
VaR=position*(mean+z*std)
print("Holding=",position, "VaR=", round(VaR,4), "tomorrow")
print("VaR/holding=",VaR/position)





