import statistics as s
n=int(input())
X=list(map(int,input().split()))
X.sort()
if(n%4==0 and n>=12):
    q1=s.median(X[0:4])
    q2=s.median(X[4:8])
    q3=s.median(X[8:])
else:
    q1=s.median(X[0:int(n/2)])
    q2=s.median(X)
    q3=s.median(X[-int(n/2):])
print(int(q1))
print(int(q2))
print(int(q3))
#this code is failing one test case
