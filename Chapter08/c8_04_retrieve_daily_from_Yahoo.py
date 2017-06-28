"""
  Name     : c8_04_retrieve_daily_from_Yahoo.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
x = getData("IBM",(2016,1,1),(2016,1,21),asobject=True, adjusted=True)
print(x[0:4])

