# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = int(input("Введите число: "))
n_to_n_list = []
for i in range(n):
    n_to_n_list.append(random.randint(-n, n))
print(n_to_n_list)

quant_elements = random.randint(1, n)
print(str(quant_elements)+'\n')

mult = 1
data = open('file.txt', 'w')
data.write(str(random.randint(1, n-1)))
for _ in range(quant_elements-1):
    data.write('\n'+str(random.randint(1, n-1)))
data.close()

with open('file.txt', 'r') as data:
    for row in data:
        print(row, end='')
        mult *= n_to_n_list[int(row)]
print('\nПроизведение {} элементов = {}'.format(quant_elements,mult))
data.close()