import add_contact as new_cont
import find_contact as find_c
import import_contact_DB as DB

import os
os.system("cls")

def user_menu():

    menu_items = {1: "Найти контакт", 2: "Добавить новый контакт", 3: "Импорт контактов из файла"}   

    choice = int(input(f'Выберете, что вы хотите сделать: \n\n'+''.join(str(k)+ ". "
     + str(v) + ' - нажмите ' + str(k) +"." + '\n' for k, v in menu_items.items())+" -> "))
    while choice > 3 or choice < 0:
        choice = int(input("Такой пункт в меню осутствует "))
    if choice == 1:
        find_c.find_cont()
    if choice == 2:
        new_cont.add_new_contact()
    if choice == 3:
        DB.import_DB()
