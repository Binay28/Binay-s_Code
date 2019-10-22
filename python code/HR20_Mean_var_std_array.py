import numpy
n,m=map(int,input().split())
#ls=list()
ls= numpy.array([input().split() for i in range(n)],float)
#for i in range(n): ls.append(map(int,input().split()))
numpy.set_printoptions(legacy='1.13')
print (numpy.mean(ls,axis=1))
print (numpy.var(ls,axis=0))
print (numpy.std(ls,axis=None))
#program to understand array its mean, var and std.
#syntax for array in python numpy.array(value list,data type)
