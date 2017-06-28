"""
  Name     : c12_10_simulate_pi.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
n=100000
x=sp.random.uniform(low=0,high=1,size=n) 
y=sp.random.uniform(low=0,high=1,size=n) 
dist=sp.sqrt(x**2+y**2) 
in_circle=dist[dist<=1] 
our_pi=len(in_circle)*4./n
print ('pi=',our_pi)
print('error (%)=', (our_pi-sp.pi)/sp.pi)
