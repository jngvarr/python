import user_menu as um
import os

path=os.path.dirname(os.path.abspath(__file__))

def fill_bd(data):
    with open(path+'\db.csv', 'a', encoding = 'utf-8') as phone_db:
        phone_db.write((f'{data[0]}\t;{data[1]}\t;{data[2]}\t;{data[3]}\n'))
    

def writing_txt (data):
    with open (path +'\db.txt', 'a', encoding = 'utf-8') as dat:
        dat.write(f'Фамилия: {data[0]}\n\n Имя: {data[1]}\n\n Номер телефона: {data[2]}\n\n Описание: {data[3]}\n\n\n')

# um.user_menu()