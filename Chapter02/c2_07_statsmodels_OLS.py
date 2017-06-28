# -*- coding: utf-8 -*-
"""
  Name     : c2_07_statsmodels_OLD.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import statsmodels.api as sm
y=[1,2,3,4,2,3,4]
x=range(1,8)
x=sm.add_constant(x)
results=sm.OLS(y,x).fit()
print(results.params)




