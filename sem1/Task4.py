# Напишите программу, которая принимает на вход принимать дробь
# и показывать первую цифру дробной части числа

num = input('Введите число ')
if "." in num:
    print(num[num.find(".")+1])
else:
    print('нет')

num = float(input('Введите число '))
if not num % 1 == 0:
    print('no')
else:
    num = int(num*10 % 10)
print(num) 

num = float(input('Введите число '))
if num.isdigit():
    print('no') 
else:
    num = int(num*10 % 10)
print(num) 