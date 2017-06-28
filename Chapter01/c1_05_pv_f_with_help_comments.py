# -*- coding: utf-8 -*-
"""
  Name     : c1_05_pv_f_with_help_comments.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def pv_f(fv,r,n):
    """Objective: estimate present value
              fv: fture value
              r : discount period rate
              n : number of periods
        formula : fv/(1+r)**n      
           e.g.,
           >>>pv_f(100,0.1,1)
           90.9090909090909
           >>>pv_f(r=0.1,fv=100,n=1)
           90.9090909090909
           >>>pv_f(n=1,fv=100,r=0.1)
           90.9090909090909
    """
    return fv/(1+r)**n