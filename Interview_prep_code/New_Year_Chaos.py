import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    #count=0
    #f=0
    #for i in range(len(q)):
    #    if(q[i]!=i+1):
    #        if(i-q.index(i+1)<=2):
    #            count+=abs(q.index(i+1)-i)
    #        else: print("Too chaotic");f=1;break
    #if(f==0):print(count//2)
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
#this is not my logic my logic is in the commented part and has an error for multiple displacements.
