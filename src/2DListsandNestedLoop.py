number_grid = [
    [1, 2, 3, 4, 5],
    [11, 22, 33, 44],
    [111, 222, 333],
    [0, 0]
]

# nested loop = two for loop
for row in number_grid:   # row 变量就是行，也就是 2D list 中的 list
    for col in row:       # col 变量就是行中的元素，也就是 list 中的元素
        print(col, end=" ")   # 表示不换行，后面接空格
    print()               # 表示换行
