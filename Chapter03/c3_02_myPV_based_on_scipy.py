# -*- coding: utf-8 -*-
"""
  Name     : c3_02_myPV_based_on_scipy.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def myPV(r,n,fv):
    import scipy as sp
    return(-sp.pv(r,n,0,fv))
    
    
    
def myPV(r,n,fv):
    """
    Objective: estimate present value of one future cash flow
           r : period rate
           n : number of periods
          fv: fture value
           
    formula used : pv=fv/(1+r)**n      
               
    Example 1: >>>myPV(0.1,1,100)
                 90.9090909090909
    
    Example #2 >>>myPV(r=0.1,fv=100,n=1)
                 90.9090909090909
    """
    import scipy as sp
    return(-sp.pv(r,n,0,fv))