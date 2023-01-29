import model



def user_menu():

    menu_items = {1: "Добавить нового ученика", 
                  2: "Отчислить ученика",
                  3: "Переведи ученика в дпугой класс", 
                  4: "Вывести список всех учеников школы", 
                  5: "Закончить работу"}   

    choice = int(input(f'\nВыберете действие: \n\n'+''.join(str(k)+ ". "
     + str(v) + ' - нажмите ' + str(k) +"." + '\n' for k, v in menu_items.items())+" -> "))
    while choice not in menu_items.keys():
        choice = int(input("Такой пункт в меню осутствует. Выберите пункт из списка: "))
    if choice == 1:
        model.create_student_data()
    if choice == 2:
        model.delete_student()
    if choice == 3:
        model.student_transfer()
    if choice == 4:
        model.student_list()
       
   