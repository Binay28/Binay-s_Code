fig=list()
while True:
    inp=input("enter the number")
    if inp=='done':
        break
    else:
        try:
            num=int(inp)
            fig.append(num)
            continue
        except:
            print('enter a valid number')
            continue
fig.sort()
print(fig)
print(max(fig))
print(min(fig))
