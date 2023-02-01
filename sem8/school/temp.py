import os
os.system('cls')

classes = {}

def get_classes():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\classes1.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()  # 1a-[1, 2, 3]
        global classes
        for elem in temp:
            classes[elem[:elem.index('-')]
                    ] = elem[elem.index('[')+1:-2].split(", ")

class_student_to_delete = "1а"
get_classes()
print(classes)
classes = {key: list(map(int, value)) for key, value in classes.items()}
print(classes)
id_to_del = int(input("Enter the student id to delete: "))

for elem in classes.values():
    print(elem)
    if id_to_del in classes[class_student_to_delete]:
        print(classes[class_student_to_delete])
        print("работает")
        classes[class_student_to_delete].remove(id_to_del)
print(classes)