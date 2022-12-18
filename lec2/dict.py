# Словари
# Неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

print(dictionary['up']) # ↑
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐

# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
print(dictionary)

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →