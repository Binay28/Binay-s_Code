import statistics
import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count=0
    for i in range(d,len(expenditure)):
        if(expenditure[i]>=2*statistics.median(expenditure[i-d:i])):count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 5/7 testcases. Test cases are numbered from 0 to n
