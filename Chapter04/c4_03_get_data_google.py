# -*- coding: utf-8 -*-
"""
  Name     : c4_03_get_stock_data_google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import pandas_datareader.data as getData
df = getData.get_data_google("IBM")
print(df.head())
