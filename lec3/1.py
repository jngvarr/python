def f(e):
    return e**2

with open('file.txt', 'r') as data:
    str = data.read()
    data.close()
print(str)
str = list(map(int, str.split()))
str = [(e, f(e)) for e in str if not(e % 2)]
print(str)
# str = str.split()
# print(str)
# str = [(e, lambda e:e**2) for e in str if e % 2 == 0]
# print(str)
