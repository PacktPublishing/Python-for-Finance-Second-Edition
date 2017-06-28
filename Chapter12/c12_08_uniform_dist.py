
"""
  Name     : c12_08_uniform_dist.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
sp.random.seed(123345) 
x=sp.random.uniform(low=1,high=100,size=10) 
print(x[0:5])
