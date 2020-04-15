'''
Speed of tuple and list looping
'''

import time
COUNT = 10000

list1 = list(range(10, COUNT, 10))
tuple1 = tuple(range(10, COUNT, 10))


start = time.time()
for t in tuple1:
    pass
end = time.time()
tupletime = end - start

start = time.time()
for l in list1:
    pass
end = time.time()
listtime = end - start

if tupletime < listtime: 
  print("Tuple looping is faster")
else:
  print("List looping is faster")