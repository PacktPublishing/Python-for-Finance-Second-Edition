"""
  Name     : c11_08_second_way_to_calculate_10day_VaR.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import pandas as pd 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
from scipy.stats import norm

# input area
ticker='WMT'            # input 1
n_shares=50             # input 2
confidence_level=0.99   # input 3
nDays=10                # input 4
begdate=(2012,1,1)      # input 5
enddate=(2016,12,31)    # input 6

#
z=norm.ppf(confidence_level) 
x = getData(ticker, begdate, enddate,asobject=True, adjusted=True)
logret = np.log(x.aclose[1:]/x.aclose[:-1])

# method 2: calculate 10 day returns 
ddate=[]
d0=x.date
for i in range(0,np.size(logret)): 
    ddate.append(int(i/nDays))
y=pd.DataFrame(logret,ddate,columns=['retNdays']) 
retNdays=y.groupby(y.index).sum()
#print(retNdays.head())
position=n_shares*x.close[0] 
VaR=position*z*np.std(retNdays)
print("Holding=",position, "VaR=", round(VaR,4), "in ", nDays, "Days")
