# def f(x):
#     return x**2
# def f(x):
#     if x == 1:
#             return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType

# a = 1
# b = 4
# c=a
# a=b
# b=c
# # a, b = b, a
# print(a)
# print(b)

# Напишите программу, которая принимает на вход число и проверяет кратно ли оно 5 и 10 или 15 но не 30

num = int(input('Введите число '))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print("оно")
else:
    print('Не оно')
