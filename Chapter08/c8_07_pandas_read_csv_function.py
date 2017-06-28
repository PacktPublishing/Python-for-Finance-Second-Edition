"""
  Name     : c8_07_pandas_read+csv_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd 
url='http://canisius.edu/~yany/data/ibm.csv'  
x=pd.read_csv(url,index_col=0,parse_dates=True) 
print(x.head())
