# -*- coding: utf-8 -*-
"""
  Name     : c7_16_sharpe_ratio_YahooData.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
from matplotlib.finance import quotes_historical_yahoo_ochl as getData

begdate=(2012,1,1)
enddate=(2016,12,31)

def ret_f(ticker,begdate,enddate):
     p = getData(ticker,begdate, enddate,asobject=True,adjusted=True)
     return(p.aclose[1:]/p.aclose[:-1]-1)
         
y=ret_f('IBM',begdate,enddate)
sharpe=sp.mean(y)/sp.std(y)
print(sharpe)