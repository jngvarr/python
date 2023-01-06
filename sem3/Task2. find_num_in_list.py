# Задайте список. Напишите программу, которая определит, присутствует ли в данном списке некое число

import random
# import os
# os.system("clear")

 # print(m in n_to_n_list)

n = int(input("Введите число: "))
n_to_n_list = []
for i in range(n):
    n_to_n_list.append(str(random.randint(-n, n)))
print(n_to_n_list)

m = input("Введите число для поиска: ")

# for i in n_to_n_list:
#     if m == i:
#         print("Такое число есть в списке")
#         break
# else: 
#     print("Такого числа нет в списке")
print(m in n_to_n_list)
