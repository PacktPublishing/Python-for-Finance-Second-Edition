# generate ff_monthly.pickle   

"""
  Name     : c4_28_federal_fund_rate.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import numpy as np
infile="c:/temp/fedFundRate.csv"
data=pd.read_csv(infile,skiprows=6,header=None)

#data=pd.read_csv(file,skiprows=3)
dd=rate=[]
n=len(data)
y=np.array(data)
rate=[]

for i in np.arange(n):
    t=y[i][0]
    dd.append(pd.to_datetime(t, format='%Y-%m-%d').date())
    rate.append(y[i][1]/100.)
#
fedFundRate=pd.DataFrame(rate,index=dd,columns=['FEDFUNDRATE'])
fedFundRate.to_pickle("c:/temp/fedFundRate.pkl")    


