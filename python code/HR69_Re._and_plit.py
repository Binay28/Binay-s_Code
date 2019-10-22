regex_pattern = r"[,.]+"	# Do not delete 'r'.
#print(*filter(None, re.split(r'[.,]+', input())), sep='\n')
#filter() returns every element in the second argument for which the function in the first argument evaluates as true. Using None as the first argument removes all items that are equivalent to false. The latter two test cases have consecutive delimiters, so using re.split() creates empty elements in the list. filter() returns the list without those empty elements.

#There are plenty of other ways to do it, though. I like BigJin's method below since it doesn't even need filter(), just adding a + to the regex to match consecutive delimiters.
import re
print("\n".join(re.split(regex_pattern, input())))
#the statements above import re are not mine and filter is a function
