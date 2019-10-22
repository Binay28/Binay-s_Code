# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    nA=int(input())
    A=input()
    nB=int(input())
    B=input()
    lsA=A.split()
    lsB=B.split()
    Adic=dict()
    #for j in lsA:
     #   (x,y)=(int(j),0)
      #  for k in lsB:
       #     if(x==int(k))
        #        y+=1
        #if(y>0):Continue
        #else:print(False)
    for j in lsA:
        Adic[j]=Adic.get(j,0)+1
    for j in Adic.keys():
        for l in lsB:
            if(j==l):
                Adic[j]+=1
    for j in Adic.keys():
        if(int(Adic[j])==0):
            print(False)
            break
    
