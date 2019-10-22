# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
for i in range(int(input())):
    q=input().split()
    #if(len(q)==1):
     #   d.q()
    #if(len(q)==2):
     #  d.q[0](q[1]) 
#print(d)
    getattr(d, q[0])(*[q[1]] if len(q) > 1 else [])
print(*[item for item in d])
#here the getattr function is not mine but its use was clever
