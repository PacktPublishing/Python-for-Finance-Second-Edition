# -*- coding: utf-8 -*-
"""
  Name     : c1_04_def_pv_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def pv_f(pv,r,n):
    return pv/(1+r)**n
#
pv=pv_f(100,0.1,2)
print(pv)