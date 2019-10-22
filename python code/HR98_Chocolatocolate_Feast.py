import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    count=n//c
    r=count
    while(r//m!=0):
        count+=r//m
        r=r//m+r%m
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
#this code can be shorter
#for _ in range(int(input())):
#    n,c,m=map(int,input().split())
#    print(n//c+(n//c-1)//(m-1))

