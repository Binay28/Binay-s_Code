# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
mset=set(map(int,input().split()))
n=int(input())
nset=set(map(int,input().split()))
#ls=list()
ms=mset.difference(nset)
ms.update(nset.difference(mset))
for i in sorted(ms):print(i)
#the set data-structure has many inbuilt functions such as
#add() - add one element at a time
#update() - it only works for iterable objects
#discard() and remove() - remove elemnt from the set but remove raises key error if element is not present in the set whereas discard does not
#union() and intersection() - same as in set theory in maths
#difference() - returns the values which a present in one set and not the other i.e, the uncommon elements
