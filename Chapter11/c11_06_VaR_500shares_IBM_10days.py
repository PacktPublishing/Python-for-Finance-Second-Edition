"""
  Name     : c11_06_VaR_500shares_IBM_10day.py
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

ticker='WMT'            # input 1
n_shares=500            # input 2
confidence_level=0.99   # input 3
n_days=10                # input 4
begdate=(2012,1,1)      # input 5
enddate=(2016,12,31)    # input 6
#
z=norm.ppf(confidence_level) 
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
ret = x.aclose[1:]/x.aclose[:-1]-1
#
position=n_shares*x.close[0] 
std=np.std(ret)
stdNdays=std*np.sqrt(n_days)
#
VaR1=position*z*stdNdays
print("Holding=",position, "VaR=", round(VaR1,4), "in ", n_days, "Days")






