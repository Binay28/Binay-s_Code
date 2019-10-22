import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count=0#;ls=s.split()
    #for i in range(len(ls)):
    #    if(ls[i]==ls[i+1] and i!=len(ls)-1):ls.pop(i);count+=1
    for i in range(len(s)): #range(len(ls)):
        if(i!=len(s)-1):
            if(s[i]==s[i+1]):count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
#this can't be done with list as the it is a string of single word and not space separated words.
