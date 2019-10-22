import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    ls=list()
    ls.append(grid[0])
    ls.append(grid[len(grid)-1])
    for i in range(1,len(grid)-1):
        f=0
        for j in range(1,len(grid)-1):
           #if(int(grid[i][j])>int(grid[i-1][j]) and int(grid[i][j])int(grid[i][j])
           if(int(grid[i][j])==max(int(grid[i][k]) for k in range(j-1,j+2)) and int(grid[i][j]==max(int(grid[k][j]) for k in range(i-1,i+2)))):
               ls.append(grid[i].replace(grid[i][j],"X"));f=1
        if(f!=1):ls.append(grid[i])
    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
#this code is failing due to not replacing the value with X