import numpy
m=list()
for i in range(int(input())):
    m.append(list(map(float,input().split())))
#print("{0:.1f}".format(numpy.linalg.det(m)))
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(m))
#linalg.inv and linalg.eig
#code for calulating the determinant of a matrix
