"""
  Name     : c13_99_03_generateBondSpread2014.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_csv("c:/temp/bondSpread2014.csv")
x.to_pickle("c:/temp/bondSpread2014.p")
print(x.head())
print(x.tail())

