# Задайте строкку из набора чисел. Напишите программу, которая покажет большее и меньшее число.

# from random import randrange
# import list_create as create_list

# num = randrange(10)
# new_list = create_list.create_intlist(num)
# print(new_list)

# max_num=new_list[0]
# min_num=new_list[0]

# for num in new_list:
#     num = int(num)
#     if num > (max_num):
#         max_num = num
#     if num < (min_num):
#         min_num = num
# print(max_num, min_num)

# второе решение

from random import randrange
import list_create as create_list


def find_min_max(list_num):
    max_num = list_num[0]
    min_num = list_num[0]

    for num in list_num:
        num = int(num)
        if num > (max_num):
            max_num = num
        if num < (min_num):
            min_num = num
    return min_num, max_num

def main(): # базовая функция
    num = randrange(1,10)
    new_list = create_list.create_intlist(num)
    print(new_list)
    print(*find_min_max(new_list))  # *-  распаковка, печать каждго члена

if __name__ =="__main__":
    main()