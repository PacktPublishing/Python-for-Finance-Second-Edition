# -*- coding: utf-8 -*-
"""
  Name     : c4_11_from_daily_ret_to_annual.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import pandas as pd
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
ticker='IBM'
begdate=(1980,1,1)
enddate=(2012,12,31)
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
logret = np.log(x.aclose[1:]/x.aclose[:-1])

date=[]
d0=x.date
for i in range(0,np.size(logret)):
    date.append(d0[i].strftime("%Y"))

y=pd.DataFrame(logret,date,columns=['retAnnual'])
ret_annual=np.exp(y.groupby(y.index).sum())-1
