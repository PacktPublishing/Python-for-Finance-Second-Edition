# -*- coding: utf-8 -*-
"""
  Name     : c4_14_download_one_jpg_image.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import urllib
f = open('c:/temp/00000001.jpg','wb')
f.write(urllib.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read())
f.close()





