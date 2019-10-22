import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    #dic=dict()
    ls=list()
    #for i in range(len(a)):
     #   dic[a[i]]=dic.get(a[i],i)
    #for i in range(k):
     #   for j in dic.keys():
      #      dic[j]=(dic.get(j,0)+1)%len(a)
    #for i in queries:
     #   for j in dic.keys():
      #      if(i==dic[j]):ls.append(j)
    while(k):
        j=a[len(a)-1]
        for i in range(len(a)-1):
            
    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#code is terminating due to timeout for maximum cases.
