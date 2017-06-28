"""
  Name     : c12_06_randard_numbers_with_seed.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
sp.random.seed(12345) 
x=sp.random.normal(0,1,20) 
print x[0:5] 
