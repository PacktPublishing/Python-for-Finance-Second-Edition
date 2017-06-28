# -*- coding: utf-8 -*-
"""
  Name     : c13_09_getIpriceYahoo.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from yahoo_finance import Share
yahoo = Share('YHOO')
print(yahoo.get_open())
print(yahoo.get_price())
print(yahoo.get_trade_datetime())
