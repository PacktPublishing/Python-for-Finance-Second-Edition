# -*- coding: utf-8 -*-
"""
  Name     : c1_18_many_useful_commands.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
a=np.zeros(10)                    # array with 10 zeros
b=np.zeros((3,2),dtype=float)     # 3 by 2 with zeros
c=np.ones((4,3),float)            # 4 by 3 with all ones
d=np.array(range(10),float)       # 0,1, 2,3 .. up to 9
e1=np.identity(4)                 # identity 4 by 4 matrix
e2=np.eye(4)                      # same as above
e3=np.eye(4,k=1)                  # 1 start from k
f=np.arange(1,20,3,float)         # from 1 to 19 interval 3
g=np.array([[2,2,2],[3,3,3]])     # 2 by 3
h=np.zeros_like(g)                # all zeros
i=np.ones_like(g)                 # all ones
