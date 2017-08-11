# -*- coding: utf-8 -*-
"""
  Name     : c10_43_EW_port.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np

ret_A=np.array([0.102,-0.02, 0.213,0.12,0.13])
ret_B=np.array([0.1062,0.23, 0.045,0.234,0.113])

port_EW=(ret_A+ret_B)/2

round(np.mean(ret_A),3),round(np.mean(ret_B),3),round(np.mean(port_EW),3) 

round(np.std(ret_A),3),round(np.std(ret_B),3),round(np.std(port_EW),3) 
