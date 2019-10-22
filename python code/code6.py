fruit=input("enter the name fo the fruit :")
fl=0
for i in range (0,len(fruit)):
    try:
        lt=int(fruit[i])
        fl=fl+1
        print("#")
    except:
        print("*")
        continue
if fl==0:
    print("the fruit name ",fruit," is a valid fruit name") 
else:
    print("it is not a valid fruit name") 
