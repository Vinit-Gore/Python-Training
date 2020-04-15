list1 = [1, 2, 3, 4]
list1[1] = 3
print(list1)

list2 = [1, 2, 3, 4]
print(list2, "-> id : ", id(list2))
list2 = [2, 3, 4, 5]
print(list2, "-> id : ", id(list2))
