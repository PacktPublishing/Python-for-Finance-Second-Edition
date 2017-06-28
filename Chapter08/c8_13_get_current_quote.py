"""
  Name     : c8_13_get_current_quote.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas_datareader.data as web
ticker='AMZN'
print(web.get_quote_yahoo(ticker))