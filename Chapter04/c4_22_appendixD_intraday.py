# -*- coding: utf-8 -*-
"""
  Name     : c4_022_AppendixD_introday.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import pandas as pd
import datetime as datetime 
import matplotlib.pyplot as plt
ticker='AAPL'
path='http://www.google.com/finance/getprices?q=ttt&i=60&p=1d&f=d,o,h,l,c,v'
p=np.array(pd.read_csv(path.replace('ttt',ticker),skiprows=7,header=None))
#
date=[]
for i in np.arange(0,len(p)): 
    if p[i][0][0]=='a':
        t= datetime.datetime.fromtimestamp(int(p[i][0].replace('a',''))) 
        date.append(t)
    else:
        date.append(t+datetime.timedelta(minutes =int(p[i][0])))
#	        
final=pd.DataFrame(p,index=date) 
final.columns=['a','Open','High','Low','Close','Vol'] 
del final['a']
#	
x=final.index 
y=final.Close
#	
plt.title('Intraday price pattern for ttt'.replace('ttt',ticker)) 
plt.xlabel('Price of stock')
plt.ylabel('Intro-day price pattern') 
plt.plot(x,y)
plt.show()
