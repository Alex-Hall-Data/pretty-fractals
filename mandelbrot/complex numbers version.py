#import numpy
import matplotlib.pyplot as plt
import numpy as np


size=1000
iterations=20
result=[iterations]*(size**2)

for row in range(0,size):
    imagz=(row-size/2)*(4/size)
    for col in range(0,size):
        realz=(col-size/2)*(4/size)-0.5 #last term centers the image - use -0.5
        c=complex(realz,imagz)
        z=0
        i=1
        for i in range (1,iterations): 
           # c=abs(z)
            z=(z**2)+c
            i+=1
            
            if abs(z)>=2:
                result[(row*size)+col]=i
                break
                print(abs(z))
#reshape as array    
result=np.array(result)
result=np.reshape(result,(size,size))

plt.clf()
#figure size - 80dpi assumed
plt.figure(figsize=(size/80,size/80))
plt.imshow(result)
#plt.savefig("mandelbrotplot.png")
plt.show()

        