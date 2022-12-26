# Реализуйте алгоритм задания случайных чисел без использования генератора псевдослучайных чисел

import time

current_time=time.time()

print(current_time)

rand_num = int(100*current_time)
print(rand_num %100)
print(str(rand_num)[-7:1])