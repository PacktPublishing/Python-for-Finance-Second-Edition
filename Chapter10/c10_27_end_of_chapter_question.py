# -*- coding: utf-8 -*-
"""
  Name     : c10_27_end_of_chapter_question.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import p4f 
import matplotlib.pyplot as plt 
plt.figtext(0.08,0.6,"Stock price=$20") 
plt.figtext(0.08,0.56,"call =7.43") 
plt.figtext(0.33,0.76,"Stock price=$67.49") 
plt.figtext(0.33,0.70,"Option price=0.93") 
plt.figtext(0.33,0.27,"Stock price=$37.40") 
plt.figtext(0.33,0.23,"Option price=14.96") 
plt.figtext(0.75,0.91,"Stock price=$91.11") 
plt.figtext(0.75,0.87,"Option price=0") 
plt.figtext(0.75,0.6,"Stock price=$50") 
plt.figtext(0.75,0.57,"Option price=2") 
plt.figtext(0.75,0.28,"Stock price=$27.44") 
plt.figtext(0.75,0.24,"Option price=24.56") 
n=2 
p4f.binomial_grid(n)
plt.show()
