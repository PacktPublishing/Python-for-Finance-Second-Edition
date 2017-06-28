"""
  Name     : c7_41_generte_ibmMonthly_pkl.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import scipy as sp
import time
# b=time.strptime(x['Date'][0],"%Y-%m-%d")
x=pd.read_csv("c:/temp/ibmMonthly.csv",index_col=0)
n=len(x)

"""
ddate=[]
for i in sp.arange(n):
    ddate.append(time.strptime(x['Date'][i],"%Y-%m-%d"))
 
#ibmMonthly=pd.DataFrame(x['Open'],x['High'],x['Low'],x['Close'],x['Volume'],x['Adj Close'],index=ddate)
#ibmMonthly=pd.DataFrame(x,columns=[['DATE','OPEN','HIGH','LOW','CLOSE','VOLUME','ADJCLOSE']])
"""

ibmMonthly=pd.DataFrame(x)

ret=-x['Adj Close'].diff(-1)/x['Adj Close'].shift(-1)
#dd=x['Adj Close'].shift(-1)

ibmMonthly['RET']=ret
ibmMonthly.to_pickle("c:/temp/ibmMonthly.pkl")
