def merge_the_tools(string, k):
    # your code goes here
    s=list()
    for i in range(int(len(string)/k)):
        del s[:]
        for j in string[k*i:k*(i+1)]:
            if j not in s:s.append(j)
                #print(j)
        #print(map(''.join(),j for j in ))
        print(''.join(s))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
#program to print the strings from the substrings with distinct character substrings are of size k
