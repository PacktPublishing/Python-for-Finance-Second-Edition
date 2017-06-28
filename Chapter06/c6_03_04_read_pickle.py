"""
  Name     : c6_04_read_pickle.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_pickle("c:/temp/yanMonthly.pkl ")
print(x[0:10])
