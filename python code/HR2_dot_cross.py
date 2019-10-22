#to calculate the matrix product of two matrices
import numpy
n=int(input())
a=numpy.matrix([list(map(int,input().split())) for i in range(n)])
b=numpy.matrix([list(map(int,input().split())) for i in range(n)])
print(a*b)
#import numpy
#n = int(input())
#arrays = [list(map(int,input().split())) for _ in range(n*2)]
#print(numpy.matmul(arrays[:n],arrays[n:]))
#import numpy
#numpy.set_printoptions(legacy='1.13')
#n = int(input())
#a = numpy.array([input().split() for i in range(n)]).astype(int)
#b = numpy.array([input().split() for i in range(n)]).astype(int)
#print(a@b)
