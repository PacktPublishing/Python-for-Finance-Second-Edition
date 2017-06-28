# -*- coding: utf-8 -*-
"""
  Name     : c1_20_matrix_dot_product.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
a=np.array([[1,2,3],[4,5,6]],float)   # 2 by 3
b=np.array([[1,2],[3,3],[4,5]],float) # 3 by 2
np.dot(a,b)                           # 2 by 2
print(np.dot(a,b))