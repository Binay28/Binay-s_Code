import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    for i in range(1,len(prices)+1):
        if(sum(prices[:i])>k):return(i-1)
        elif(sum(prices[:i])==k):return(i)
    #prices.sort()
    #count = 0
    #for i in prices:
    #    if (i <= k):
    #        count += 1
    #        k -= i
    #    else:
    #        break
    #return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#this code was failing majority of test cases due to use of sorted function there is a difference between sorted(parameter) and array.sort() function
#the code in the commented part is not my  code.
