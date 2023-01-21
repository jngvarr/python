# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import polynom_create as new_polynom

def poly_create(poly_degree, path):
    rnd_dict = new_polynom.random_dict_create(poly_degree)
    polynom = new_polynom.polynom_create(rnd_dict)
    print(polynom)
    with open(path, 'w') as data:
        data.write(str(polynom))
    data.close()

def str_to_dictionary(path):
    data = open(path, 'r')   #
    poly = data.read()       # чтение данных из файла
    data.close()             #
    poly = poly.replace(' ', '')        #
    poly = poly.replace('*X^', ':')     # преобразование
    poly = poly.replace('*X', ':1')     # многочлена вида 37*X^5 + 43*X^4 + 24*X^3 + 2*X^2 + 93*X + 83 = 0
    poly = poly.replace('=0', ':0')     # в вид           37:5+43:4+24:3+2:2+93:1+83:0
                                        # преобразование строки 37:5+43:4+24:3+2:2+93:1+83:0
    # print(poly)
    poly_dict = dict((int(v), int(k)) for v, k in (e.split(':') for e in poly.split('+'))) # в словарь {37: '5', 43: '4', 24: '3', 2: '2', 93: '1', 83: '0'}
    # print(poly_dict)
    # перемена местами ключей и значений словаря {'5': 37, '4': 43, '3': 24, '2': 2, '1': 93, '0': 83}
    poly_dict = {v: k for k, v in poly_dict.items()}
    # poly_dict=set(poly_dict.values())
    return poly_dict

# Суммируем два словаря
def dict_sum(dict1, dict2):
    dict_keys = set(list(dict1.keys())+list(dict2.keys())) # перевод ключей двух словарей в одно множество
    dict_sum = {}
    for key in dict_keys:                                  # поиск по ключам множества значений в словарях
        val1 = dict1.get(key)                              # и их суммирование по 
        val2 = dict2.get(key)
        if val1 == None:
            val_sum = val2
        elif val2 == None:
            val_sum = val1
        else:
            val_sum = val1+val2
        dict_sum[key] = val_sum
    return dict_sum


def main():
    first_polynom_degree = int(input("Задайте степень первого многочлена: "))+1
    path1 = 'first_polynom.txt'
    second_polynom_degree = int(input("Задайте степень второго многочлена: "))+1
    path2 = 'second_polynom.txt'
    print('Создаются два случайных многочлена введенных степеней и записываются в соответствующие файлы.')
    print(f'Читаем из файла {path1} первый сгенерированный многочлен:')
    poly_create(first_polynom_degree, path1)
    print(f'Читаем из файла {path2} второй сгенерированный многочлен:')
    poly_create(second_polynom_degree, path2)
    poly1 = str_to_dictionary(path1)
    poly2 = str_to_dictionary(path2)
    # print(poly1)
    # print(poly2)
    dict_summ = dict_sum(poly1, poly2)
    # print(dict_summ)
    path_sum = 'sum_polynom.txt'
    sum_polynom = new_polynom.polynom_create(dict_summ)
    print(f'Сумма многочленов:')
    print(sum_polynom)
    with open(path_sum, 'w') as data:
        data.write(sum_polynom)
if __name__ == "__main__":
    main()
