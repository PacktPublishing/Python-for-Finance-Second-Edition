import scipy as sp

var1=0.016
var2=0.027

sigma1=sp.sqrt(var1)
sigma2=sp.sqrt(var2)
rho=-1
n=1000
portVar=10   # assign a big number
tiny=1.0/n

for i in sp.arange(n):
    w1=i*tiny
    w2=1-w1
    var=w1**2*var1 +w2**2*var2**2+2*w1*w2*rho*sigma1*sigma2
    if(var<portVar):
        portVar=var
        finalW1=w1
    #print(vol)
print("min vol=",sp.sqrt(portVar), "w1=",finalW1)