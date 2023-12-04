import os

# sub_str='s'
# for i in range(1,6):
#     s = sub_str*i
#     print(f'{s:10}')
    
# '    s'
# '   ss'
# '  sss'
# ' ssss'
# 'sssss'

# print("\"fdfdf\"")

# import re
 
# test_str = '04-01-1997'
# pattern_str = r'^\d{4}-\d{2}-\d{2}$'
 
# if re.match(pattern_str, test_str):
#     print("True")
# else:
#     print("False")

def dictinaryCreate():
    dict = {}
    with open(os.path.dirname(os.path.abspath(__file__))+'\\notes.csv', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for i in range(len(lines)):
            key, val = lines[i][:lines[i].index(
                ";")], (lines[i][lines[i].index(";")+1:]).split(";")
            dict[key] = val
        return dict
        
def notes_byDate_list(dict):
    # print(el[0] for  el in dict.values())
    for k, v in dict.items():
        # if v[2]==date:
            print(dict[k])
            # print_note(k,dict)

notes_byDate_list(dictinaryCreate()) 