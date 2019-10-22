# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
Eng=set(map(int,input().split()))
m=int(input())
Fnc=set(map(int,input().split()))
#print(len(Eng.symmetric_difference(Fnc)))
print(len(Eng^Fnc))
#both the print statements give the same result

