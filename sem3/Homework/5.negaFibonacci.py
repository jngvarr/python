# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def nega_fib(n):
    fibo_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
        fibo_list.append(x)
        fibo_list.insert(0, -x if i % 2 else x)
    return fibo_list

num = int(input("Введите число: "))
print(nega_fib(num))
