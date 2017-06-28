"""
  Name     : c13_03_print_moodyAAAyield.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_pickle("c:/temp/moodyAAAyield.p")
print(x.head())
print(x.tail())







