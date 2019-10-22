import numpy
#z=list()
#o=list()
n,m,*k=map(int,input().split())
#numpy.set_printoptions(sign=" ")
#print("\n".join(numpy.zeros((n,m),dtype=numpy.int)))
print(numpy.zeros((n,m,*k),dtype=numpy.int))
print(numpy.ones((n,m,*k),dtype=numpy.int))
#print(z)
#print(o)
#tuples are faster than list


