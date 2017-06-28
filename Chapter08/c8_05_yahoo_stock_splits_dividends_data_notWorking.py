"""
  Name     : c8_05_print_obs_from_Google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""



import pandas_datareader.data as web
import datetime
ticker='WMT'
begdate = datetime.datetime(2010, 1, 1)
enddate= datetime.datetime(2015, 5, 9)
x=web.DataReader(ticker,'yahoo-actions',begdate,enddate)
print(x.head())