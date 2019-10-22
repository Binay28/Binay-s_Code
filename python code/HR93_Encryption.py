import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    S="".join(map(str,s.split()))
    ls=list()
    row=math.floor(math.sqrt(len(S)))
    col=math.ceil(math.sqrt(len(S)))
    if(row*col<len(S)):row=math.ceil(len(S)/col)
    for i in range(row):
        ls.append(S[i*col:col*(i+1)])
    #for i in range(col):
    if(len(ls[row-1])!=col):ls[row-1]=ls[row-1].rjust(col-len(ls[row-1])," ")
    return(" ".join("".join(j[i] for j in ls) for i in range(col)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
#used the rjust function to add whitespaces but it is not working still
#s = input().strip()
#c = ceil(sqrt(len(s)))
#print(' '.join(map(lambda x: s[x::c], range(c))))

