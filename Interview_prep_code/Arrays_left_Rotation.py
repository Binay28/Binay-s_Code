import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    dic=dict()
    #ls=range(len(a))
    #for i in range(len(a)):
     #   if(i-d>=0):
      #      dic[a[i]]=i-d
      #  elif(i-d<0):
       #     dic[a[i]]= len(a)-(d-i) 
    #sorted(dic.values())
    #for i in range(len(a)): dic[a[i]]=(len(a)+i-d)%len(a)
    for i in range(len(a)): dic[(len(a)+i-d)%len(a)]=a[i]
    #for i in range(len(a)): print(dic[a[i]])
    return(dic[i] for i in range(len(a)))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#this code is for left rotation of array
