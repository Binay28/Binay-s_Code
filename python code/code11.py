friend=['Kunal','Somu','HV','Ghanshyam']
friend1=['Mayank','Kumbha','Swarn','Pranav']
friend2=friend+friend1
friend3=list()
for i in range(4):
    print(friend[i])
    print(friend1[i])
for i in range(8):
    print(friend2[i])
print(len(friend))
print(friend2[2:5])
for i in range(3):
    data=input("enter your friends name")
    friend3.append(data)
print(friend3)
print('Kunali' in friend)
