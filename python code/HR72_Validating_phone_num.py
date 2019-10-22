# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    m=re.match("^[789]{1}\d{9}$",input().strip())
    print("YES" if m else "NO")
#code for validating phone numbers using regular expressions
