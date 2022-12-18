list1 = [1, 2, 3, 4, 5]
list2 = list1

list1[0] = 123
list2[1] = 333

for e in list1:
    print(e)
print()
for e in list2:
    print(e)

print()
for i in list1:
    list1.pop()
    print(list1)

list1 = [1, 2, 3, 4, 5]
list1.pop(2)
print(list1)

list1.insert(2, 11) # добавление элемента списка (11) на указанную позицию в списке (2)
print(list1)

list1.append(22) # добавление элемента списка (22) в конец списка
print(list1)