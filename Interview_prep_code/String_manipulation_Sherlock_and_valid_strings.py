import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    dic=dict()
    for i in s:
        dic[i]=dic.get(i,1)+1
    t=min(dic.values())
    ls=list(dic.values())
    #if(dic.values().count(t)==len(dic) or len(dic)-dic.values().count(t)==1 or dic.values().count(t)-len(dic)==len(dic)-1):return("Yes")
    #if(ls.count(t)==len(dic) or len(dic)-ls.count(t)==1 or ls.count(t)-len(dic)==len(dic)-1):return("YES")
    if(ls.count(t)==len(dic)):return("YES")
    elif(len(dic)-ls.count(t)==1):
        if(max(dic.values())-t==1):return("YES")
    elif(len(dic)-ls.count(t)==len(dic)-1):
        if(t==1):return("YES")
    else: return("NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()


#making a set of individual alphabets and checking whether the length of the string is completely divisible by it or not is not right it would lead to a wrong answer. Eg: aabbcccd len=8 set length=4
#i have checked whether all the minimum value occurs in all the keys of the dictionary or not or whether the no. of its occurence is 1 less then the length of the dictionary. 
#this code is giving runtime error for 11/20 testcases.
#the below code is not my code and is passing all the testcases need to study this code.
#def isValid(s):
    #Create a list containing just counts of each distinct element
    freq = [s.count(letter) for letter in set(s) ]
    #If all values the same, then return 'YES'
 #   if max(freq)-min(freq) == 0:
 #       return 'YES'
    #If difference between highest count and lowest count is 1
    #and there is only one letter with highest count, 
    #then return 'YES' (because we can subtract one of these 
    #letters and max=min , i.e. all counts are the same)
 #   elif freq.count(max(freq)) == 1 and max(freq) - min(freq) == 1:
 #       return 'YES'
    #If the minimum count is 1
    #then remove this letter, and check whether all the other
    #counts are the same
 #   elif freq.count(min(freq)) == 1:
 #        freq.remove(min(freq))
 #       if max(freq)-min(freq) == 0:
 #           return 'YES'
 #       else:
 #           return 'NO'
 #   else:
 #       return 'NO'
