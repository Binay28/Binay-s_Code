x=int(input("enter the value of the base"))
y=int(input("enter the value of the power"))
p=1
for i in range(0,y):
 p=p*x
print("the result of", x,"to the power", y,"is:",p)
p=1
for i in range(0,x):
 p=p*y
print('the result of',y ,'to the power',x ,'is:',p)
