# -*- coding: utf-8 -*-

"""
  Name     : c7_01_3factor_model.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


from scipy import stats 
from pandas.stats.api import ols
import pandas as pd
y = [0.065, 0.0265, -0.0593, -0.001,0.0346] 
x1 = [0.055, -0.09, -0.041,0.045,0.022]
x2 = [0.025, 0.10, 0.021,0.145,0.012]
x3=  [0.015, -0.08, 0.341,0.245,-0.022]

df=pd.DataFrame({"y":y,"x1":x1, 'x2':x2,'x3':x3})
result=ols(y=df['y'],x=df[['x1','x2','x3']])
print(result)
