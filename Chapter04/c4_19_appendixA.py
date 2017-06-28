# -*- coding: utf-8 -*-
"""
  Name     : c4_19_appendixA.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import matplotlib.mlab as mlab
from matplotlib.pyplot import *
from matplotlib.finance import quotes_historical_yahoo_ochl as getData
#
ticker='IBM' 
begdate=(2015,1,1) 
enddate=(2015,11,9)
p = getData(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[:1] 
[n,bins,patches] = hist(ret, 100)
mu = np.mean(ret) 
sigma = np.std(ret)
x = mlab.normpdf(bins, mu, sigma) 
plot(bins, x, color='red', lw=2) 
title("IBM return distribution") 
xlabel("Returns") 
ylabel("Frequency")
show()
