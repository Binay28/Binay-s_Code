import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):
    if(n==1 or n%2==0 and n!=2):return("Not prime")
    elif(n==2):return("Prime")
    for i in range(3,n,2):
        if(n%i==0):return("Not prime")
    return("Prime")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
#this code is failing 2/11 test cases due to timeout although i am only checking for division by odd numbers in the for loop
#previous code was failing two more test cases due to n being 1 for which i did not give any condition
