# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_multiply(nums):
    simple_nums_list = [1]
    i = 2
    while i * i <= nums:
        if not nums % i:
            simple_nums_list.append(i)
            nums /= i
        else:
            i += 1
    if nums > 1:
        simple_nums_list.append(int(nums))
    return simple_nums_list


def main():
    num = int(input("Введите число: "))
    x_list = simple_multiply(num)
    print(x_list)
    
if __name__ =="__main__":
    main()
