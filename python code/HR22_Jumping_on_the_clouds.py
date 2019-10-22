#n, k  = map(int, input().strip().split())
#clouds = list(map(int, input().strip().split()))
#print(100 - sum(1 + 2 * clouds[i] for i in range(0, n, k)))
#!/bin/python3
#the above commented code is not my code it was a posted solution my code is below
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i=k
    e=100
    while(i!=0):
        if(c[i]==0):
            e=e-1
            i=(i+k)%len(c)
        else:
            e=e-3
            i=(i+k)%len(c)
    if(c[0]==0):return(e-1)
    else: return(e-3)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
