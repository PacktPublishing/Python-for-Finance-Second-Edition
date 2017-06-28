# -*- coding: utf-8 -*-
"""
  Name     : c4_07_first_one.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
p = getData("IBM", (2015,1,1), (2015,12,31),asobject=True, adjusted=True)
print(p[0:5])




