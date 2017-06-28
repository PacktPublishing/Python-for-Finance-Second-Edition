
"""
  Name     : c8_33_print_TORQcq.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd 
cq=pd.read_pickle("c:/temp/TORQcq.pkl") 
print(cq.head() )
