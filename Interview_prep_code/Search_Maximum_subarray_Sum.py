import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def maximumSum(a, m):
    max=0
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            if(sum(a[i:j])%m>max):max=sum(a[i:j])%m
    return max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 15/19 test cases due to timeout.
