# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(input().split())
result=True
for i in range(int(input())):
    B=set(input().split())
    if not A.issuperset(B):result=False
print(result)
#code to check whether A is a strict superset of all the given sets or not
