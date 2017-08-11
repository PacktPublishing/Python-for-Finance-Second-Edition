"""
  Name     : c10_44_implied_vol_binary_search.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import log,exp,sqrt,stats 
S=42;X=40;T=0.5;r=0.01;c=3.0
def bsCall(S,X,T,r,sigma):
    d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T)) 
    d2 = d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
#
def impliedVolBinary(S,X,T,r,c):
    k=1
    volLow=0.001
    volHigh=1.0
    cLow=bsCall(S,X,T,r,volLow)
    cHigh=bsCall(S,X,T,r,volHigh)
    if cLow>c or cHigh<c:
        raise ValueError
    while k ==1:
        cLow=bsCall(S,X,T,r,volLow)
        cHigh=bsCall(S,X,T,r,volHigh)
        volMid=(volLow+volHigh)/2.0
        cMid=bsCall(S,X,T,r,volMid)
        if abs(cHigh-cLow)<0.01:
            k=2
        elif cMid>c:
            volHigh=volMid
        else:
            volLow=volMid
    return volMid, cLow, cHigh
#
print("Vol,     cLow,      cHigh")
print(impliedVolBinary(S,X,T,r,c))