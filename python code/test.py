import re
#fh = open('Sample_Data.txt','r')
fh = open('Actual_Data.txt','r')
sum=0
for line in fh:
    num=re.findall('[0-9]+',line)
    for i in num:
        sum+=int(i)
print(sum)
    
