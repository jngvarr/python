# import shutil
# def delete_student():
#     class_student_to_delete = view.get_new_student_info("Input student class: ")
#     with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             if line[:line.index("-")] == class_student_to_delete:
#                 class_list = line[line.index('[')+1:line.index(']')].split(', ')
#     with open(os.path.dirname(os.path.abspath(__file__))+'\students.csv', 'r', encoding='utf-8') as file:
#         for line in file:
#             if line[:line.index(';')] == "ID":
#                 print(line[:line.index(';bir')].replace(';', '\t'))
#             if line[:line.index(';')] in class_list:
#                 print(line[:line.rfind(';')].replace(';', '\t'))
#     student_id_to_del = int(input("Enter the student id to delete: "))
#     with open(os.path.dirname(os.path.abspath(__file__)) + '\classes.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             if line[:line.index("-")] == class_student_to_delete:
#                 temp = list(map(int, line[line.index(
#                     '[')+1:-2].replace(' ', '').split(',')))
#                 del temp[temp.index(student_id_to_del)]
#                 temp_class = str()
#                 temp_class = class_student_to_delete+"-"+ str(temp)
#     file.close            
#     renew_classes(class_student_to_delete, temp_class)


# def renew_classes(old_class, new_class):
#     path = os.path.dirname(os.path.abspath(__file__))
#     with open(path + '\classes.txt', 'r', encoding ='utf-8') as f1, \
#          open(path + '\classes1.txt', 'w', encoding ='utf-8') as f2:
#          lines = f1.readlines()
#          for line in lines:
#             line = line.strip()
#             if line[:line.index("-")] == old_class:
#                 f2.write(new_class+"\n")
#             else:
#                 f2.write(line+"\n")

#     # shutil.move(path + '\classes1.txt', path + '\classes.txt')            
#     os.remove(path + '\classes.txt')
#     os.rename(path + '\classes1.txt', path + '\classes.txt')
