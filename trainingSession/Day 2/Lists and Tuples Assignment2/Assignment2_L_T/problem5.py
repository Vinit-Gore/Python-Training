'''
Given a list of lists, find the list with highest sum of elements.
'''
list1 = [[10,20,30], [40,50,60], [70,80,90],[-2,300,-200]]
sum = [0]*len(list1)
for (indexValue, lo) in enumerate(list1):
  for li in lo:
    sum[indexValue]+=li
i = sum.index(max(sum))  
print(list1[i])
