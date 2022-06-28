
def max_num(number1, number2, number3):
    if number1 >= number2:
        if number1 >= number3:
            max_number = number1
        else:
            max_number = number3
    else:
        if number2 >= number3:
            max_number = number2
        else:
            max_number = number3
    return max_number


def max_num_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        max_number = num1
    elif num2 >= num1 and num2 >= num3:
        max_number = num2
    elif num3 >= num1 and num3 >= num2:
        max_number = num3
    return max_number


def max_num_three_list(num1, num2, num3):
    list = [num1, num2, num3]
    return max(list)


print(max_num(2, 2, 2))
print(max_num_three(3, 3, 3))
print(max_num_three_list(3, 1, 5))

