from itertools import combinations
S,n=input().split()
for k in range(1,int(n)+1):
    for i in (combinations(sorted(S),int(k))): print(''.join(i))
#code for the use of combinations function.
