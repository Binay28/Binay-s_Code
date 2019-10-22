import string
def print_rangoli(size):
    # your code goes here
    strls=string.ascii_lowercase
    ls=list()
    for i in range(size):
        s = "-".join(strls[i:n])
        ls.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(ls[:0:-1]+ls))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
#not my code need to understand this logic
