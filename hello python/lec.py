print ('hello world')

value = None
print('Введите a')
a= input() 
print('Введите b')
# b = 1.23
b=input()
print('Введите c')
c= int(input()) 
print('Введите d')
d=float(input())

print(type(a))
print(type(value))
print(type(b))
print(value)
s="'hello  world'"
#s="'hello \n world'"
print  (s)# вывод строки
#print(a,    b,s)
print(a, '-' ,  b,'-',s)
print('{} - {} - {}'.format(a, b,s))
print('{2} - {0} - {1}'.format(a, b,s))
print(f'{a} - {b} - {s}')
f=True
print(f)

list=[]
print(list)
list2=[list, '1', '2']
print(list2)
print(a,'+',b,'=',a+b)

print(c,'+',d,'=',c+d)