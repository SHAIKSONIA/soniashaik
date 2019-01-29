import numpy as np
import matplotlib.pyplot as sketch

f1=float(input("enter the frequency"))
fs=float(input("enter the sampling frequency"))
p=np.arange(0,10,0.1)
q=np.sin(2*np.pi*p*f1/fs)
sketch.plot(p,q)
sketch.xlabel('samples')
sketch.ylabel('voltage')
sketch.title('sine wave')
sketch.show( )