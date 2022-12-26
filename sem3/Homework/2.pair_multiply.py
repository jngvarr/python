# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import list_create as new_list

my_list = new_list.create_intlist(int(input("Введите число: ")))

print(my_list)
mult_list=list()
for i in range(0, (len(my_list)+1)//2):
     mult_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(mult_list)