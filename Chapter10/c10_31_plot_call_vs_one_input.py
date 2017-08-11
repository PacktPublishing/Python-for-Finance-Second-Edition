# -*- coding: utf-8 -*-
"""
  Name     : c10_31_plot_call_vs_one_inut.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np 
import p4f as pf
import matplotlib.pyplot as plt
s0=30;T0=0.5;sigma0=0.2;r0=0.05;x0=30
sigma=np.arange(0.05,0.8,0.05) 
T=np.arange(0.5,2.0,0.5) 
call_0=pf.bs_call(s0,x0,T0,r0,sigma0) 
call_sigma=pf.bs_call(s0,x0,T0,r0,sigma) 
call_T=pf.bs_call(s0,x0,T,r0,sigma0) 
plt.plot(sigma,call_sigma,'b') 
plt.plot(T,call_T)
plt.show()




