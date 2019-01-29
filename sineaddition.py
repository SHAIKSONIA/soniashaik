import numpy as np
import matplotlib.pyplot as boy

f1=float(input("enter the first frequency"))
f2=float(input("enter the second frequency"))
fs=float(input("enter the sampling frequency"))


x1=np.arange(0,10,0.25)
y1=np.sin(2*np.pi*x1*f1/fs)
x2=np.arange(0,10,0.25)
y2=np.sin(2*np.pi*x2*f2/fs)

x3=x1+x2
y3=y1+y2


boy.subplot(3,1,1)
boy.plot(x1,y1)
boy.xlabel("time")
boy.ylabel("amplitude")
boy.title('first wave')

boy.subplot(3,1,2)
boy.plot(x2,y2)
boy.xlabel("time")
boy.ylabel("amplitude")
boy.title('second wave')
  
boy.subplot(3,1,3)
boy.plot(x3,y3)
boy.xlabel("time")
boy.ylabel("amplitude")
boy.title('resultant wave')
boy.show( )