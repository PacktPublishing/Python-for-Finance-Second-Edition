
"""
  Name     : c11_11_normality_test_for_SP500.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np 
from scipy import stats 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
#
ticker='^GSPC'    # ^GSPC is for S&P500
begdate=(2012,1,1) 
enddate=(2016,12,31) 
#
p =getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[1:] 
print 'ticker=',ticker,'W-test, and P-value' 
print(stats.shapiro(ret))
print( stats.anderson(ret) )
