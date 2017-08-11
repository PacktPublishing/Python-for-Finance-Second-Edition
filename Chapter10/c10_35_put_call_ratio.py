"""
  Name     : c10_35_put_call_ratio.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
import pandas as pd
from matplotlib.pyplot import *
#
infile='c:/temp/totalpc.csv'
data=pd.read_csv(infile,skiprows=2,index_col=0,parse_dates=True)
data.columns=('Calls','Puts','Total','Ratio') 
x=data.index
y=data.Ratio 
y2=sp.ones(len(y)) 
title('Put-call ratio') 
xlabel('Date') 
ylabel('Put-call ratio') 
ylim(0,1.5)
plot(x, y, 'b-')
plot(x, y2,'r') 
show()