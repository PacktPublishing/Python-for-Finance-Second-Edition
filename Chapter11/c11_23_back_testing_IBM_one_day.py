"""
  Name     : c11_30_back_testing_IBM_one_day.py
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
#begdate=(2016,2,7)        # input 4
begdate=(1962,2,7)        # input 4
enddate=(2017,2,7)        # input 5
VaR=-3186.5054            # from the previous program
position=122598.996       # from the previous program
#('Holding=', 122598.996, 'VaR=', -3186.5054, 'tomorrow')
#('VaR/holding=', -0.025991284652254254)
#
z=norm.ppf(1-confidence_level) 
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
print("first day=",x[0])
ret = x.aclose[1:]/x.aclose[:-1]-1
#
cutOff=VaR/position 
n=len(ret)
ret2=ret[ret<=cutOff]
n2=len(ret2)
print("n2=",n2)
ratio=n2*1./(n*1.)
print("Ratio=", ratio)






