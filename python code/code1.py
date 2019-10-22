x=float(input('enter the rating of the movie :'))
y=input('enter the rating type')
if(x>5.5 and(y=='imdb'or y=='IMDB')):
 print('it is a good movie')
elif (x>5.5):
 print('it is an average movie')
else:
 print('it is a bad movie')
