# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# вариант 1 :

sourse_str = 'Напишите абв АбВпрограмму,  АБВудаляющую из текста все слова, содержащие "абв". '
print(sourse_str)

new_str = list(filter(lambda elem: 'абв' not in elem.lower(), sourse_str.split() ))
print(*new_str)

new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), sourse_str.split())))
print(new_str)