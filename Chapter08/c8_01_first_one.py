"""
  Name     : c8_01_first_one.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd 
import scipy as sp
mean=0.10
std=0.2
ddate = pd.date_range('1/1/2016', periods=252) 
n=len(ddate)

data = pd.Series(sp.random.normal(mean,std,n), index=ddate)
print(data.head())