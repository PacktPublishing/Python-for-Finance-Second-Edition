# -*- coding: utf-8 -*-
"""
  Name     : c7_03_random_OLS.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import scipy as sp
import statsmodels.regression.linear_model as sm

n=100
sp.random.seed(12345)

y=[1,2,3,4,2,3,4]
x1=range(1,8)
x2=[4,2,-1,4,2,3,5]
x3=[0,2,3,4,2,4,-1]
x=[x1,x2,x3]
x=sm.add_constant(x)
#est = sm.OLS(formula='Sales ~ TV + Radio', data=df_adv).fit()
results=sm.OLS(y,x1).fit()
print(results.summary())
