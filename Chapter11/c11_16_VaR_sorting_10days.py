
"""
  Name     : c11_16_VaR_sorting_10day.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
ticker='WMT'            # input 1
n_shares=500            # input 2
confidence_level=0.99   # input 3
begdate=(2000,1,1)      # input 4
enddate=(2016,12,31)    # input 5
nDays=10                # input 6
#
z=norm.ppf(confidence_level) 
x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
logret = np.log(x.aclose[1:]/x.aclose[:-1])
ret = x.aclose[1:]/x.aclose[:-1]-1
position=n_shares*x.close[0] 
#
# Method I
mean=np.mean(ret)
std=np.std(ret)
meanNdays=(1+mean)**nDays-1
stdNdays=std*np.sqrt(nDays)
z=norm.ppf(confidence_level) 
VaR1=position*z*stdNdays
print("Holding=",position, "VaR1=", round(VaR1,0), "in ", nDays, "Days")
#
# method 2: calculate 10 day returns 
ddate=[]
d0=x.date
for i in range(0,np.size(logret)): 
    ddate.append(int(i/nDays))
y=pd.DataFrame(logret,index=ddate,columns=['retNdays']) 
logRet=y.groupby(y.index).sum()
retNdays=np.exp(logRet)-1
# 
VaR2=position*z*np.std(retNdays)
print("Holding=",position, "VaR2=", round(VaR2,0), "in ", nDays, "Days")
# 
# Method III
ret2=np.sort(retNdays) 
n=np.size(ret2)
leftTail=int(n*(1-confidence_level))
print(leftTail)
#
VaR3=position*ret2[leftTail]
print("Holding=",position, "VaR=", round(VaR3,0), "in ",nDays, "Days")






