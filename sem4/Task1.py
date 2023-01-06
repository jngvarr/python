# Задайте строкку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве разделителя использовать пробел

list_num = input("введите числа через пробел: ").split() # ввод списка строковых элементов
print(list_num)
max_num = list_num[0]
min_num = list_num[0]

list_num = list(map(int, list_num)) # перебираем список строковых значений, преобразуем в список целых значений
print(max(list_num), min(list_num)) # встроенная функция поиска максимального и минимального значения в списке

# from random import randrange
# import list_create as create_list

# num = randrange(10)
# new_list=create_list.create_intlist(num)
# print(new_list)
