"""
  Name     : c6_10_save_price_data_from_Yahoo.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import re
ticker='msft'
f=open("c:/temp/msft3.txt","w")
begdate=(2013,1,1)
enddate=(2013,11,9)
p = getData(ticker, begdate, enddate,asobject=True,adjusted=True)
f.write(str(p))
f.close()
