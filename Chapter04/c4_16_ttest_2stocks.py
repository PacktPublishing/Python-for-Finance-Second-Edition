# -*- coding: utf-8 -*-
"""
  Name     : c4_16_ttest_2stocks.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import scipy.stats as stats
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
begdate=(2013,1,1)
enddate=(2016,12,9)

def ret_f(ticker,begdate,enddate):
     p = getData(ticker,begdate, enddate,asobject=True,adjusted=True)
     ret=p.aclose[1:]
     ret=p.aclose[1:]/p.aclose[:-1]-1
     return(ret)
     
a=ret_f('IBM',begdate,enddate)
b=ret_f('MSFT',begdate,enddate)
print(stats.ttest_ind(a,b))

