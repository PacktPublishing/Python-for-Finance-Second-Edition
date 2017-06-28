# -*- coding: utf-8 -*-
"""
  Name     : c6_24_bible.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from string import maketrans 
import pandas as pd 
word_freq = {}
infile="c:/temp/AV1611.txt"
word_list = open(infile, "r").read().split() 
ttt='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~0123456789'
for word in word_list:
    word = word.translate(maketrans("",""),ttt )
    if word.startswith('-'): 
        word = word.replace('-','')
    if len(word): 
        word_freq[word] = word_freq.get(word, 0) + 1 
keys = sorted(word_freq.keys())
x=pd.DataFrame(keys) 
x.to_pickle('c:/temp/uniqueWords.pkl')


