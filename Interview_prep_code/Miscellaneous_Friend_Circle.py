import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    ls=list()
    a=set()
    for i in queries:#range(len(queries)):
        if(j in i for j in a):
            ls.append(len(set(i).union(a)))
        else:ls.append(len(set(i)))
        a.add(j for j in i)
    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
#this code is failing 2/3 sample test cases because it is appending incremented values in the list
