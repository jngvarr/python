# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# string = str(input().split())
path = r'C:\Users\Jngvarr\gb\python\sem5\new_file.txt'
string = ('1 2 \n3 4 5 \n6 8 9 \n10')
print(string)
with open(path, 'w') as data:
    data.write(string)
with open(path, 'r') as data:
    string_data = data.read()
    num_row = list(map(int, string_data.split()))
    # num_row = list()
    # for line in data:
    #     print(line)
    #     num_row += list(map(int, line.split()))
print(num_row)

print(filter(lambda e:e[i]+1!= e+1, num_row))

# for i, elem in enumerate(num_row[:-1]):
#     print(i,elem)
#     if elem + 1 != num_row[i+1]:
#         print(elem + 1)
#         # break