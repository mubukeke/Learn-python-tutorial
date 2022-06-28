# txt, csv, html and so on.
employee_file = open("ReadingFiles_employee.txt", "r")   # 读取文件

if employee_file.readable():   # employee_file.readable()/writeable() 文件是够可读/可写 返回 boolean
    # 方式一：
    # print(employee_file.read())  # employee_file.read() 读取
    print("-----------")
    # 方式二：
    # print(employee_file.readline())  # 读取第一行
    # print(employee_file.readline())  # 紧接着读取第二行等等
    # 方式三：
    employee_list = employee_file.readlines()   # readlines 把所有行存储在 list 中
    for line in employee_list:
        print(line)

employee_file.close()   # 关闭文件
