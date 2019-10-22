# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x=map(int,input().split())
ls=list()
for i in range(x):
    ls.append(map(float,input().split()))
for i in zip(*ls):
    print(sum(i)/len(i))
#here *is used with ls in zip argument because map function returns the pointer to the base address of the list so to access its elements we need to dereference it.
