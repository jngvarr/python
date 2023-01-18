# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal
import decimal
import math
from os import system
system("cls")
pi = math.pi
print(pi)
# d = int(input("Задайте точность(количество знаков после запятой) числа π: "))
d = input("Задайте точность(количество знаков после запятой) числа π: ")
if 0.0000000001 <= float(d) <=0.1:
    print(d.split("."))
    d=int(len(d.split(".")[1]))
# через Decimal
decimal.getcontext().prec = d+1
pi = Decimal(pi)/Decimal(1)
print(pi)

# через округление
print(round(pi, d))