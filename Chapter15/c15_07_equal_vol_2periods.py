"""
  Name     : c15_07_equal_vol_2periods.py
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
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
# input area
ticker='F'            # stock
begdate1=(1982,9,1)   # starting date for period 1 
enddate1=(1987,9,1)   # ending date for period   1 
begdate2=(1987,12,1)  # starting date for period 2 
enddate2=(1992,12,1)  # ending   date for period 2
#
# define a function
def ret_f(ticker,begdate,enddate):
    p =getData(ticker, begdate, enddate,asobject=True, adjusted=True)
    ret = p.aclose[1:]/p.aclose[:-1]-1 
    date_=p.date
    return pd.DataFrame(data=ret,index=date_[1:],columns=['ret'])
#
# call the above function twice 
ret1=ret_f(ticker,begdate1,enddate1) 
ret2=ret_f(ticker,begdate2,enddate2)
#
# output
print('Std period #1	vs. std period #2') 
print(round(sp.std(ret1.ret),6),round(sp.std(ret2.ret),6)) 
print('T value ,	p-value ') 
print(sp.stats.bartlett(ret1.ret,ret2.ret))
