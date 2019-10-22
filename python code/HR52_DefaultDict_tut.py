# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
A=defaultdict(list)
#B=defaultdict()
C=defaultdict(list)
n=list(map(int,input().split()))
for i in range(n[0]):A[input()].append(i+1)
#for i in range(n[1]):B[i].append(input())
#print(A)
for i in range(n[1]):
    word=input()
    #for j in range(n[0]):
        #if(word==A[j]):C[word].append(j+1)
    #if not C[word]:C[word].append(-1)
    for j in A.keys():
        if(word==j):print(" ".join(map(str,A[j])))
    if not A[word]: print("-1")
#for i in C.keys():
 #   print(" ".join(map(str,C[i])))
#for i in range(n[0]):A[i].append(input())
#the indexing on basis of integers was giving error and would take more space
