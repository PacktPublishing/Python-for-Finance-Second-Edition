# -*- coding: utf-8 -*-

"""
  Name     : c11_18_sort_pandas.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
a = pd.DataFrame([[9,4],[9,2],[1,-1]],columns=['A','B'])
print(a)
# sort by A ascedning, then B descending 
b= a.sort_values(['A', 'B'], ascending=[1, 0])
print(b)
# sort by A and B, both ascedning 
c= a.sort_values(['A', 'B'], ascending=[1, 1])
print(c)