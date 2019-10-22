if __name__ == '__main__':
    ls=list()
    names=list()
    scores=list()
    #dic=dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name,score])
        if score not in scores:scores.append(score)
        #dic[score]=dic.get(score,ls1())
    ls.sort(key=lambda i:i[1])
    scores.sort()
    for i in ls:
        if(i[1]==scores[1]):names.append(i[0])
    names.sort()
    for i in names:print(i)

#Code could have been shorter like below:
#marksheet = []
#for _ in range(0,int(input())):
 #   marksheet.append([input(), float(input())])

#second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
#print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

