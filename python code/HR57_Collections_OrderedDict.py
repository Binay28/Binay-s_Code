# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
dic=OrderedDict()
for i in range(int(input())):
    data=input().split()
    dic[" ".join(data[:-1])]=dic.get(" ".join(data[:-1]),0)+int(data[-1])
print(*[" ".join([i,str(dic[i])])for i in dic.keys()],sep='\n')
#ordered dictionary prints the dictionary in the order which the keys where inserted into it
