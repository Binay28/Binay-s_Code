if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ls=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k!=n):
                    ls.append([i,j,k])
    print (ls)
#print the list of 3D co-ordinates whose sum is not n and are less than x,y,z 
