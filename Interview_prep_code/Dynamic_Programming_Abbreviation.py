import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    f=0
    if(set(b.lower()).issubset(set(a.lower()))):
        for i in set(a.lower()).difference(set(b.lower())):
            if(i.upper() in a):return("NO");f=1;break
        if(f==0):return("YES")
    else: return("NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
#this code is failing 10/16 test cases.
