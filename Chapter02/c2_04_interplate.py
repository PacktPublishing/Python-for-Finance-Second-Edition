"""
  Name     : c2_04_interplate.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import pandas as pd
#
np.random.seed(123)
x=np.arange(1, 3.1, .25)**2
n=np.size(x)
y = pd.Series(x + np.random.randn(n))
print(y)
y[4]=np.nan
print(y)
z=y.interpolate()
print(z)

