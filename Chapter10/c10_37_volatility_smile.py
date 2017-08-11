"""
  Name     : c10_37_volatility_smile.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ochl as getData

# Step 1: input area
infile="c:/temp/callsFeb2014.pkl"
ticker='IBM'
r=0.0003                          # estimate
begdate=datetime.date(2010,1,1)   # this is arbitrary 
enddate=datetime.date(2014,2,1)   # February 2014

# Step 2: define a function 
def implied_vol_call_min(S,X,T,r,c): 
    from scipy import log,exp,sqrt,stats 
    implied_vol=1.0
    min_value=1000
    for i in range(10000): 
        sigma=0.0001*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T)) 
        d2 = d1-sigma*sqrt(T)
        c2=S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2) 
        abs_diff=abs(c2-c)
        if abs_diff<min_value: 
            min_value=abs_diff 
            implied_vol=sigma 
            k=i
    return implied_vol


# Step 3: get call option data 
calls=pd.read_pickle(infile)
exp_date0=int('20'+calls.Symbol[0][len(ticker):9])  # find expiring date
p = getData(ticker, begdate,enddate,asobject=True, adjusted=True)
s=p.close[-1]                    # get current stock price 
y=int(exp_date0/10000)
m=int(exp_date0/100)-y*100
d=exp_date0-y*10000-m*100
exp_date=datetime.date(y,m,d)    # get exact expiring date 
T=(exp_date-enddate).days/252.0  # T in years

# Step 4: run a loop to estimate the implied volatility 
n=len(calls.Strike)   # number of strike
strike=[]             # initialization
implied_vol=[]        # initialization
call2=[]              # initialization
x_old=0               # used when we choose the first strike 

for i in range(n):
    x=calls.Strike[i]
    c=(calls.Bid[i]+calls.Ask[i])/2.0
    if c >0:
        print ('i=',i,',    c=',c)
        if x!=x_old:
            vol=implied_vol_call_min(s,x,T,r,c)
            strike.append(x)
            implied_vol.append(vol)
            call2.append(c)
            print x,c,vol
            x_old=x

# Step 5: draw a smile 
plt.title('Skewness smile (skew)') 
plt.xlabel('Exercise Price') 
plt.ylabel('Implied Volatility')
plt.plot(strike,implied_vol,'o')
plt.show()
