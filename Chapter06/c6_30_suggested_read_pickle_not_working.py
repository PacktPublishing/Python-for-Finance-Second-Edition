"""
  Name     : c6_30_suggested_read_pickle_not_working.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import cStringIO
import urllib2
loc="http://canisius.edu/~yany/python/yanMonthly.pkl"
x=pd.read_pickle(cStringIO.StringIO(urllib2.urlopen(loc).read()))


y=cStringIO.StringIO(urllib2.urlopen(loc).read())