# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел

a = int(input("input A: "))
b = int(input("input B: "))
max_num = max(a, b)

for i in range(max_num, a*b+1, max_num):
    if i % a == i % b == 0:
        print(i)
        break
