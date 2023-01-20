def encode(sourse_string):

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

if __name__ == '__main__':

    sourse_string = 'wwwWWWxxxSSdd'
    print(encode(sourse_string))
