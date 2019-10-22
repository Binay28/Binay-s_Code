#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for i in range(n):
        ppos=grid[i].find('p')
        if(ppos!=-1):
            while(abs(((n-1)/2)-i)):
                if((n-1)/2>i):
                    print("UP")
                    i+=1
                elif((n-1)/2<i):
                    print("DOWN")
                    i-=1
            while(abs(((n-1)/2)-ppos)):
                if((n-1)/2>ppos):
                    print("LEFT")
                    ppos+=1
                elif((n-1)/2<ppos):
                    print("RIGHT")
                    ppos-=1
            break
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
