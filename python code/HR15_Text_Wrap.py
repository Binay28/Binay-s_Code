mport textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#this program is used to get familiar with the textwrap library and wrap function
