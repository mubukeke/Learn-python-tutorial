print(2*4)   # 2 multiply 4 = 8
print(2**4)  # 2 exponential 4 = 2^4 = 16


def raise_to_power(base_num, pow_num):   # base^pow 指数函数。
    result = 1
    for pow_ in range(abs(pow_num)):   # 控制循环几次，也就相应的 base_num 自己乘了多少次
        result = result * base_num

    if pow_num < 0:
        result = 1 / result   # 除就是 1 / 2 = 0.5

    return result


print(raise_to_power(2, -3))
