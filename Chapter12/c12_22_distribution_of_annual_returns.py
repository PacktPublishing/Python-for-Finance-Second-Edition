
"""
  Name     : c12_22_distribution_of_annual_returns.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np 
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
# Step 1: input area
ticker='MSFT'	        # input value 1 
begdate=(1926,1,1)      # input value 2 
enddate=(2013,12,31)    # input value 3 
n_simulation=5000       # input value 4

# Step 2: retrieve price data and estimate log returns
x=getData(ticker,begdate,enddate,asobject=True)
logret = sp.log(x.aclose[1:]/x.aclose[:-1])

# Step 3: estimate annual returns 
date=[]
d0=x.date
for i in range(0,sp.size(logret)): 
    date.append(d0[i].strftime("%Y"))

y=pd.DataFrame(logret,date,columns=['logret']) 
ret_annual=sp.exp(y.groupby(y.index).sum())-1 
ret_annual.columns=['ret_annual']
n_obs=len(ret_annual)

# Step 4: estimate distribution with replacement 
sp.random.seed(123577) 
final=sp.zeros(n_obs,dtype=float)
for i in range(0,n_obs):
    x=sp.random.uniform(low=0,high=n_obs,size=n_obs) 
    y=[]
    for j in range(n_obs): 
        y.append(int(x[j]))
        z=np.array(ret_annual)[y] 
    final[i]=sp.mean(z)

# step 5: graph
plt.title('Mean return distribution: number of simulations ='+str(n_simulation))
plt.xlabel('Mean return')
plt.ylabel('Frequency')
mean_annual=round(np.mean(np.array(ret_annual)),4) 
plt.figtext(0.63,0.8,'mean annual='+str(mean_annual)) 
plt.hist(final, 50, normed=True)
plt.show()
