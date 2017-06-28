# -*- coding: utf-8 -*-
"""
  Name     : c6_02_random_OLS.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import stats 
import scipy as sp
sp.random.seed(12456)
alpha=1.0
beta=0.8
n=100
x=sp.arange(n)
y=alpha+beta*x+sp.random.rand(n)
(beta, alpha, r_value, p_value, std_err) = stats.linregress(y,x) 
print(alpha,beta) 
print("R-squared=", r_value**2)
print("p-value =", p_value)
