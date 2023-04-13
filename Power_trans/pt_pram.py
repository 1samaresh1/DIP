import numpy as np
import math
p=open("Power_trans/mapping.pgm",'r')
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

q=open("Power_trans/output.pgm",'w')
c=1
Y=0.98765
e=0.01
q.write(p1)
q.write(p2)
q.write(p3)
q.write(p4)




for i in range(row):
    for j in range(col):
        q.write(f"{round(c*math.pow(k[i,j]+e,Y))}\n")
q.close()
