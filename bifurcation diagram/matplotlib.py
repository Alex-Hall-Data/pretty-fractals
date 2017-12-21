import math
#import numpy
import matplotlib

#number of iterations
iterations=20

#grid size
size=10

#initiate the grid with all values=iteration
grid=[[0,0] for b in range(0,size**2)]
gridy=[]
gridx=[]
gridex=[]

for x in range(0,size):
    gridx.append(x)
gridx=[gridx]*size
gridx  = [val for sublist in gridx for val in sublist]
for i in range(0,len(gridx)):
    gridx[i]=((4*gridx[i])/size)-2


#for y in range(0,size):
#    gridy.append([size-y]*size)
#gridy = [val for sublist in gridy for val in sublist]
#for i in gridy:
#    gridy[i]=((4*gridy[i])/size)-2


#gridy=((4*gridy)/size)-2

##list of grid elements (LIST - NEEDS TURNING TO MATRIX)
#for n in range(0,(size**2)-1):
#    grid[n][0]=gridx[n]

#for m in range(0,(size**2)-1):
#    grid[m][1]=gridy[m]

    

