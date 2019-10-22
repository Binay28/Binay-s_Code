# Enter your code here. Read input from STDIN. Print output to STDOUT
#for i in range(int(input())):
 #  if (input().startswith("+")or input().startswith("-")or input().startswith(".")):
import re
[print(bool(re.match(r'[-+]?[0-9]*\.[0-9]{1,}$',input()))) for i in range(int(input()))]        
#use of regular expressions is very useful
