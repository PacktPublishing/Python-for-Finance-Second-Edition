"""
  Name     : c8_20_test_January_effect.py
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
from datetime import datetime 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
ticker='IBM' 
begdate=(1962,1,1) 
enddate=(2016,12,31) 
x =getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
logret = sp.log(x.aclose[1:]/x.aclose[:-1]) 
date=[] 
d0=x.date 
for i in range(0,sp.size(logret)): 
    t1=''.join([d0[i].strftime("%Y"),d0[i].strftime("%m"),"01"]) 
    date.append(datetime.strptime(t1,"%Y%m%d")) 

y=pd.DataFrame(logret,date,columns=['logret']) 
retM=y.groupby(y.index).sum() 
ret_Jan=retM[retM.index.month==1] 
ret_others=retM[retM.index.month!=1] 
print(sp.stats.ttest_ind(ret_Jan.values,ret_others.values))


