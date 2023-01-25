# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import list_create as new_list


def origin_element_list(list_):
    new_list = []
    for elem in list_:
        if elem not in new_list:
            new_list.append(elem)
    return (new_list)


def uniq_elements(list_):
    new_list = []
    for elem in list_:
        if list_.count(elem) == 1:
            new_list.append(elem)
    print(list(set(list_))) # множество set() не содержит дубликаты элементов
    return (new_list)

# def uniq_elements(list_):
#     new_list = []
#     # for i in range(len(list_)):
#     #     count = 0
#     #     for j in range(len(list_)):
#     #         if list_[i] == list_[j]:
#     #             count +=1
#         if count == 1:
#             new_list.append(list_[i])
#     return (new_list)


def main():
    my_list = new_list.create_intlist(
        int(input("Введите число элементов последовательноти: ")))
    print(my_list)
    print(f'Список с неповторяющимися элементами:\n{origin_element_list(my_list)}')
    print(f'Список уникальных элементов:\n{uniq_elements(my_list)}')


if __name__ == "__main__":
    main()
