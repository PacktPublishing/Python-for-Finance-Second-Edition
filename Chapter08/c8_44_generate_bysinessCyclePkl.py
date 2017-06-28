"""
  Name     : c8_44_generate_businessCycle.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_csv("c:/temp/business_cycle.csv",index_col=0,parse_dates=[0])
y=pd.DataFrame(x.cycle,index=x.index,columns=['CYCLE'])
x.to_pickle("c:/temp/businessCycle.pkl")