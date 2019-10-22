import numpy
n,m=map(int,input().split())
numpy.set_printoptions(sign=" ")
#if(n==m):print(numpy.identity(n))
print(numpy.eye(n,m,k=0))
#code for printing the identity matrix the eye function can insert 1's in any diagonal upper or lower

