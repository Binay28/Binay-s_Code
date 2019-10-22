import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    ls=list()
    #while(1):
       # mini=min(arr)
       #if len(arr)==0: return ls 
       # else: ls.append(len(arr))
       # for i in range(len(arr)): 
       #     if(arr[i]==mini):arr.pop(i)
       #     else:arr[i]-=mini
    ls.append(len(arr))
    while True:                 
        arr = [x for x in arr if x != min(arr)] 
        if len(arr)==0:
            break
        ls.append(len(arr))
    return ls

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#this is not my logic my logic is in the commented part
