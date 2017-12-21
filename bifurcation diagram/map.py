import matplotlib

#starting value of x is 0.5 in this case
#recursive function for logistic map. i=number of iterations
def logistic(r,i):
    if i==2:
        return r*0.5*(1-0.5)
    else:
        return r*logistic(r,i-1)*(1-logistic(r,i-1))
    
