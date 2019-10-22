import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    # solve here
    ls=list()
    for i in queries:
        maximum=0
        for j in arr:
            if(i^j>maximum):maximum=i^j
        ls.append(maximum)
    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#this code is failing 10/15 testcases due to timeout
