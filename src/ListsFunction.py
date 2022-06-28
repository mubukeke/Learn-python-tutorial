lucky_numbers = [4, 6, 15, 16, 23, 24]
friends = ["kevin", "karen", "Jim", "Oscar", "Toby", "Jim"]
# 增
# friends.extend(lucky_numbers)   # list.extend() 在list后面添加 iterator,也就是添加其他 list 的每个元素
# friends.append("Mike")   # list.append() 在 list 后面添加一个 object
# friends.insert(1, "Vicky")   # list.insert(index, object) 在list index索引处插入一个 object
# friends.insert(2, lucky_numbers)   # 把整个list对象当作一个object插入到list中
# 删
# friends.remove(friends[1])   # list.remove() 删除一个object
# friends.clear()   # list.clear() 清空list
# friends.pop(2)   # list.pop(index) pop the element in index / last element
# 查
print(friends.index("Oscar"))   # list.index(element) find the index of the element if it exits.
print(friends.count("Jim"))
# 排序
friends.sort()   # list.sort() 默认ascend, reverse=True descend
print(friends)
lucky_numbers.sort(reverse=True)
print(lucky_numbers)
friends.reverse()   # list.reverse() list倒序输出
print(friends)
# 以上的所有操作都会修改 list 中 element
# 拷贝
friends_copy = friends.copy()   # list.copy() 拷贝一份给新的list
print(friends_copy)
