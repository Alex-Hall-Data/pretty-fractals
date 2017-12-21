
size=10
iterations=20

grid=[[0]*2]*(size**2)
gridx=[0]*size**2
gridylist=[0]*size
gridy=[0]*size**2
result=[iterations]*(size**2)
row=[0]*size


#list of grid coordinates in the form[[x,y],[x,y]...]
#for n in range(0,(size**2)-1):
 #   grid[n][0]=gridx[n]

#for m in range(0,(size**2)-1):
#    grid[m][1]=gridy[m]
    
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
    grid[p][0]=gridx[p]
for q in range(0,(size**2)-1):
    grid[q][1]=gridy[q]
