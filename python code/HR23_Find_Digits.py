import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    i=n
    c=0
    while(i!=0):
        q=i%10
        i=int(i/10)
        if(q==0):continue
        elif(n%q==0):c+=1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
#note that int() is used with the / operator
