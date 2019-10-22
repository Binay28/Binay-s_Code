#In this code i have used the update method in dictionary to insert the values with keys 

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
     maximum=0
     tls=dict()
     for i in range(len(topic)):
         for j in range(i+1,len(topic)):
             count=0
             for k,l in zip(topic[i],topic[j]):
                 if(k=='1' or l=='1'):count+=1
             tls.update({str(i)+str(j):count})
     maximum=max(tls.values())
     count=0
     for i in tls.keys():
         if(tls[i]==maximum):count+=1
     return (maximum,count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#this program is for calculating the maximum no. of topics known to a two member team in ICPC and the maximum no. of teams which know this topic
