import numpy as np
import pandas as pd
nn=np.nan
x=pd.Series([0.29,0.57,nn,1.34,nn,nn,nn,nn,2.7])
y=x.interpolate()
print(y)
