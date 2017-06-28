"""
  Name     : c8_20_Durbin_Watson_test.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import statsmodels.stats.stattools as tools 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
ticker='IBM' 
begdate=(2012,1,2) 
enddate=(2016,12,31) 
data= getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
p=data.aclose 
ret=p[:1]/p[1:]-1

print(tools.durbin_watson(ret))
