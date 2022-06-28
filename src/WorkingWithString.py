print("Giraffe\nAcademy")
print("Giraffe\“Academy")
print("Giraffe\Academy")
print("Giraffe\\Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool.")
print(phrase.lower())
print(phrase.islower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))   # len() 求解string length
print(phrase[0])     # string[] 读取index出元素
print(phrase[len(phrase)-1])
print(phrase.index("a"))   # string.index(" ")字符串中查找某个单词，并输出index;查找不到不输出
print(phrase.index("aff"))   # string.index(" ")字符串中查找连续字符
# print(phrase.index("z"))    # throw an error
print(phrase.replace("ffe", "ttr"))  # string.replace(old, new) 字符串中替换
