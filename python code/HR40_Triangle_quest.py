for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print reduce((lambda a, v: a * 10 + v), map(lambda x: -1 * abs(x - i) + i, range(1, 2 * i)), 0)

#print(''.join(str(range(i+1)))+''.join(str(reversed(range(i+1)))))
#the challenge is here to print a triangle with each line consisting of a palindrome string of numbers.
