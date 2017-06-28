"""
  Name     : c11_04_show_z_genative.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy.stats import norm
confidence_level=0.99
z=norm.ppf(1-confidence_level)
print(z)
