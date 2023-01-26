# first_name=[1]
# last_name=[2]
# tel_num=[3]
# comment=[4]

# contact=list(zip(first_name,last_name,tel_num,comment))
# print(contact)
# contact=list(enumerate(contact))
# contact=dict(contact)
# print(contact)
# # for e in contact:
# #     print(e)
contact=[]
contact.append(input("Имя: "))
contact.append(input("Введите фамилию: "))
contact.append(input("Введите номер телефона: "))
contact.append(input("Введите описание: "))
# contact=list(enumerate(contact))
print(contact)