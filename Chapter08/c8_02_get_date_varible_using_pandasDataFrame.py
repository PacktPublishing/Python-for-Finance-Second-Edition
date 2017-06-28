"""
  Name     : c8_02_get_date_variable.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd 
import scipy as sp

sp.random.seed(1257)
mean=0.10
std=0.2
ddate = pd.date_range('1/1/2016', periods=252) 
n=len(ddate)
rets=sp.random.normal(mean,std,n)
data = pd.DataFrame(rets, index=ddate,columns=['RET'])
print(data.head())
