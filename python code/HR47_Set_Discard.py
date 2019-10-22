n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    cmd=input().split()
    if(len(cmd)==2):
        if(cmd[0]=="remove"):s.remove(int(cmd[1]))
        elif (cmd[0]=="discard"):s.discard(int(cmd[1]))
    elif(len(cmd)==1):s.pop()
print(sum(s))
#code for the use of pop(),remove() and discard() functions
