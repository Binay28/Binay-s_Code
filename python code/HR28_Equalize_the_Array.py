import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    dic=dict()
    for i in arr:
        dic[i]=dic.get(i,0)+1
    #maximum=max(dic.items(),key=lambda x:x[1])
    maximum=max(dic.values())
    return len(arr)-maximum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#In this code we calulate the minimum number of elements to be deleted so that the array is left with similar elements.Learnt to find the max element in a dictionary
