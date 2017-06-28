# -*- coding: utf-8 -*-
"""
  Name     : c4_12_get_ffMonthly.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas_datareader.data as getData
ff =getData.DataReader("F-F_Research_Data_Factors", "famafrench")
