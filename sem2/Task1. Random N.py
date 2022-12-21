# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.

import random

n = int(input("Enter thr number: "))
for i in range(n):
    print(random.randint(0, 10), end=" ")