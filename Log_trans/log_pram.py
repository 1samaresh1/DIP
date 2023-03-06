import numpy as np
import math
p=open("Log_trans/spectrum.pgm",'r')
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

q=open("Log_trans/output.pgm",'w')
q1=q.write(p1)
q2=q.write(p2)
q3=q.write(p3)
q4=q.write(p4)


c=25



for i in range(row):
    for j in range(col):
        q.write(f"{round(c*math.log2(k[i,j]+1))}\n")
       
q.close()
