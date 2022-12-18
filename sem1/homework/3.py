# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input('Введите x-коодринату точки : '))
y = int(input('Введите y-коодринату точки : '))

if x==0 and y==0:
    print("точка находится в начале координат")
    exit()
if x==0:
    print("точка лежит на оси Y")
elif y==0:
    print("точка лежит на оси X")
elif x > 0 and y > 0:
    print("Первая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
else:
    print("Четвертая четверть")
