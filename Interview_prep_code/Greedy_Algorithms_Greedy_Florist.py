import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if(len(c)>k):
        sorted(c,reverse=True)
        s=sum(c[:k])
        if((len(c)-k)>k):
            for i in range((len(c)-k)//k):
                s+=(i+2)*c[k+i]
        for j in range((len(c)-k)%k):
            s+=(((len(c)-k)//k)+2)*c[k+((len(c)-k)//k)+j]
    elif(len(c)==k):s=sum(c)
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
#this code is failing 2/3 sample test cases.
