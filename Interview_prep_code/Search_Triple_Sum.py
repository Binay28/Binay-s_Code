import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    count=0
    for i in b:
        j=len([k for k in a if k<=i])
        l=len([k for k in c if k<=i])
        count+=j*l
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
#this code is failing 1/3 sample test cases due to wrong answer. 
