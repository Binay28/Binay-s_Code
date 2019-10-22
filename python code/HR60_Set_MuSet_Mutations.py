# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
A=set(list(map(int,input().split())))
for i in range(int(input())):
    cmd=input().split()
    ls=set(map(int,input().split()))
    getattr(A,cmd[0])(ls)
print(sum(A))
#getattr is a useful function used to parse the attribute from a string
