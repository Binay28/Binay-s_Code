# Enter your code here. Read input from STDIN. Print output to STDOUT
#Els=list()
#Fls=list()
#Nls=list()
#for i in range(int(input())):Els=set(map(int,input().split()))
#for i in range(int(input())):Fls.append(set(map(int,input().split())))
#Nls=Els.union(Fls)
#print(len(Nls))
n=int(input())
Eng=set(map(int,input().split()))
m=int(input())
Fnc=set(map(int,input().split()))
print(len(Eng.union(Fnc)))
#code to explain the use of union() function in sets
