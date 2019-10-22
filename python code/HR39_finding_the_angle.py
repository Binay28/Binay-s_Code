import math
lab=int(input())
lbc=int(input())
#lac=sqrt(sum(lab*lab,lbc*lbc))
print(str(round(math.degrees(math.atan2(lab,lbc))))+chr(176))
#this code is to find and print the angle formed by the line joining the midpoint of the hypotenuse and the right angle point of the triangle and the side BC.
