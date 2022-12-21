# 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n=int(input("Введите число: "))
dict={}
sum=0
for n in range(1,n+1):
    dict[n]=round((1 + 1 / n)**n, 2)  
    sum+=dict[n]
    print(sum)
print(dict)
print(f'сумма элементов: {sum}')
# print(f'сумма элементов: {sum(dict.values)}') 