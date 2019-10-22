# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
Eng=set(map(int,input().split()))
m=int(input())
Fnc=set(map(int,input().split()))
print(len(Eng.intersection(Fnc)))
#code to explain use of intersection() function
