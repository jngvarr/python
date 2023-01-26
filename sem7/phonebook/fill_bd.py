import user_menu as menu
import os

path=os.path.dirname(os.path.abspath(__file__))

def fill_csv_bd(data):
    with open(path+'\db.csv', 'a', encoding = 'utf-8') as phone_db:
        phone_db.write((f'{data[0]};{data[1]};{data[2]};{data[3]}\n'))
    

def fill_txt_bd(data):
    with open (path +'\db.txt', 'a', encoding = 'utf-8') as dat:
        dat.write(f' Фамилия: {data[0]}\n\n Имя: {data[1]}\n\n Номер телефона: {data[2]}\n\n Описание: {data[3]}\n\n\n')
    menu.um()
