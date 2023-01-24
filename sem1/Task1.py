# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно
# квадратом другого

num1, num2 = int(input('a= ')), int(input('b= '))
print(f'{num1}, {num2} ->', end=' ')
if num1**2 == num2 or num2**2 == num1:
    print('Да')
else:
    print('Нет')