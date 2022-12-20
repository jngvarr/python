# Для натурального N создать словарь индекс-значение, состоящих из элементов последователности 
# 3n+1

n = int(input("Enter thr number: "))
my_dict = {}
for i in range(1, n+1):
    my_dict[i]=3*i+1
print(my_dict)
