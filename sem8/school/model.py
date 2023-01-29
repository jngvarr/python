import os
import view

student_id_counter = 0
students = {}
classes = {}

def get_student_class():
    pass


def add_new_student():
    new_student = dict()
    new_student['id'] = get_new_ID()
    new_student['first_name'] = view.get_new_student_info('students_first_name')
    new_student['last_name'] = view.get_new_student_info('students_last_name')
    new_student['birthday'] = view.get_new_student_info('students_bithday')
    add_student_to_class(new_student['id'])
    return new_student



def get_new_ID():
    global student_id_counter
    student_id_counter +=1
    return student_id_counter



def save_student_to_file(students):
    with open(os.path.dirname(os.path.abspath(__file__)) + '\students.csv', 'a', encoding='utf-8') as file:
        file.write(f"\n{students['id']};{students['first_name']};{students['last_name']};{students['birthday']}")


def add_student_to_class(student_id):
    global classes
    student_class = view.get_new_student_info('student_class')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:    
        classes[student_class] = [student_id]

def get_last_student_id():
    global student_id_counter
    with open(os.path.dirname(os.path.abspath(__file__))+'\last_student_id.txt', 'r', encoding='utf-8')as file:
        student_id_counter = int(file.read())

def save_last_student_id():
    global student_id_counter
    with open(os.path.dirname(os.path.abspath(__file__))+'\last_student_id.txt', 'w', encoding='utf-8') as file:
        file.write(f'{student_id_counter}')

def save_classes():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'a', encoding='utf-8') as file:
        for k,v in classes.items():
            file.write(k + "-" + str(v)+'\n' )

def get_classes():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines() # 1a-[1, 2, 3]
        classes={}
        for elem in temp:
            classes[elem[:elem.index('-')]] = elem[elem.index('[')+1:-2].split(", ")
        print(classes)

def delete_student():
    student_to_delete = view.get_new_student_info("Input student class: ")
    with open(os.path.dirname(os.path.abspath(__file__))+ '\classes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line[:line.index("-")] == student_to_delete:
                class_list=line[line.index('[')+1:line.index(']')].split(', ')
    with open(os.path.dirname(os.path.abspath(__file__))+'\students.csv', 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line[:line.index(',')])
            # if line[2:line.index('ID')]
            # print(f'{line}'.split(';'))
            # print(line[:line.index("-")] )
    # print()(new_student['id'])




def student_transfer():
    pass

def student_list():
    pass


def create_student_data():
    get_last_student_id()
    get_classes()
    stop = False
    while not stop:
        save_student_to_file(add_new_student())
        if view.get_new_student_info('"q" to stop').lower() == 'q':
            stop = True
    save_classes()
    save_last_student_id()