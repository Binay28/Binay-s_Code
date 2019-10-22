if __name__ == '__main__':
    N = int(input())
    ls=list()
    for i in range(N):
        #name,pos,val=map(str,input().split(" "))
        s=input().split()
        #name,pos,val=s[0],s[1],s[2]
        if(len(s)==1):
            if(s[0]=="print"):print(ls)
            elif(s[0]=="sort"):ls.sort()
            elif(s[0]=="pop"):ls.pop()
            elif(s[0]=="reverse"):ls.reverse()
        elif(len(s)==2):
            if(s[0]=="remove"):ls.remove(int(s[1]))
            elif(s[0]=="append"):ls.append(int(s[1]))
        elif(len(s)==3):ls.insert(int(s[1]),int(s[2]))
#this code is basic usage of lists
