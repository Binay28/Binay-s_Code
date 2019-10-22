from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(*product(A,B))
#product(A, B) returns the same as ((x,y) for x in A for y in B)
