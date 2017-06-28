"""
  Name     : c9_44_equal_weighted_vs_value_weighted.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import pandas as pd
import scipy as sp

x=pd.read_pickle("c:/temp/yanMonthly.pkl")

def ret_f(ticker):
    a=x[x.index==ticker]
    p=sp.array(a['VALUE'])
    ddate=a['DATE'][1:]
    ret=p[1:]/p[:-1]-1
    out1=pd.DataFrame(p[1:],index=ddate)
    out2=pd.DataFrame(ret,index=ddate)
    output=pd.merge(out1,out2,left_index=True, right_index=True)
    output.columns=['Price_'+ticker,'Ret_'+ticker]
    return output

a=ret_f("IBM")
b=ret_f('WMT')
c=pd.merge(a,b,left_index=True, right_index=True)
print(c.head())

