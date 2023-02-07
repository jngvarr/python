def calc(my_list):
    num1, num2, operation = my_list
    match operation:
        case "+":
            result = num1+num2
        case "-":
            result = num1-num2
        case "*":
            result = num1*num2
        case "/":
            result = num1/num2
    return result