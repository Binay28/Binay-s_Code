import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    ls=list()
    for i in range(len(arr)):
        s=0
        if(arr[i]>=0):
            for j in range(i+2,len(arr)):
                if(arr[j]>=0):s+=arr[j];j+=1
        ls.append(arr[i]+s)
    return max(ls)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
#this code is failing 1 sample test case because i have not considered some cases.
#the change in the for loop will probably solve the problem

