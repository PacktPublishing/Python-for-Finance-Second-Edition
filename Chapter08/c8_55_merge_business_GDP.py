"""
  Name     : c8_55_merge_business_GDP.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import datetime
import scipy as sp
import numpy as np
import pandas as pd
import pandas_datareader.data as web
#
cycle=pd.read_pickle("c:/temp/businessCycle.pkl")
begdate = datetime.datetime(1947, 1, 1)
enddate = datetime.datetime(2017, 1, 27)
GDP= web.DataReader("GDP", "fred", begdate,enddate)
final=pd.merge(cycle,GDP,left_index=True,right_index=True,how='right') 
print(cycle.head())
print(GDP.head())
print(final.head())

final2=final[np.isnan(final.cycle)!=True]
print(sp.corrcoef(final2.cycle,final2.GDP))

