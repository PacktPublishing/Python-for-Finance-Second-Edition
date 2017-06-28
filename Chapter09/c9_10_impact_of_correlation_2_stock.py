"""
  Name     : c9_10_impact_of_correlation_2stocks.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import matplotlib.pyplot as plt
sp.random.seed(123)
n=1000

sigma1=0.3
sigma2=0.20

n_step=20

for i in sp.arange(n_step):
    print i
