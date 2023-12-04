import os


# str = "1;первая заметка;текст первой заметки;2023-04-27_14:43:39;2023-04-27_14:43:39"
# print(str[:str.index(':')])

def notes_list():
    dict = {}
    arr = []
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\notes.csv', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for i in range(1, len(lines)):
            key, val = lines[i][:lines[i].index(
                ";")], (lines[i][lines[i].index(";")+1:]).split(";")
            dict[int(key)] = val
            

    for k, v in dict.items():
         print(k,":", v[0])

        # dict_keys = list(dict)
        # print(dict_keys)
    # for i in range(len(dict_keys)):
    #     print(dict_keys[i], dict[i+1][0])


        # for i in range(len(dict)+1):
        # print(dict.keys()[1])
            # print()
            # print(dict.get(i), dict[i][0])
            # print(val)
    # d =dict[2][0]
    # print(d)
    # for k, v in dict.items():
    #     print(k,":", v)

#     arr = [line.split(';') for line in lines]
# for elem in arr[2]:
#     print (elem)
#             dict[int(key)] = val
# for key in dict:
#     print (dict.values)

notes_list()

# for i in range(len(lines)):
#             arr = [line for line in lines]
#             print (arr[i])

# lines = file.read().splitlines()
#         last_line = lines[-1]
#         for i in range(len(lines)):
#             for j in lines[i].split(';'):
#                 print(j,end=""+" ")
#             print()
# note_id_counter = last_line[:last_line.index(";")]
# print( int(note_id_counter))
