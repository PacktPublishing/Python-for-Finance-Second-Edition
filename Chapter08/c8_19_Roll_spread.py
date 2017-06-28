
"""
  Name     : c8_19_Roll_spread.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import scipy as sp 
ticker='IBM' 
begdate=(2013,9,1) 
enddate=(2013,11,11) 
data= getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
p=data.aclose 
d=sp.diff(p)
cov_=sp.cov(d[:-1],d[1:]) 
if cov_[0,1]<0: 
    print("Roll spread for ", ticker, 'is', round(2*sp.sqrt(-cov_[0,1]),3)) 
else: 
    print("Cov is positive for ",ticker, 'positive', round(cov_[0,1],3)) 

