import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    ls=list()
    while(n!=0):
        ls.append(1 if n%2==0 else 0)
        n=n//2
    #''.join(map(str,ls)).rjust(32,'1')
   #sum(pow(2,i) for i in range(len(ls),32))
   #sum(ls[i]*pow(2,i) for i in range(len(ls)))
    return(sum(ls[i]*pow(2,i) for i in range(len(ls)))+sum(pow(2,i) for i in range(len(ls),32)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
#this is my code, probably my first code after hello world types to clear all the test cases in first attempt
