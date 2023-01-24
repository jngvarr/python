# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1. Напишите программу, которая принимает на вход принимать число N и выводитчисла от -N до N

# n = int(input('Введите число '))
# print([i for i in range(-n, n+1)])

# 2. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# my_list = list(map(int, input('Введите числа, через пробел: ').split()))
# print(sum(my_list[1::2]))

# 3.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# sourse_list =[2, 3, 4, 5, 6]
# import math
# list_a = list(map(int, sourse_list))
# print('Исходный список: ',list_a)
# print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))

# 4. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# from math import factorial
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))