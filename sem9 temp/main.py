import user_menu as menu
import os
import create_bd as cr_bd

def main():
    if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+'\db.csv'): 
        cr_bd.creat_BD ()
    menu.um()
if __name__ == '__main__':
    main()