import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    #ls=list()
    #ls.append(n*b)
    #for i in range(n):
     #   ls.append((n-i-1)*a+i*b)
    #return sorted(ls)
    return sorted(set([a*i+b*(n-1-i) for i in range(n)]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
#my code is in the commented part of the stones function my logic was same as the non-commented part but my code was failing some test cases maybe due to the duplication of data when a and b were same. 
