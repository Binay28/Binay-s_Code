# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
data=list(map(int,input().split()))
print(calendar.day_name[calendar.weekday(data[2],data[0],data[1])].upper())
#use of calendar module
