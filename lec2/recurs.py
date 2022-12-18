def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
list = []
for e in range(1, 10):
    list.append(fibo(e))
print(list) # 1 1 2 3 5 8 13 21 34