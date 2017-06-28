# -*- coding: utf-8 -*-
"""
  Name     : c4_06_read_local_csv_file.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_csv("c:/temp/ibm.csv")
print(x.head())
