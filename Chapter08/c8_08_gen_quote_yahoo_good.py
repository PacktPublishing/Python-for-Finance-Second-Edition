"""
  Name     : c8_08_get_quote_yahoo_good.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas_datareader.data as web
ticker='AMZN'
print(web.get_quote_yahoo (ticker))
