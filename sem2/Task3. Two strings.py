# Напишите программу, в которой пользователь будет задавать две строки,
# а программа определять количество вожденийодной строки в другую.

first_string = input("введите строку, в которой ищем: ")
second_string = input("введите строку, которую ищем: ")
count = 0
for i in range(len(first_string)-len(second_string)):
    if first_string[i] == second_string[0]:
        flag = True
        for j in range(1, len(second_string)):
            if second_string[j] != first_string[i+j]:
                flag = False
        if flag:
            count += 1
print(count)