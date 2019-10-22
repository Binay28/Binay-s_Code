import numpy
arr=list()
n,m=map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
print(numpy.max(numpy.min(arr,axis=1)))
#code for use of max and min from numpy library



