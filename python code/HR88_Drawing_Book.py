import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    #fcount=0
    #bcount=1
    #if(n%2==0):
        #if(n!=p):
            #t1=(0,1)
           # t2=(n-2,n-1)
           # while(p not in t1): 
          #      fcount+=1
         #       t1+=1
        #    while(p not in t2):
       #         bcount+=1
      #          t2-=1  
     #   else: return 0
    #else:
        #if(n!=p and n-1!=p): 
            #t1=(0,1)
            #t2=(n-2,n-1)
           # while(p not in t1): 
          #      fcount+=1
         #       t1+=(1,1)
        #    while(p not in t2):
       #         bcount+=1
      #          t2-=1 
     #   else: return 0     
    #return (fcount if fcount<bcount else bcount)
    return min(p//2,n//2-p//2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
#this logic was not mine but i was trying to do the same previously
