import numpy
arr=list(map(float,input().split()))
numpy.set_printoptions(sign=' ')
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
#note the numpy.set_printoptions(sign(=' ')) in this code used to print the values with spaces between them

