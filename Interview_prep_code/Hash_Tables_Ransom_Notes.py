#from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #nls=note.split()
    #mls=magazine.split()
    f=0
    for i in note:
        if i not in magazine:f=1;break
        else: magazine.pop(magazine.index(i))
    if(f==0): print("Yes") 
    else:print("No")
    #dic=defaultdict(int)
    #for i in note:
    #    dic[i]+=1
    #for i in magazine:
    #    if(dic[i]==0): print("No");f=1
    #    else: dic[i]-=1
    #if(f==0):print("Yes")
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
#this logic is getting timed out for two test cases
#the code in the commented part is not mine it is a external code the code in the non-commented part is mine
