# Giraffe Language 用字母 g 替换单词中的元音字母
# vowels(a e i o u) -> g
# ----------------------
# dog -> dgg

# str 可以相加；单引号字符可以和双引号字符串一起相加。
letter1 = 'a'
letter2 = "b"
trans = ""
print(trans + letter1 + letter2)


def translate(phrase):
    translation = ""
    for letter in phrase:
        # if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or \
        #    letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        if letter in "AEIOUaeiou":   # 判断某个元素是否为元音， if letter in "AEIOUaeiou": 即可
        # if letter.lower() in "aeiou":
            letter = 'g'
        translation += letter
    return translation


print(translate("HellOWorlD"))
print(translate(input("Enter a phrase: ")))
