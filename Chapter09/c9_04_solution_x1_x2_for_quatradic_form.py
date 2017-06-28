"""
  Name     : c9_04_solution_x1_x2_for_quatradic_form.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import scipy as sp
a=1
b=6
c=3

inside=b**2-4*a*c

if inside>0:
    squared=sp.sqrt(inside)
    print("x1=",(b+squared)/(2*a))
    print("x2=",(b-squared)/(2*a))


    
 