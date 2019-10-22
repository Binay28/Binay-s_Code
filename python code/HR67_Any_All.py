# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
#ls=list(map(int,input().split()))
#print(True if all(ls>0)and any(str(ls)=="")
#print all([i>0 for i in ls] and any(str(ls)=="".join(reversed(str(ls)))))
#print all([all(ls>0)] and any(str(ls)=="".join(reversed(str(ls)))))
ls=list(input().split())
print (all([int(i)>0 for i in ls]) and any([j == j[::-1] for j in ls]))
#have to debub my code in #tag the code without #tag is not mine
