'''
Given a list of tuples, find the smallest second index value from a list of tuples.
'''
x = [(3, 1), (4, 2), (9, 0), (6, -2),  (-9, -1)]
min = 0
for t in x:
  if t[1] < min:
    min = t[1]
print(min)