import os

def add_new_contact():
    # first_name=[]
    # last_name=[]
    # tel_num=[]
    # comment=[]
    contact=list()
    path=os.path.dirname(os.path.abspath(__file__))
    contact.append(input("Введите имя: "))
    contact.append(input("Введите фамилию: "))
    contact.append(input("Введите номер телефона: "))
    contact.append(input("Введите описание: ")) 
    print(contact)
    # print(str(list(contact)).split(","))
    with open(path+'\db.csv', 'a', encoding = 'utf-8') as phone_db:
        phone_db.write((f'{contact[0]};{contact[1]};{contact[2]};{contact[3]}\n'))