# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except ValueError as e:
        print("Error Code:",e)
    except ZeroDivisionError as e:
        print("Error Code:",e)
#this code explains the use of exceptions with parameters in python
