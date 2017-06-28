"""
  Name     : c8_36_Fama_MecBeth_regression.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np 
import pandas as pd 
import statsmodels.api as sm
from datetime import datetime 
#
n = 252 
np.random.seed(12345) 
begdate=datetime(2013, 1, 2) 
dateRange = pd.date_range(begdate, periods=n) 
def makeDataFrame(): 
    data=pd.DataFrame(np.random.randn(n,7),columns=['A','B','C','D','E',' F','G'],
    index=dateRange) 
    return data 
#
data = { 'A': makeDataFrame(), 'B': makeDataFrame(), 'C': makeDataFrame() }
Y = makeDataFrame() 
print(pd.fama_macbeth(y=Y,x=data))
