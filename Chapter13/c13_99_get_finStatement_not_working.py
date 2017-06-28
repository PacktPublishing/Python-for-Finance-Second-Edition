"""
  Name     : c13_99_get_finStatement.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import urllib2
import pandas as pd

url='http://financials.morningstar.com/income-statement/is.html?t=IBM&region=usa&culture=en-US'
x= pd.read_csv(url, skiprows=10, index_col=0)
