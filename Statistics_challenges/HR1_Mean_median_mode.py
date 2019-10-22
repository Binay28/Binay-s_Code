# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy import stats
import numpy as np
n=int(input())
ar=list(map(int,input().split()))
#print(np.mean(ar))
#print(np.median(ar))
print("{0:.1f}".format(np.mean(ar)))
print("{0:.1f}".format(np.median(ar)))
print(int(stats.mode(ar)[0]))

