import os

def creat_BD():

    with open (os.path.dirname(os.path.abspath(__file__))+'\db.csv', 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия; Имя; Номер телефона; Описание\n')
        