# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
#ch=['-','.','_']
pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for i in range(n):
    name,email=map(str,input().split())
    pos=email.find(".")
    if(re.match(pattern,email)): print(name+" "+email)
#if (not email[pos+1:-1].isalpha() or not email[1].isalpha()):continue
#elif (not email[1:pos+1].isalnum() or not i not in ch for i in email[1:pos+1]):
#continue
#elif (len(email[pos+1:-1])==3):print(name+" "+email)
#In this code we have used the special characters
