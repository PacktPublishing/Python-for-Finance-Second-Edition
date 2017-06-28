"""
  Name     : c9_77_Modigliani_m2_performance_measure.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

begdate=(2012,1,1)
enddate=(2016,12,31)
ticker='IBM'

def ret_f(ticker):  #	function 1
    x = getData(ticker,begdate,enddate,asobject=True,adjusted=True)
    ret=x.aclose[1:]/x.aclose[:-1]-1 
    ddate=x['date'][1:]
    y=pd.DataFrame(ret,columns=[ticker],index=ddate) 
    return y.groupby(y.index).sum()

a=ret_f(ticker)
b=ret_f("^GSPC")
c=pd.merge(a,b,left_index=True, right_index=True)
print(c.head())
mean=sp.mean(c)
print(mean)
cov=sp.dot(c.T,c)
print(cov)



