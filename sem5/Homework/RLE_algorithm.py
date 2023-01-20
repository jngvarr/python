# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os 
os.system('cls')

path=os.path.dirname(os.path.abspath(__file__))
print(f'путь к файлу: {path}')

with open(os.path.dirname(os.path.abspath(__file__)) + '\sourse_file.txt', 'r') as data:
    str = data.read()
    print(str)
    print(len(str))
# from itertools import groupby
# def compress(str):
#     return [(key, len(tuple(group))) for key, group in groupby(str)]
 
def compress(str):
    print(str[1:len(str):2])
    print(str[0:len(str):2])
    print(zip(str[0:len(str):2], str[1:len(str):2]))
    lambda tup:  tup[0] * int(tup[1])
    
    new_list =  "".join((map(lambda tup:  tup[0] * int(tup[1]), zip(str[0:len(str):2], str[1:len(str):2])))) 
           
    print(new_list)  

compress(str)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for i in range(0,len(old_list)-1):
    #     count=1
    #     while old_list[i]==old_list[i+1]:
    #         count+=1
    #         i+=1
    #     if count >1:
    #        new_list.append(count)
    #        new_list.append(old_list[i])
    #        count=1
    #     else:
    #        new_list.append(count)
    #        new_list.append(old_list[i])