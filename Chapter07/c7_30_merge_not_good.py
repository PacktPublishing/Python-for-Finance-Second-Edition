"""
  Name     : c7_30_merge_not_good.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.DataFrame([[40,50],[0.2,0.3]],rows=['A','B'])
y=pd.DataFrame([[30,22],[0.1,-0.25]],rows=['C','B'])
z=pd.merge(x,y)

