import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count=0
    for i in range(n):
        for j in range(n+1):
            if(len(set(s[i:j].split()))==2 and (j-i+1)%2!=0):
                count+=1
            elif(len(set(s[i:j].split()))==1):count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is incomplete need to add some more conditions under the first if statement.
