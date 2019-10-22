# Enter your code here. Read input from STDIN. Print output to STDOUT
result=True
for _ in range(int(input())):
    UID=input()
    if not UID.isalnum():result=False
    elif not (len(UID)==10):result=False
    
