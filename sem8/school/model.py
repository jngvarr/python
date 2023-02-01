import os
import view
import menu

student_id_counter = 0
students = {}
classes = {}


def get_student_class():
    pass


def add_new_student():
    new_student = dict()
    new_student['id'] = get_new_ID()
    new_student['first_name'] = view.get_new_student_info('students_first_name: ')
    new_student['last_name'] = view.get_new_student_info('students_last_name: ')
    new_student['birthday'] = view.get_new_student_info('students_bithday: ')
    add_student_to_class(new_student['id'])
    return new_student


def get_new_ID():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


def save_student_to_file(students):
    with open(os.path.dirname(os.path.abspath(__file__)) + '\students.csv', 'a', encoding='utf-8') as file:
        file.write(
            f"\n{students['id']};{students['first_name']};{students['last_name']};{students['birthday']}")


def add_student_to_class(student_id):
    student_class = view.get_new_student_info('student class to add: ')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]
    print(f'student with ID "{student_id}" added to "{student_class}" class')

def get_last_student_id():
    global student_id_counter
    with open(os.path.dirname(os.path.abspath(__file__))+'\last_student_id.txt', 'r', encoding='utf-8')as file:
        student_id_counter = int(file.read())


def save_last_student_id():
    global student_id_counter
    with open(os.path.dirname(os.path.abspath(__file__))+'\last_student_id.txt', 'w', encoding='utf-8') as file:
        file.write(f'{student_id_counter}')


def save_classes():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'w', encoding='utf-8') as file:
        for k, v in classes.items():
            file.write(k + "-" + str(v)+'\n')


def get_classes():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()  # 1a-[1, 2, 3]
        global classes
        for elem in temp:
            classes[elem[:elem.index('-')]
                    ] = elem[elem.index('[')+1:-2].split(", ")    
    classes = {key: list(map(int, value)) for key, value in classes.items()}

def print_data(class_student_to_remove):
    with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line[:line.index("-")] == class_student_to_remove:
                class_list = line[line.index('[')+1:line.index(']')].split(', ')
    with open(os.path.dirname(os.path.abspath(__file__))+'\students.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if line[:line.index(';')] == "ID":
                print(line[:line.index(';bir')].replace(';', '\t'))
            if line[:line.index(';')] in class_list:
                print(line[:line.rfind(';')].replace(';', '\t'))

def delete_student(action):
    class_student_to_remove = view.get_new_student_info(f'students class to {action} the student: ')
    global id_to_del
    print_data(class_student_to_remove)
    id_to_del = int(input("Enter the students id to remove: "))
    remove_student_from_class(class_student_to_remove, action)

def remove_student_from_class(class_student_to_remove, action):         
    global classes
    get_classes()
    classes = {key: list(map(int, value)) for key, value in classes.items()}
    for elem in classes.values():
        if id_to_del in classes[class_student_to_remove]:
            classes[class_student_to_remove].remove(id_to_del) 
    print(f'Student with ID "{id_to_del}" {action}ed from "{class_student_to_remove}" class.')
    save_classes()
    # menu.user_menu()

def student_transfer(action):
    delete_student(action+" off")
    add_student_to_class(id_to_del)
    save_classes()
    menu.user_menu() 
    
def student_list():
    with open(os.path.dirname(os.path.abspath(__file__))+'\students.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.replace(';', '\t'), end="")
    menu.user_menu()
   

def create_student_data():
    get_last_student_id()
    get_classes()
    stop = False
    while not stop:
        save_student_to_file(add_new_student())
        if view.get_new_student_info('"q" to stop: ').lower() == 'q':
            stop = True
    save_classes()
    save_last_student_id()
    menu.user_menu()
