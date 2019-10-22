cube = lambda x:pow(x,3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    ls=[0,1]
    for i in range(n-2):ls.append(ls[i]+ls[i+1])
    #elif(n==1):ls=0
    return ls[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
#The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
#Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.
#Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries. 
