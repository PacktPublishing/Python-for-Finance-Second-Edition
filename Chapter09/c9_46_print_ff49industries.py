"""
  Name     : c9_461_print_ff49industries.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_pickle("c:/temp/ff49industries.pkl")
print(x.head(2))
