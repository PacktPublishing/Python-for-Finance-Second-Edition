"""
  Name     : c6_28_OLS_example.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
from pandas.stats.api import ols
yRet= [0.1,0.22,0.12,0.04,-0.12]
xRet=[0.1, 0.11, 0.05, -0.04, 0.22]

df = pd.DataFrame({"y":yRet,"x":xRet})
result = ols(y=df['y'], x=df['x'])
print(result)

