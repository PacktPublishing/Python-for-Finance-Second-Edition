# -*- coding: utf-8 -*-
"""
  Name     : c7_16_def_sharpe_ratio.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def sharpeRatio(ticker,begdate=(2012,1,1),enddate=(2016,12,31)):
    """Objective: estimate Sharpe ratio for stock
        ticker  : stock symbol 
        begdate : beginning date
        enddate : ending date
        
       Example #1: sharpeRatio("ibm")
                     0.0068655583807256159
        
       Example #2: date1=(1990,1,1)
                   date2=(2015,12,23)
                   sharpeRatio("ibm",date1,date2)
                     0.027831010497755326
    """
    import scipy as sp
    from matplotlib.finance import quotes_historical_yahoo_ochl as getData
    p = getData(ticker,begdate, enddate,asobject=True,adjusted=True)
    ret=p.aclose[1:]/p.aclose[:-1]-1
    return sp.mean(ret)/sp.std(ret)
