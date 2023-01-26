import os
import user_menu as um

def find_cont():
    with open(os.path.dirname(os.path.abspath(__file__))+'\db.csv', 'r',encoding = 'utf-8') as db:
        for line in db:
            print(line,end='')
    um.um()