def almost_fact(mult):
    if mult == 1: return 1
    a=almost_fact(mult - 1) * mult
    my_list.append(a)
    return my_list


my_list = []
num = int(input("Введите число: "))
print(almost_fact(num))