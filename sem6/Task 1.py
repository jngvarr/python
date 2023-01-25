# # Напишите программу где на вводе есть строка с выражением

def arythmetics(parse: list):
    while '*' in parse or '/' in parse:
        for i in range(1, len(parse) - 1): # parse.reverse() = parse[::-1] перебор списка из конца в начало, применять если удаляеся  найденный элемент
            if parse[i] == '*':
                oper1 = int(parse.pop(i - 1))
                oper2 = int(parse.pop(i))
                parse[i-1] = oper1 * oper2
                break
            elif parse[i] == '/':
                oper1 = int(parse.pop(i - 1))
                oper2 = int(parse.pop(i))
                parse[i-1] = oper1 / oper2
                break
    while '+' in parse or '-' in parse:
        for i in range(1, len(parse) - 1):
            if parse[i] == '+':
                oper1 = int(parse.pop(i - 1))
                oper2 = int(parse.pop(i))
                parse[i-1] = oper1 + oper2
                break
            elif parse[i] == '-':
                oper1 = int(parse.pop(i - 1))
                oper2 = int(parse.pop(i))
                parse[i-1] = oper1 - oper2
                break   
    return parse

user_input = input('Введите выражение: ')
num_str = ''
operands = user_input.replace('(', ' ( ').replace(')', ' ) ').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ')\
    .replace('-', ' - ').split()

if '(' in operands:
    left = operands.index('(') 
    right = operands.index(')')
    operands = operands[:left]+ arythmetics(operands[left+1:right]) + operands[right+1:]

print(arythmetics(operands))

# # Напишите программу где на вводе есть строка с выражением

# user_input = input('Введите выражение: ')
# num_str = ''
# parse = user_input.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split()
# print(parse)
# while '*' in parse or '/' in parse:
#     for i in range(1, len(parse) - 1):
#         if parse[i] == '*':
#             oper1 = int(parse.pop(i - 1))
#             oper2 = int(parse.pop(i))
#             parse[i-1] = oper1 * oper2
#             break
#         elif parse[i] == '/':
#             oper1 = int(parse.pop(i - 1))
#             oper2 = int(parse.pop(i))
#             parse[i-1] = oper1 / oper2
#             break
# while '+' in parse or '-' in parse:
#     for i in range(1, len(parse) - 1):
#         if parse[i] == '+':
#             oper1 = int(parse.pop(i - 1))
#             oper2 = int(parse.pop(i))
#             parse[i-1] = oper1 + oper2
#             break
#         elif parse[i] == '-':
#             oper1 = int(parse.pop(i - 1))
#             oper2 = int(parse.pop(i))
#             parse[i-1] = oper1 - oper2
#             break   
#     print(parse)