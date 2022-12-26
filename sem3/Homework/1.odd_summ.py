# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import list_create as new_list
my_list = new_list.create_intlist(int(input("Введите число: ")))
print(my_list)
odd_summ = 0
for i in range(1, len(my_list), 2):
    odd_summ += my_list[i]
print(f'Сумма элементов списка, стоящих на нечетной позиции = {odd_summ}.')
