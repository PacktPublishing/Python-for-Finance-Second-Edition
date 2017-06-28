# -*- coding: utf-8 -*-
"""
  Name     : c1_08_NPV_Excel.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def npv_Excel(rate, cashflows):
     total = 0.0
     for i, cashflow in enumerate(cashflows):
         total += cashflow / (1 + rate)**(i+1)
     return total