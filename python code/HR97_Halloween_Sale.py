import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count=0
    #tot=0
    if(s>p):
        while(p>m):
            #if(s>tot):
            if(s>0):
                #tot+=p
                s-=p
                p=p-d
                count+=1
            else:return count
        return(count+math.floor(s/m))
    #elif(s==p):return 1   
    else:return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
#in this code 1 test case is failing
