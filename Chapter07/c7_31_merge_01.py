"""
  Name     : c7_31_mrege_01.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
import pandas as pd
#
x= pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                 'A': ['A0', 'A1', 'A2', 'A3'],
                 'B': ['B0', 'B1', 'B2', 'B3']})
y = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K6'],
                  'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3']})
print(sp.shape(x))
print(sp.shape(y))
print(x)
print(y)

result = pd.merge(x,y, on='key')
print(result)

result2=pd.merge(x,y)
print(result2)

