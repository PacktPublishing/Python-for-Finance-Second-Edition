
"""
  Name     : c12_21_use_permulation_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import numpy as np 
x=range(1,11) 
print(x) 
for i in range(5):
    y=np.random.permutation(x) 
#
print(y)
