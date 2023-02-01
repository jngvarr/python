import model

def um():

    menu_items = {1: "Добавить нового ученика", 2: "Отчислить ученика",
                  3: "Переведи ученика в дпугой класс", 4: "Вывести список всех учеников школы"}   

    choice = int(input(f'\nВыберете, что вы хотите сделать: \n\n'+''.join(str(k)+ ". "
     + str(v) + ' - нажмите ' + str(k) +"." + '\n' for k, v in menu_items.items())+" -> "))
    while choice > 4 or choice < 0:
        choice = int(input("Такой пункт в меню осутствует "))
    if choice == 1:
        model.add_new_student()
    if choice == 2:
        model.delete_student()
    if choice == 3:
        model.student_transfer()
    if choice == 4:
        model.student_list()