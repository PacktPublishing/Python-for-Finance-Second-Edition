"""
  Name     : c8_03_daily_to_monthly.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import numpy as np
import pandas as pd 

ticker='IBM' 
begdate=(2013,1,1) 
enddate=(2013,11,9)

x = getData(ticker, begdate, enddate,asobject=True, adjusted=True)
logret = np.log(x.aclose[1:]/x.aclose[:-1])
yyyymm=[]
d0=x.date

for i in range(0,np.size(logret)): 
    yyyymm.append(''.join([d0[i].strftime("%Y"),d0[i].strftime("%m")]))

y=pd.DataFrame(logret,yyyymm,columns=['retMonthly']) 
retMonthly=y.groupby(y.index).sum()

print(retMonthly.head())
