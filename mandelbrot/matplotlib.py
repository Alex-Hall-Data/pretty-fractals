import math
#import numpy
import matplotlib



#number of iterations
iterations=20

#grid size
size=10

#INITIATE A MAP GRID ALL OF VALUE ITERATIONS
result=[iterations]*(size**2)

#initiate the grid with all values=iteration
grid=[[0,0] for b in range(0,size**2)]
gridy=[]
gridx=[]

#generate list of x coordinates 
for x in range(0,size):
    gridx.append(x)
gridx=[gridx]*size
gridx  = [val for sublist in gridx for val in sublist]
for i in range(0,len(gridx)):
    gridx[i]=((4*gridx[i])/size)-2

#generate list of y coordinates
for y in range(0,size):
    gridy.append([size-y]*size)
gridy = [val for sublist in gridy for val in sublist]
for i in range (0,len(gridy)):
    gridy[i]=((4*gridy[i])/size)-2




#list of grid coordinates in the form[[x,y],[x,y]...]
for n in range(0,(size**2)-1):
    grid[n][0]=gridx[n]

for m in range(0,(size**2)-1):
    grid[m][1]=gridy[m]

g=0 #grid position counter
#generate points. do each pixel in turn
for e in grid:
    lc=1 #loop counter
    for i in range(1,iterations):
        x=(e[0]**2)-(e[1]**2)
        y=2*e[0]*e[1]
        c=(((x**2)+(y**2)))**0.5
        lc+=1
        if (c>2):
            result[g]=lc
            break

        #update element values for next iteration
        e[0]=x
        e[1]=y
    g+=1 #increase outer loop counter by 1
        

