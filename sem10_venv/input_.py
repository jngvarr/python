import calculate_

def input_data():
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    if 'j' in num1 or 'j' in num2:
        num1=complex(num1)
        num2=complex(num2)
    else:
        num1=float(num1)
        num2=float(num2)

    operation = input('Введите операцию:  +,  -,  *,  /: ')
    return (num1, num2, operation)

def input_bot_data(my_list):
    num1, num2, operation = my_list
    if 'j' in num1 or 'j' in num2:
        num1=complex(num1)
        num2=complex(num2)
    else:
        num1=float(num1)
        num2=float(num2)

    return (calculate_.calc(my_list=(num1, num2, operation)))