"""
  Name     : c15_04_sp500_4moments.py
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
ticker='^GSPC' 
begdate=(1926,1,1)
enddate=(2013,12,31)
p = getData(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = p.aclose[1:]/p.aclose[:-1]-1
print( 'S&P500	n	=',len(ret))
print( 'S&P500	mean	=',round(np.mean(ret),8)) 
print( 'S&P500	std	=',round(np.std(ret),8)) 
print( 'S&P500	skewness=',round(stats.skew(ret),8))
print( 'S&P500	kurtosis=',round(stats.kurtosis(ret),8))
