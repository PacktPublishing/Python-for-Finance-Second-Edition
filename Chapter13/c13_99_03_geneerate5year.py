"""
  Name     : c13_99_03_generate5year.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_csv("c:/temp/migration5year.csv",index_col=0)
y=x/100
print(y)
y.to_pickle("c:/temp/migration5year.pkl")
