"""
  Name     : c6_01_save_binary_file.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import array 
import numpy as np 
outfile = "c:/temp/tmp.bin" 
fileobj = open(outfile, mode='wb') 
outvalues = array.array('f') 
data=np.array([1,2,3]) 
outvalues.fromlist(data.tolist()) 
outvalues.tofile(fileobj) 
fileobj.close()
