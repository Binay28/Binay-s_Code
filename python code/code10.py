fhand=open('/media/binay/TOSHIBA EXT/study/computer and music/python for everybody/words.txt')
count=0
for line in fhand:
    count=count+1
    if line.startswith('We'):
        print(line)
print('line count:',count)
inp=fhand.read()
print(len(inp))
print(inp[:20])
