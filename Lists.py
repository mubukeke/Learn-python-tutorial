friends = ["Kevin", "Karen", "Jim", 50, True]    # list []
         #    0        1       2     3   4
         #   -5        -4     -3    -2   -1
print(friends)   # 输出 list 中所有元素
print(friends[3])   # 索引输出指定元素
print(friends[-1])   # back of the lists output 使用负数
print(friends[1:])   # 输出1~最后
print(friends[1:3])   # [1, 3) = [1, 2]

friends[1] = "Mike"   # 通过索引修改list中某个位置的值
print(friends)
