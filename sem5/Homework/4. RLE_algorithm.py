# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
os.system('cls')

def compress(sourse_string):
    encoding_string = []
    i = 0
    while i < len(sourse_string):
        count = 1
        while i + 1 < len(sourse_string) and sourse_string[i] == sourse_string[i + 1]:
            count += 1
            i += 1
        encoding_string.append(str(count))
        encoding_string.append(sourse_string[i])
        i += 1
    return "".join(encoding_string)

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    print(f'путь к файлу: {path}')

    with open(path + '\sourse_file.txt', 'r') as data:
        sourse_string = data.read()
        print(sourse_string)
        encoding_string = compress(sourse_string)
        print(encoding_string)
    with open(path + '\\result_file.txt', 'w') as result:
        result.write(encoding_string)

if __name__ == '__main__':        
    main()