
"""
  Name     : c12_07_normal_dist.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
sp.random.seed(12345) 
mean=0.05
std=0.1
n=50
x=sp.random.normal(mean,std,n) 
print(x[0:5])


