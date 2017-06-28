"""
  Name     : c6_07_input_Excel.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import pandas as pd
infile=pd.ExcelFile("c:/temp/Book1.xlsx")
x=infile.parse('Sheet1',header=None)
print(x)
