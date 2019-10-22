from itertools import combinations_with_replacement
S,n=input().split()
for i in (combinations_with_replacement(sorted(S),int(n))):
    print(''.join(i))
#code for the use of combinations_with_replacements
