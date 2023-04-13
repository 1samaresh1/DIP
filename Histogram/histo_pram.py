import numpy as np
import matplotlib.pyplot as plt
p=open("Histogram/lena.pgm",'r')
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


q=open("Histogram/out.pgm",'w')
q1=q.write(p1)
q2=q.write(p2)
q3=q.write(p3)
q4=q.write(p4)

a=[0]*256
b=[0]*256

for i  in range(row):
    for j in range(col):
        x=k[i,j]
        a[x]=a[x]+1

for i in range(256):
    b[i]=i
    
     
plt.bar(b, a,width = 0.2, color = ['red', 'green'])       
plt.xlabel('r---->')
plt.ylabel('s---->')
plt.title('My bar chart!')
plt.show()

    
q.close()

