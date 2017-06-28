"""
  Name     : c9_12_get_ert_matrix_from_yanMonthly.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import scipy as sp
df=pd.read_pickle("c:/temp/yanMonthly.pkl")
#print(df[0:10])

print(sp.unique(df.index))


"""
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import numpy as np 
import pandas as pd 

ticker='IBM' 
begdate=(2016,1,2) 
enddate=(2017,1,9) 
x =getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
myName=ticker+'_adjClose'
x2=pd.DataFrame(x['aclose'],x.date,columns=[myName]) 
ff=pd.read_pickle('c:/temp/ffDaily.pkl') 
final=pd.merge(x2,ff,left_index=True,right_index=True)
print(final.head())
"""
