import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    ls=list()
    for i in range(len(a)):
        try:
            pos=a.index(a[i],i+1,len(a))
            ls.append(pos-i)
        except:continue
    if len(ls)!=0:return min(ls)
    else:return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
#first the code was failing 1 test case due to the end index for the array a=[1,1] upon changing the end index from len(a)-1 to len(a) the code passed all the test cases.
