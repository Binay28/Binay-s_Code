import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    #arr1=set(s1.split())
    #arr2=set(s2.split())
    l=0
    #arr1=s1;arr2=s2
    #if(len(s1)>len(s2)):
    #k1=set(s1)
    #k2=set(s2)
    #print(k1)
    #print(k2)
    for i in set(s1):
        if(i in set(s2)): l+=min(s1.count(i),s2.count(i))#;print(1)
    #print(s1)
    #print(s2)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 11/15 test cases.
