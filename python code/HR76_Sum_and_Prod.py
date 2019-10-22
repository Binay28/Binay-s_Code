import numpy
arr=list()
n,m=map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
print(numpy.prod(numpy.sum(arr,axis=0)))
#code for use of prod and sum from numpy library

