def split_and_join(line):
    # write your code here
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#program to explain the use of split and join function.Here "-"is the parameter for join function which is used to join the list elements.
