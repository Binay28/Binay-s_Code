import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    n=len(container)
    for i in range(n):
        csum=0
        for j in range(n):
            if(i!=j):csum+=container[j][i]
        if(sum(container[i])-container[i][i]==csum):continue
        else: return "Impossible"     
    return "Possible"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
#this code is failing 5/7 test cases but my logic is similar to one of the solutions
#my logic is that the total number of foreign balls in a container should be equal to the total no. balls of the container type outside the container.For example if container 0 3 foreign balls then there should be 3 0 type balls outside the container 0. 
