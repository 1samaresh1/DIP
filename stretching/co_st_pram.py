import numpy as np
import math
p=open("stretching/image.pgm",'r')
p1=p.readline()
p2=p.readline()
p3=p.readline()
p4=p.readline()
col,row=[int(i) for i in p3.split()]
k=np.zeros((row,col),dtype=int)
for i in range(row):
    for j in range(col):
        k[i,j]=int(p.readline())

p.close()

q=open("stretching/output.pgm",'w')

q.write(p1)
q.write(p2)
q.write(p3)
q.write(p4)

a=110
b=170
for i in range(row):
    for j in range(col):
        if (k[i,j]< a):
            k[i,j]=k[i,j]
        elif((k[i,j]>=a)and(k[i,j]<b)):
            k[i,j]=245
        else:
             k[i,j]=k[i,j]

for i  in range(row):
    for j in range(col):
        q.write(f"{k[i,j]}\n") 

       
q.close()
