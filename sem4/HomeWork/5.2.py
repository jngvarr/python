num_1 = '83*x^2 + 43*x^1 + 57*x^0 = 0'.replace(' ', '')
num_1 = num_1[:num_1.find('=')].split('+')
num_2 = '23*x^5 + 25*x^4 + 37*x^3 + 72*x^2 + 41*x^1 + 52*x^0 = 0'.replace(' ', '')
num_2 = num_2[:num_2.find('=')].split('+')
num_all = num_1 + num_2
my_dict = {}

for elem in num_all:
    key = int(elem[elem.find('^') + 1:])
    if key in my_dict:
        my_dict[key] += int(elem[:elem.find('*')])
    else:
        my_dict[key] = int(elem[:elem.find('*')])
    print(my_dict)

my_str = '' 
for key, value in sorted(my_dict.items(),reverse=True):
    my_str += f'{value}*x^{key} + '
print(my_str)  
my_str = my_str[:my_str.rfind('+')] + '= 0'
print(my_str)