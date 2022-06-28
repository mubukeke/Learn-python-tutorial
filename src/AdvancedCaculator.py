
def advanced_caculator(number1, operator, number2):
    if not isinstance(operator, str):
        print("The operator must be str datapype.")
    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    elif operator == "*":
        answer = number1 * number2
    elif operator == "/":
        if number2 == 0:
            answer = 100000
        else:
            answer = 1.0 * number1 / number2
    else:
        print("Invalid operator.")
        answer = -1.1111
    return answer


num1 = input("Enter first number:")
op = input("Enter operator:")
num2 = input("Enter second number:")
print(advanced_caculator(float(num1), op, float(num2)))
