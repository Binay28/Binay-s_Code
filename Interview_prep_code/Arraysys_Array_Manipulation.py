#import numpy
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #arr=numpy.zeros(n,dtype=int)
    arr=[0]*(n+1)
    for i in queries:
       for j in range(i[0],i[1]+1):arr[j]=arr[j]+i[2]
    return max(arr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 7/13 test cases.
