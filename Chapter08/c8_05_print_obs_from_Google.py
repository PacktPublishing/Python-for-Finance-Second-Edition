"""
  Name     : c8_05_print_obs_from_Google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas_datareader.data as getData
import re
ticker='msft'
p = getData.DataReader(ticker, "google")
print(p.head())
