"""
  Name     : c8_35_Pandas_OLS.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np 
import pandas as pd 
from datetime import datetime 
n = 252 
np.random.seed(12345) 
begdate=datetime(2013, 1, 2) 
dateRange = pd.date_range(begdate, periods=n) 
x0= pd.DataFrame(np.random.randn(n, 1),columns=['ret'],index=dateRange) 
y0=pd.Series(np.random.randn(n), index=dateRange) 
print pd.ols(y=y0, x=x0)
