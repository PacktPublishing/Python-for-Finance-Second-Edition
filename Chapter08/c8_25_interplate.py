"""
  Name     : c8_25_interplate.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd 
import numpy as np 
nn=np.nan
x=pd.Series([1,2,nn,nn,6]) 
print(x.interpolate())

