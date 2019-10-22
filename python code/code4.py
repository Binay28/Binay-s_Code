smallest=None
print("before")
for value in(9,41,12,3,74,15):
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print("smallest so far :",smallest)
print("the final smallest :",smallest)
