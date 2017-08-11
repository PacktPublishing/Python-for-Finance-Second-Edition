# -*- coding: utf-8 -*-

"""
  Name     : c10_17_calendarSpread.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import p4f
import numpy as np
import matplotlib.pyplot as plt
sT = np.arange(20,70,5) 
s=40;x=40;T1=0.5;T2=1;sigma=0.3;r=0.05
payoff=(abs(sT-x)+sT-x)/2 
call_01=p4f.bs_call(s,x,T1,r,sigma)	# short 
call_02=p4f.bs_call(s,x,T2,r,sigma)	# long

profit_01=payoff-call_01 
call_03=p4f.bs_call(sT,x,(T2-T1),r,sigma) 
calendar_spread=call_03-payoff+call_01 -call_02 
y0=np.zeros(len(sT))
plt.ylim(-20,20) 
plt.xlim(20,60) 
plt.plot(sT,call_03,'b-.')
plt.plot(sT,call_02-call_01-payoff,'b-.') 
plt.plot(sT,calendar_spread,'r') 
plt.plot([x,x],[-20,-15])
plt.title("Calendar spread with calls") 
plt.xlabel('Stock price at maturity (sT)') 
plt.ylabel('Profit (loss)')
plt.annotate('Buy a call with T1	and sell a call with T2', xy=(25,16)) 
plt.annotate('where T1<T2', xy=(25,14))
plt.annotate('Calendar spread', xy=(25,-3), xytext=(22,-15), arrowprops=dict(facecolor='red',shrink=0.01),)
plt.annotate('Value of the call (T2) at maturity', xy=(45,7), xytext=(25,10),
arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('Proflit/loss with call 1 only', xy=(50,-10), xytext=(30,-10),
arrowprops=dict(facecolor='blue',shrink=0.01),) 
plt.show()