def encode(sourse_string):
    # print(sourse_string)
    # print(sourse_string[0:len(sourse_string):2])
    # print(sourse_string[1:len(sourse_string):2])
    # tup=tuple()
    # print(tup[1],zip(sourse_string[0:len(sourse_string):2], sourse_string[1:len(sourse_string):2]))
    new_list =  "".join((map(lambda tup:  tup[0] * int(tup[1]), zip(sourse_string[0:len(sourse_string):2], sourse_string[1:len(sourse_string):2])))) 
    print(list(zip(sourse_string[0:len(sourse_string):2], sourse_string[1:len(sourse_string):2])))
    return new_list
tup=('1', '1'), ('3', '3')
tup1=list(zip("11335788", "11335888"))
tup2=list(zip("11335788", "11335888"))
tup3=tup1*tup2
print(tup1)
print(tup2)
print(tup3)

sourse_string = '1111333355788888'
# print(encode(sourse_string))