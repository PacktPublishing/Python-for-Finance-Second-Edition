"""
  Name     : c8_44_relative_spread_TORQcq.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import pandas as pd 
import scipy as sp
cq=pd.read_pickle('c:/temp/TORQcq.pkl') 
x=cq[cq.index=='MO'] 
spread=sp.mean(x.ofr-x.bid) 
rel_spread=sp.mean(2*(x.ofr-x.bid)/(x.ofr+x.bid)) 
print(round(spread,5) )
print(round(rel_spread,5) )
