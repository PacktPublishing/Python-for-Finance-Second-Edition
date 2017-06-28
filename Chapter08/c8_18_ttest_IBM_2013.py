"""
  Name     : c8_18_ttest_IBM_2013.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import stats 
import scipy as sp
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
ticker='ibm' 
begdate=(2013,1,1) 
enddate=(2013,12,31) 
p=getData(ticker,begdate,enddate,asobject=True, adjusted=True)  
ret=p.aclose[1:]/p.aclose[:-1]-1
print(' Mean T-value P-value ' ) 
print(round(sp.mean(ret),5), stats.ttest_1samp(ret,0))
