# -*- coding: utf-8 -*-
"""
  Name     : c4_08_get_data.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import datetime    
import pandas_datareader.data as getData
begdate = datetime.datetime(1962, 11, 1)
enddate = datetime.datetime(2016, 11, 7)
df = getData.DataReader("IBM", 'google', begdate, enddate)
