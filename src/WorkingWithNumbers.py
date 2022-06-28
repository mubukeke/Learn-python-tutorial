print(2)
print(2.35)
print(-3.2)
print(3 + 4.5 + 3*3 + (1 + 2)/3)
print(10 % 3)   # mod

my_number = -5
print(my_number)
print(str(my_number) + " is my number.")   # str() print number to string "-5"
print(abs(my_number))   # abs() absolute value of negative number = |-5|
print(pow(9, 2))   # pow(底数，指数) 9^2 = 81
print(max(4, 6))   # max()/min()
print(round(3.3))   # round() 四舍五入取整 = 3
# print(floor(4.3))   # python 库里没有这个函数

from math import *
print(floor(4.6))   # 从 math module 里面导入所有的函数库，供我使用。 floor() 向下取整 = 4
print(ceil(4.2))   # ceil() 向上取整 = 5
print(sqrt(49))   # sqrt() = 7
