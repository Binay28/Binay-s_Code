from itertools import permutations
S,n=input().split()
#print(sort(list(*permutations(S,int(n)))))
for i in sorted(permutations(S,int(n))):
    print(''.join(i))
#use of permutations function
