# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
Eng=set(map(int,input().split()))
m=int(input())
Fnc=set(map(int,input().split()))
print(len(Eng.difference(Fnc)))
#code to explain the use of difference() function
