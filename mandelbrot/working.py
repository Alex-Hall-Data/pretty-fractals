#import numpy
import matplotlib.pyplot as plt
import numpy as np

size=1000
iterations=20
startgrid=[]
grid=[]
gridx=[0]*size**2
gridylist=[0]*size
gridy=[0]*size**2
result=[iterations]*(size**2)
row=[0]*size

    
#populate the result grid with coordinate positions
#x coordinates
for n in range (0, size):
    row[n]=n/(size/2)-2*((size-n)/size)    

gridx=row*size

#y coordinates
for n in range(0,size):
    gridylist[n]=[-1*(n/(size/2)-2*((size-n)/size))]*size

gridy=[val for sublist in gridylist for val in sublist]

#populate grid coordinates
for p in range(0,(size**2)-1):
    grid==grid.append([gridx[p],gridy[p]])
    startgrid==startgrid.append([gridx[p],gridy[p]])
    #print(grid[p])



g=0 #grid position counter
#generate points. do each pixel in turn
for e in grid:
    
    for i in range(1,iterations):

        c=((e[0]**2)+(e[1]**2))**(0.5)
        
        #update element values for next iteration
        e[0]=((e[0]**2)-(e[1]**2))+(startgrid[g][0])
        e[1]=(2*e[0]*e[1])+(startgrid[g][1])
        
        
        if (c>2):
            result[g]=i
            break

        
    g+=1 #increase outer loop counter by 1


#reshape as array    
result=np.array(result)
result=np.reshape(result,(size,size))

plt.clf()
plt.imshow(result)
plt.show()
