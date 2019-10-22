# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n,m=map(int,input().split())
for i in range(1,n+1):
    if(i<=math.floor(n/2)):
        #for j in range(m):
        print ((".|."*(i-1)).rjust((m-(i-1)*n)/2,"-")+".|."+(".|."*(i-1)).ljust((m-(i-1)*n)/2,"-"))
    elif(i==(math.floor(n/2)+1)):
        print("WELCOME".center(m,"-"))
    elif(i>math.floor(n/2)+1):
        #for j in range(m):
        print ((".|."*(n-i)).rjust(m-1,"-")+".|."+(".|."*(n-i)).ljust(m-1,"-"))

#n, m = map(int,input().split())
#pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
#print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
