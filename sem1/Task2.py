# Напишите программу, которая принимает на вход пять чисел и находит максимальное

# num1=int(input('Введите первое число='))
# num2=int(input('Введите второе число='))
# num3=int(input('Введите третье число='))
# num4=int(input('Введите четвертое число='))
# num5=int(input('Введите пятое число='))

# my_max = num1
# if my_max>num2

numbers = []
for i in range(1,6):
    numbers.append(int(input(f'Введите {i}-е число: ')))
    print(numbers)
    print(max(numbers))

my_max=0
for _ in range(5):
    num=(int(input(f'Введите число: ')))
    if my_max<num:
            my_max=num
print(my_max)