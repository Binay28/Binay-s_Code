import numpy
n,m=map(int,input().split())
for i in range(n): A=numpy.array(list(map(int,input().split())))
for i in range(n): B=numpy.array(list(map(int,input().split())))
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
#print(*map(int,numpy.divide(A,B)))
#print(numpy.divide(A,B))
print("[".rstrip(),A//B,"]".lstrip())
print(numpy.mod(A,B))
print(numpy.power(A,B))
#this code is not working properly because of the divide statement result output result
