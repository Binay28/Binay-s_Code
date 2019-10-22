import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    ls=list()
    for i in list(set(range(n)).difference(c)):
        ls.append(min(abs(j-i) for j in c))
    if len(ls)==0:return 0
    else:return(max(ls))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing two test cases
#compiler message:Terminated due to timeout
