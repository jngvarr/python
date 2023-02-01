import os
os.system("cls")

old_class = '1а'
new_class = '1а-[1, 6]'

def renew_classes(old_class, new_class):

    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + '\classes.txt', 'r', encoding ='utf-8') as f1, \
         open(path + '\classes1.txt', 'w', encoding ='utf-8') as f2:
         lines = f1.readlines()
         print(lines)
         for line in lines:
            line = line.strip()
            if line[:line.index("-")] == old_class:
                print(old_class)
                print(new_class)
                print(line[:line.index("-")])
                f2.write(new_class+"\n")
            else:
                f2.write(line+"\n")

renew_classes(old_class, new_class)