# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def random_dict_create(polynomials_degree):
    degree_dict = {}
    for i in range(0,polynomials_degree):
        degree_dict[i] = random.randint(1, 100)
    return degree_dict

def polynom_create(base_dictionary):
    poly_dict=dict(reversed(base_dictionary.items()))
    # проверка на наличие нулевого коэффициента и его удаление
    poly_dict_copy = poly_dict.copy() # создание копии полинома для итерации и удаления элемента т.к. удаление из итерируемого объекта вызывает ошибку
    # poly_dict_copy[3]=0
    # print(poly_dict_copy)
    for values in poly_dict_copy:
        if poly_dict_copy[values] == 0:
            del (poly_dict[values])
    # print(degree_dict)
    poly = " ".join([str(v)+'*X^'+str(k)+" +" for k,v in poly_dict.items()])
    poly = poly.replace('*X^0 +', ' = 0')
    poly = poly.replace('X^1', 'X')
    return poly

def main():
    polynomials_degree = int(input("Задайте степень многочлена: "))+1
    rnd_dict = random_dict_create(polynomials_degree)
    polynom = polynom_create(rnd_dict)
    print(polynom)

    with open('polynom.txt', 'w') as data:
        data.write(polynom)

if __name__ == "__main__":
    main()
