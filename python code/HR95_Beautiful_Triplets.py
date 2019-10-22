import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    count=0
    for i in range(len(arr)):
        #for j in range(i+1,len(arr)):
         #   for k in  range(j+1,len(arr)):
         #       if(arr[j]-arr[i]==d and arr[k]-arr[j]==d):count+=1(
        try:
            j=arr.index(arr[i]+d)
            try:
                if(arr.index(arr[j]+d)):count+=1
            except:continue
        except:continue
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#the nested loop was taking more time and thus was failing due to timeout
#the try and except with index function speeded up the computation
