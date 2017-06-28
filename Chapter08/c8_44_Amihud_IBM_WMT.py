"""
  Name     : c8_44_Amihud_IBM_WMT.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import numpy as np 
import statsmodels.api as sm 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
begdate=(2013,10,1) 
enddate=(2013,10,30) 
ticker='IBM'                   # or WMT  
data= getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
p=np.array(data.aclose) 
dollar_vol=np.array(data.volume*p) 
ret=np.array((p[1:] - p[:-1])/p[1:]) 
illiq=np.mean(np.divide(abs(ret),dollar_vol[1:])) 
print("Aminud illiq for =",ticker,illiq) 

