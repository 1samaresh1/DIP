import numpy as np
import random
p=open("Mean_filters/anim.pgm",'r')
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


q=open("Mean_filters/mfout.pgm",'w')
q1=q.write(p1)
q2=q.write(p2)
q3=q.write(p3)
q4=q.write(p4)

for i  in range(1,row-1):
    for j in range(1,col-1):
        k[i,j]= (k[i-1, j-1]+k[i-1, j]+k[i-1, j + 1]+k[i, j-1]+ k[i, j]+k[i, j + 1]+k[i + 1, j-1]+k[i + 1, j]+k[i + 1, j + 1])/9



for i  in range(row):
    for j in range(col):  
        q.write(f"{k[i,j]}\n")     
q.close()

