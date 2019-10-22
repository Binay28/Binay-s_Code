import numpy
n,m=map(int,input().split())
ls=numpy.array([input().split() for i in range(n)],int)
print(numpy.transpose(ls))
print(ls.flatten())
#code for transpose and flattening of a matrix


