figures=list()
i=int(input("enter the number of figures to be entered"))
for x in range(i):
    try:
        num=int(input('enter a number'))
        figures.append(num)
    except:
        print("enter a valid number")
        i=i+1
figures.sort()
print(figures)
print(len(figures))
print(max(figures))
print(min(figures))
print(sum(figures))
