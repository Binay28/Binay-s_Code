import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    ls=list()
    for i in range(p,q):
       r=str(int(pow(i,2)))[-len(str(i)):]
       l=str(int(pow(i,2)))[:-len(str(i))]#len(str(int(pow(i,2))))-len(str(i))+1]
       r.strip();l.strip()
       if(int(r)+int(l)==i):
           ls.append(i)
    #print(ls)
    if(len(ls)==0):print("INVALID RANGE")
    else: print(" ".join(i for i in map(str,ls)))
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
#this code is failing some test cases due to white spaces which can't be converted into string. literal conversion error to string base 10: ' '
