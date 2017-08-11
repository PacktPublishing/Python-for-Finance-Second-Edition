"""
  Name     : c10_33_implied_vol_EuropeanPut_min.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from scipy import log,exp,sqrt,stats 

def implied_vol_put_min(S,X,T,r,p):
    implied_vol=1.0
    min_value=100.0
    for i in xrange(1,10000): 
        sigma=0.0001*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T)) 
        d2 = d1-sigma*sqrt(T)
        put=X*exp(-r*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1) 
        abs_diff=abs(put-p)
        if abs_diff<min_value: 
            min_value=abs_diff 
            implied_vol=sigma 
            k=i
        put_out=put
    print 'k, implied_vol, put, abs_diff' 
    return k,implied_vol, put_out,min_value