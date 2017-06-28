"""
  Name     : c6_07_read_csv_file.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
f=pd.read_csv("c:\\temp\\ibm.csv")
print(f[1:3])