# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal
import decimal
import math
pi = math.pi
print(pi)
d = int(input("Задайте точность(количество знаков после запятой) числа π: "))

# через Decimal
decimal.getcontext().prec = d+1
pi = Decimal(pi)/Decimal(1)
print(pi)

# через округление
print(round(pi, d))