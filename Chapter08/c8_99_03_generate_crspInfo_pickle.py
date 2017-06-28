"""
 10000  7952 68391610 OPTIMUM MANUFACTURING INC       OMFGA  3 19860131-19870630
 10001  7953 36720410 GAS NATURAL INC                 EGAS   2 19860131-20151231
 10002  7954 05978R10 BANCTRUST FINANCIAL GROUP INC   BTFG   3 19860131-20130228
 10003  7957 39031810 GREAT COUNTRY BK ASONIA CT      GCBK   3 19860131-19951229

"""

import pandas as pd
infile="c:/temp/cheadfile.dat"
fwidths = [7,6,8,33,5,3,9,1,9]
df = pd.read_fwf(infile, widths=fwidths)
#print(df.head(2))

crspInfo=pd.DataFrame(df)

crspInfo.columns=['PERMNO','PERMCO','CUSIP','FIRMNAME','TICKER','EXCHANGE','BEGDATE','D','ENDDATE']

del crspInfo['D']


#crspInfo=pd.DataFrame(df,columns=['PERMNO','PERMCO','CUSIP','NAME','TICKER','EX','BEGDATE','D','ENDDATE'])
crspInfo.to_pickle("c:/temp/crspInfo.pkl")



