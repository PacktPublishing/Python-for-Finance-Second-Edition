"""
  Name     : c9_99_01_generate_stockMonthly.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd

x=pd.read_csv("c:/temp/stockMonthly2.csv")
#y=pd.DataFrame(x)
x.columns=['PERMNO','DATE','RETURN','VOLUME','PRICE','SHARESOUTSTNDING']
#print(y.head())
#print(y.tail())
x.to_pickle('c:/temp/stockMonthly.pkl')


