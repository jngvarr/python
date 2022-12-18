t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
print(type(colors)) # list
y = tuple(colors) # преобразование list в tuple
print(y) # ('red', 'green', 'blue')
print(type(y)) # tuple
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
print()
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
    print(e) # red green blue
    #t[0] = 'black' # TypeError: 'tuple' object does not support item assignment
li=list(t)
print()
li[0] = 'black'
print(li[0])

t = tuple(['red', 'green', 'blue'])
red, green, blue = t # получение переменных из кортежа
print('r:{} g:{} b:{}'.format(red, green, blue)) # # r:red g:green b:blue   