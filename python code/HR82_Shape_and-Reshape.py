import numpy
arr=numpy.array([input().split()],int)
arr.shape=(3,3)
print(arr)
#print(numpy.reshape(arr,(3,3)))
#shape resizes the original array whereas reshape returns a copy of the resized original array and leaves the original array unaltered
