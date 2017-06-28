"""
  Name     : c15_06_LSPD.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import pandas as pd 
from scipy import stats
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
#
ticker='IBM' 
begdate=(2009,1,1) 
enddate=(2013,12,31)
p =getData(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = p.aclose[1:]/p.aclose[:-1]-1
date_=p.date
x=pd.DataFrame(data=ret,index=date_[1:],columns=['ret']) 
#
ff=pd.read_pickle('c:/temp/ffDaily.pkl') 
final=pd.merge(x,ff,left_index=True,right_index=True) 
#
k=final.ret-final.Rf
k2=k[k<0] 
LPSD=np.std(k2)*np.sqrt(252)
print("LPSD=",LPSD)
print(' LPSD (annualized) for ', ticker, 'is ',round(LPSD,3))
 
