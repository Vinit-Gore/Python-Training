import re
s = input('Please input string: ')
print((lambda x, y: y[y.find(x)+1:y.find(x)+3] if x in y else 'Error')('#', s))
