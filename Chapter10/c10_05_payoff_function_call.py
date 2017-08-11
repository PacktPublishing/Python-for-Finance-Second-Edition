"""
  Name     : c10_05_payoff_function_call.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def payoff_call(sT,x):
    return (sT-x+abs(sT-x))/2
