# Напишите программу, которая определит позицию второго вхождения строки в списке, либо сообщит, -1

my_list = ['qwe', 'asd', 'zxc', 'qwe', 'erwgwrvw']
count = 0
str_to_find = 'qwe'

if my_list.count(str_to_find) > 1:
    my_index = my_list.index(str_to_find)
    print(my_list[my_index+1:].index(str_to_find))
else:
    print(-1)
    
# for i in range(0, len(my_list)):
#     if my_list[i] == str_to_find:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print('-1')

# if str_to_find in my_list:
#     my_index = my_list.index(str_to_find)
#     if str_to_find in my_list[my_index+1:]:
#         print(my_list[my_index+1:].index(str_to_find))
#     else:
#         print(-1)
# else:
#     print(-1)

