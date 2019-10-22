import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    (count,last)=(1,1)
    #count=1
    #last=1
    for i in range(1,n):
        if(arr[i-1]<arr[i] and i!=0):
            last+=1;count+=last
        elif(arr[i-1]>arr[i] and i!=0):
            last-=1;count+=last
        #else: last=1;count=1
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 2/3 test cases need to check.
