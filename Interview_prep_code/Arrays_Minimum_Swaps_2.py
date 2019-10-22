import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    for i in range(len(arr)):
      if(arr[i]!=i+1):  
        s=arr[arr.index(min(arr[i:]))]
        arr[arr.index(min(arr[i:]))]=arr[i]
        arr[i]=s
        count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
#this code is failing 5/14 test cases due to timeout.
