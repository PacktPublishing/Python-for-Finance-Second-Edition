"""
  Name     : c8_28_52_week_high.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
from datetime import datetime 
from dateutil.relativedelta import relativedelta 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
ticker='IBM' 
enddate=datetime(2016,12,31)
#
begdate=enddate-relativedelta(years=1) 
p =getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
x=p[-1] 
y=np.array(p.tolist())[:,-1] 
high=max(y) 
low=min(y) 
print(" Today, Price High Low, % from low ") 
print(x[0], x[-1], high, low, round((x[-1]-low)/(high-low)*100,2))
