# 5 Реализуйте алгоритм перемешивания списка

import random
n = int(input("Введите число элементов списка: "))
random_list = []
for i in range(n):
    random_list.append(random.randint(-n, n))
print(random_list)
random.shuffle(random_list)
print(random_list)