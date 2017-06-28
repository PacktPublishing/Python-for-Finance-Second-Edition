# -*- coding: utf-8 -*-
"""
  Name     : c1_19_flatten_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
#
x=np.array([[1,2],[5,6],[7,9]])     # a 3 by 2 array
print(x)
y=x.flatten()
print(y)
x2=np.reshape(y,[2,3])
print(x2)