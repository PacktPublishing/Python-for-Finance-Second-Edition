"""
  Name     : c10_36_put_call_ratio_add_trend.py
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
import matplotlib.pyplot as plt 
from datetime import datetime 
import statsmodels.api as sm
#
data=pd.read_csv('c:/temp/totalpc.csv',skiprows=2,index_col=0,parse_dates=True)
data.columns=('Calls','Puts','Total','Ratio') 
begdate=datetime(2013,6, 1) 
enddate=datetime(2013,12,31)
data2=data[(data.index>=begdate) & (data.index<=enddate)] 
x=data2.index
y=data2.Ratio 
x2=range(len(x)) 
x3=sm.add_constant(x2) 
model=sm.OLS(y,x3) 
results=model.fit()

#print results.summary() 
alpha=round(results.params[0],3) 
slope=round(results.params[1],3) 
y3=alpha+sp.dot(slope,x2) 
y2=sp.ones(len(y))
title('Put-call ratio with a trend') 
xlabel('Date') 
ylabel('Put-call ratio') 
ylim(0,1.5)
plot(x, y, 'b-')
plt.plot(x, y2,'r-.')
plot(x,y3,'y+')
plt.figtext(0.3,0.35,'Trend: intercept='+str(alpha)+',slope='+str(slope)) 
show()
