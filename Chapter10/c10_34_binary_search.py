
"""
  Name     : c10_34_binary_search.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def binary_search(x, target, my_min=1, my_max=None):
    if my_max is None:
       my_max = len(x) - 1
    while my_min <= my_max:
      mid = (my_min + my_max)//2
      midval = x[mid]
      if midval < target:
          my_min = my_mid + 1
      elif midval > target:
          my_max = mid - 1
      else:
          return mid
    raise ValueError

