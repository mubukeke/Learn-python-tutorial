number1 = input("Enter a number: ")
number2 = input("Enter another number: ")

result = int(number1) + float(number2)   # number1 and number2 are string. so plus is concat two numbers not add.
# 两种方式将 input 读取进来的字符串转化成为数字， int() float()  我们建议都使用 float() 做转换
print(result)
