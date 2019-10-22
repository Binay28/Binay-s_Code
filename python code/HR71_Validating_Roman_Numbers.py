regex_pattern = r"[XI{1,3}VLCDM]"	# Do not delete 'r'.
#import re

#thousand = 'M{0,3}'
#hundred = '(C[MD]|D?C{0,3})'
#ten = '(X[CL]|L?X{0,3})'
#digit = '(I[VX]|V?I{0,3})'
#print (bool(re.match(thousand + hundred+ten+digit +'$', input())))

import re
print(str(bool(re.match(regex_pattern, input()))))
