# for loop in str
for letter in "Giraffe Academy":
    if letter != ' ':
        print(letter, end="")   # 输出不换行，对参数执行 end=“” 即可；如果 end=“ ”则输出后面空一格。
    else:
        print(letter)


# for loop in array
friends = ["Jam", "Mike", "Nico", "Ram"]
for name in friends:
    print(name)


for index in range(10):   # 遍历 [0, 10)
    print(index)

for index in range(5, 10):   # 遍历 [5, 10)
    print(index)

for index in range(len(friends)):   # 遍历 [0, 4)
    print(friends[index])
