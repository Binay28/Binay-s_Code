import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ls=list()
    #score=defaultdict()
    score=list((sorted(set(scores),reverse=True)))
    for i in alice:
        for j in range(len(score)):
            if(i>=score[j] and j==0):ls.append(1)
            elif(i<score[j] and j==len(score)-1):ls.append(len(score)+1)
            #elif(i<=score[j] and i>=score[j+1]):ls.append(j+2)
            elif(i<score[j] and i>=score[j+1]):ls.append(j+2)
    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#this code is terminating due to timeout on hackerrank for large number of inputs such as 2000 elements
