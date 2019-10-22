import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
   count=0
   #sorted(arr)
   #arr.sort()
  #for i,j,k in zip(range(len(arr)),range(i+1,len(arr)),range(i+2,len(arr))):
   for i in arr:
       j=arr.count(r*i)
       k=arr.count(pow(r,2)*i)
       count+=j*k
   return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
#this code is failing 9/13 test cases 1 due to wrong answer and rest due to timeout.
