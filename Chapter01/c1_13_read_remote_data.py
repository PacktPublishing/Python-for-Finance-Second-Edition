# -*- coding: utf-8 -*-
"""
  Name     : c1_13_read_remote_data.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
url='http://canisius.edu/~yany/data/ibm.csv'
x=pd.read_csv(url)
print(x.head())