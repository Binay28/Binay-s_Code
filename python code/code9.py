handle=open('Makefile')
print(handle)
for word in handle:
    print(word)
stuff=handle.read()
print(stuff)
print(len(stuff))
