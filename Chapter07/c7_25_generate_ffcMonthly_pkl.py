"""
  Name     : c7_25_generateffcMonthly_pkl.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
ff=pd.read_pickle("c:/temp/ffMonthly.pkl")
print(ff.head(2))

mom=pd.read_pickle("c:/temp/ffMomMonthly.pkl")
print(mom.head(3))

x=pd.merge(ff,mom,left_index=True,right_index=True)
print(x.head())

x.to_pickle("c:/temp/ffcMonthly.pkl")


