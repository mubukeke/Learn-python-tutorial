# keyword: def   function name: say_hi   parameters: none  冒号
def say_hi():
    name = input("Enter your name: ")
    print("Hello User " + name)


def say_age(age):
    print("Hello " + str(age))


def say_information(name, age):
    print("Hello " + name + ", you are " + str(age))


print("Top")
say_hi()
print("Bottom")
say_age(25)
say_information("Mike", 22)
