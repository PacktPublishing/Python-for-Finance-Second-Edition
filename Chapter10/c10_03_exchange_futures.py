
"""
  Name     : c10_03_exchange_futures.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
def futuresExchangeRate(s0,rateDomestic,rateForeign,T):
    futureEx=s0*sp.exp((rateDomestic-rateForeign)*T)
    return futureEx

s0=1.25
rHome=0.01
rForeigh=0.02
T=3./12.
futures=futuresExchangeRate(s0,rHome,rForeigh,T)
print("futures=",futures)
