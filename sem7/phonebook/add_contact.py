import fill_bd as fill

def add_new_contact():
    contact=list()
    contact.append(input("Введите имя: "))
    contact.append(input("Введите фамилию: "))
    contact.append(input("Введите номер телефона: "))
    contact.append(input("Введите описание: ")) 

    fill.fill_csv_bd(contact)
    fill.fill_txt_bd(contact)