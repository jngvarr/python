# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите число: "))
temp_num = num
res = list()
while temp_num > 0:
    res.append(temp_num % 2)
    temp_num //= 2
res.reverse()
print(f'Десятичное число {num} в двоичном виде - {"".join(map(str, res))}')
