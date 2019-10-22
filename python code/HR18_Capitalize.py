import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #ls=s.split()
    return " ".join(i.capitalize() for i in s.split(" "))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
#program to capitalize the first letter of name but why is the space parameter neede in the split function
