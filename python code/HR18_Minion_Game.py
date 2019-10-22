def minion_game(string):
    # your code goes here
    vowels=["A","E","I","O","U"]
    kscore=0
    Sscore=0
    for i in range(len(string)):
        #j=0
        if(string[i] in vowels):
            #kscore+=len(string[i:])
            kscore+=len(string)-i
        elif(string[i] not in vowels):
                #while(len(s[i:])!=j):
                #Sscore+=len(string[i:])
                Sscore+=len(string)-i
                #print(len(s[i:]),s[i:])
    if(Sscore>kscore):print("Stuart",Sscore)
    elif(Sscore<kscore):print("Kevin",kscore)
    else:print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
#my code for minion game but what is the difference between kscore+=len(string[i:]) and kscore+=len(string)-i
