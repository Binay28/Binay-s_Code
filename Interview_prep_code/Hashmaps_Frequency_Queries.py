import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    arr=list()
    ls=list()
    for i in queries:
        f=0
        if(i[0]==1):arr.append(i[1])
        elif(i[0]==2):
            try:arr.pop(arr.index(i[1]))
            except:break
        elif(i[0]==3):#ls.append(1 if any arr.count(j for j in arr)==i[1] else 0)
            for j in set(arr):
                if(arr.count(j)==i[1]):ls.append(1);f=1;break
            if(f==0):ls.append(0)
    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
#this code is failing 1/3 test cases in the sample test case and 13/15 test cases in the actual test cases.
