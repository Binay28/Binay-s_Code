for i in range(int(input())):
    nA=int(input())
    A=set(map(int,input().split()))
    nB=int(input())
    B=set(map(int,input().split()))
    if A.issubset(B): print(True)
    else : print(False)
#code to check  whether A is a subset of B
