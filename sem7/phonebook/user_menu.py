import add_contact as new_cont
import print_contact as print_c
import thanks as th
import os
os.system("cls")

def user_menu():

    menu_items = {1: "Вывести на экран книгу контактов", 2: "Добавить новый контакт",3: "Закончить работу программы"}   

    choice = int(input(f'\nВыберете, что вы хотите сделать: \n\n'+''.join(str(k)+ ". "
     + str(v) + ' - нажмите ' + str(k) +"." + '\n' for k, v in menu_items.items())+" -> "))
    while choice > 3 or choice < 0:
        choice = int(input("Такой пункт в меню осутствует "))
    if choice == 1:
        print_c.find_cont()
    if choice == 2:
        new_cont.add_new_contact()
    if choice == 3:
        th.thanks()
   