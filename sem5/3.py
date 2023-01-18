# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# вариант 1 :

my_str = 'самбо важный вид Спорта. Это как АбВ.  От АБВНовичков до Мастеров. '

# фильтер и лямбда + все в один регистр:
new_str = list(filter(lambda el: 'абв' not in el.lower(), my_str.split() ))
print(*new_str)



# вариант 2 :

my_str = 'АБВ важно удалАБВть фи снова эту_ абв удалить  абВ'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)