# -*- coding: utf-8 -*-
"""
  Name     : c10_28_standard_normal_dist.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from scipy import exp,sqrt,stats,arange
#
x = arange(-3,3,0.1)
y=stats.norm.pdf(x)
plot(x,y)
