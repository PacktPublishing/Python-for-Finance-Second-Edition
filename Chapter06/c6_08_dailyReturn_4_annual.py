"""
  Name     : c6_08_beta_4_IBM.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import scipy as sp
import pandas as pd
from scipy import stats 
from matplotlib.finance import quotes_historical_yahoo_ochl 

def ret_f(ticker,begdate, enddate):
    p = quotes_historical_yahoo_ochl(ticker, begdate,    
    enddate,asobject=True,adjusted=True)
    return((p.aclose[1:] - p.aclose[:-1])/p.aclose[:-1])
#
begdate=(2010,1,1)
enddate=(2016,12,31)
#
y0=pd.Series(ret_f('IBM',begdate,enddate))
x0=pd.Series(ret_f('^GSPC',begdate,enddate))
#
d=quotes_historical_yahoo_ochl('^GSPC', begdate, enddate,asobject=True,adjusted=True).date[0:-1]
lag_year=d[0].strftime("%Y")
y1=[]
x1=[]
beta=[]
index0=[]
for i in sp.arange(1,len(d)):
    year=d[i].strftime("%Y")
    if(year==lag_year):
       x1.append(x0[i])
       y1.append(y0[i])
    else:
       (beta,alpha,r_value,p_value,std_err)=stats.linregress(y1,x1) 
       alpha=round(alpha,8)
       beta=round(beta,3)
       r_value=round(r_value,3)
       p_vaue=round(p_value,3)
       print(year,alpha,beta,r_value,p_value)
       x1=[]
       y1=[]
       lag_year=year
