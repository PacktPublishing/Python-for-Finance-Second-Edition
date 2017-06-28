"""
  Name     : c11_01_normal_density_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy.stats as stats
from scipy import sqrt, exp,pi
d1=stats.norm.pdf(0,0.1,0.05)      
print("d1=",d1)
d2=1/sqrt(2*pi*0.05**2)*exp(-(0.1)**2/0.05**2/2)  # verify manually
print("d2=",d2)




