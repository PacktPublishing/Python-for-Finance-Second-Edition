"""
  Name     : c6_14_get_sp500.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import re
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
ticker='^GSPC'
begdate=(2013,1,1)
enddate=(2013,11,9)
df = getData(ticker, begdate, enddate,asobject=True,adjusted=True)
f=open("c:/temp/sp500.txt","w")
f.write(str(df))
f.close()


