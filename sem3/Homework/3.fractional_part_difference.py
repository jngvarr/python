# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import list_create as new_list

my_list = new_list.create_doublelist(int(input("Введите количество элементов: ")))

print(my_list)
max_fract=my_list[0]-int(my_list[0])
min_fract=my_list[0]-int(my_list[0])
for element in my_list:
    if element-int(element) > max_fract:
        max_fract=element-int(element)
    if element-int(element) < min_fract:
        min_fract=element-int(element)
# print(max_fract, min_fract, max_fract-min_fract)
print("Максимальная дробная часть:{0:5.2f}, минимальная дробная часть:{1:5.2f}, их разность:{2:5.2f} "
.format(max_fract, min_fract, max_fract-min_fract))