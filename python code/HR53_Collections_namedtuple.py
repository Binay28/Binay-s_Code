# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
#data=namedtuple('data',",".join(map(str,input().split())))
#data1=data(mark12,id=1,class=10,name='bhaisi')
categories=list(input().split())
ind=categories.index("MARKS")
sum=0
for i in range(n):
    sum+=int(list(input().split())[ind])
print(sum/n)
#though this code was for namedtuple introduction i have done it using my list logic
