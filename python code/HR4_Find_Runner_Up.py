if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #dic=dict()
    ls=list()
    #for i in arr:
    #    dic[i]=dic[i].get(i,0)+1
    #dic.sort()
    #print(dic)
    for i in arr:
        if i not in ls:ls.append(i)
    ls.sort(reverse=True)
    print(ls[1])
#here in sort function parameter reverse=True sorts the list in descending order
