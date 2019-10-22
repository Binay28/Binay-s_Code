from itertools import groupby
S=input()
#print(*groupby(S))
for k, g in groupby(S):
    print((len(list(g)),int(k)),end=" ")
#counts the no. of occurences of each element of a string
