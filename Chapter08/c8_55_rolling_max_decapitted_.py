import pandas as pd
import scipy as sp
x=sp.arange(1,1000)

y=pd.rolling_max(x,5)
