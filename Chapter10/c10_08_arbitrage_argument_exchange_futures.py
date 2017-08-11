"""
  Name     : c10_08_abtitrage_ragument_exchange_futures.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
#
obligationForeign=1.0           # how much to pay in 3 months
f=1.26                          # future price
s0=1.25                         # today's exchnage rate 
rHome=0.01
rForeign=0.02
T=3./12.

todayObligationForeign=obligationForeign*sp.exp(-rForeign*T)
usBorrow=todayObligationForeign*s0  
costDollarBorrow=usBorrow*sp.exp(rHome*T)

profit=f*obligationForeign-costDollarBorrow
print("profit in USD =", profit)






