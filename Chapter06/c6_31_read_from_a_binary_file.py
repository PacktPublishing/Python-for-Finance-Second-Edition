"""
  Name     : c6_31_read_from_a_binary_file.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import array 
infile=open("c:/temp/tmp.bin", "rb") 
s=infile.read()       # read all bytes into a string 
d=array.array("f", s) # "f" for float 
print(d)  
infile.close()
