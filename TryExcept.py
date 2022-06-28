
# catch 的异常过于笼统
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.Please enter a number.")


# 通过在 except 后面指定错误类型来精细化定位异常类型
try:
    number = int(input("Enter a number: "))
    print(number)
    num = 10 / 0
except ZeroDivisionError as zeroErr:
    print(zeroErr)
# except ZeroDivisionError:
#     print("Divided by zero.")
except ValueError:
    print("Invalid Error.")
