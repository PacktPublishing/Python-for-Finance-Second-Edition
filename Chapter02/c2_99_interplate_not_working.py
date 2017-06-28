"""
  Name     : c2_04_interplate_not_worling.py
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
x=np.arange(1, 3, .25)**2
n=np.size(x)
y = pd.Series(x + np.random.randn(n))

bad = np.array([4, 13, 14, 15, 16, 20, 30])

x[bad] = np.nan
methods = ['linear', 'quadratic', 'cubic']
df = pd.DataFrame({m: x.interpolate(method=m) for m in methods})
#df=x.interpolate(method="linear")
df.plot()

