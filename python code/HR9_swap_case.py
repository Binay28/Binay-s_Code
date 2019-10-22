def swap_case(s):
    return s.swapcase()
    #return ''.join(i.lower() if i.isupper() else i.upper() for i in s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#both the statements work. swapcase() is a built in function in python
