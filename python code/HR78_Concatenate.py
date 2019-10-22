import numpy
A=list()
B=list()
n,m,p=map(int,input().split())
for i in range(n): A.append(list(map(int,input().split())))
for i in range(m): B.append(list(map(int,input().split())))
print(numpy.concatenate((A,B),axis=0))
#code for concatenating arrays
