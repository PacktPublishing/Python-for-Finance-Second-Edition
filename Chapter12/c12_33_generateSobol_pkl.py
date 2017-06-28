# -*- coding: utf-8 -*-

"""
  Name     : c12_33_generateSobol.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import sobol_seq
import scipy as sp
import pandas as pd
a=[]
n=1000
for i in sp.arange(n):
     t=sobol_seq.i4_sobol(1,i)
     a.append(t)
print(a[0:10])
b=pd.DataFrame(a,columns=['Sobol','b'])
sobol=b['Sobol']
sobol.to_pickle("e:/sobol.pkl")