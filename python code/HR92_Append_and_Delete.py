import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    #sls=s.split()
    #tls=t.split()
    count=0
    #while(k):
    if(len(s)==len(t)):
        for i in range(len(s)):
            if(s[i]!=t[i]):count=len(s)-i     
        if(k>=2*count): return("Yes")
        else:return("NO")
    elif(len(s)>len(t)):
        for i in range(len(t)):
            if(s[i]!=t[i]):count=len(t)-i;break
        if(k>=(2*count)+len(s)-len(t)):return("Yes")
        else:return("No")
    elif(len(t)>len(s)):
        for i in range(len(s)):
            if(s[i]!=t[i]):count=len(s)-i;break
        if(k>=(2*count)+len(s)-len(t)):return("Yes")
        else:return("No")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
#this code is failing 4/14 test cases on hackerrank
