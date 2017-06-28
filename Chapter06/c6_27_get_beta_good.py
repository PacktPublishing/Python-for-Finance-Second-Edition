from scipy import stats 
from matplotlib.finance import quotes_historical_yahoo_ochl as aa 
#
def dailyReturn(ticker,begdate,enddate):
     p = aa(ticker, begdate,enddate,asobject=True,adjusted=True)
     return p.aclose[1:]/p.aclose[:-1]-1
#
begdate=(2012,1,1)
enddate=(2017,1,9)
retIBM=dailyReturn("wmt",begdate,enddate)
retMkt=dailyReturn("^GSPC",begdate,enddate)
outputs=stats.linregress(retMkt,retIBM) 
print(outputs)
