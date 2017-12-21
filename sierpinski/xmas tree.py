# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint as randint
import random
from matplotlib import pyplot
from pylab import rcParams

iterations=10000
offset=200

#scale down to stop points being too spread out
size=iterations/10

#vertices
v1=[0,0]
v2=[size/2,((size**2)-(size/2)**2)**0.5]
v3=[size,0]


point=[size/2,size/2]



vertex=[]
pointsx=[]
pointsy=[]
pointssquarex=[]
pointssquarey=[]

for i in range(1,iterations):
  
  #pick a random vertex
  rand = randint(1,3)
  if (rand==1):
      vertex=v1;
  if (rand==2):
      vertex=v2;
  if (rand==3):
      vertex=v3;
  

  #go half way to vertex
  point=[(vertex[0]+point[0])/2,((vertex[1]+point[1])/2)+offset/2]
  pointsx.append(point[0])
  pointsy.append(point[1])
  
  pointssquarex.append(random.uniform(size/2-offset/5,size/2+offset/5))
  pointssquarey.append(random.uniform(0,offset))
  
   
  i=i+1
  

  
rcParams['figure.figsize'] = 10, 14
pyplot.scatter(pointsx,pointsy,color="green",s=2)
pyplot.scatter(pointssquarex,pointssquarey,color="red",s=1)
pyplot.title("Have a fractal-tastic Christmas! \n",fontname="Franklin Gothic Medium",fontsize=20)
pyplot.savefig('awful_card.png')


