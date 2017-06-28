"""
  Name     : c11_21_ES_z_value_normal_distribution.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
sp.random.seed(12345) 
n=5000000
ret=sp.random.normal(0,1,n) 
print(ret[0:5] )


