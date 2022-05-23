list1 = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
list1.reverse()
index = len(list1) // 3
index2 = index * 2
list2 = list1[:index]
list3 = list1[index:index2]
list4 = list1[index2:]
print(list2)
print(list3)
print(list4)