
from Inheritance_Chef import Chef


class ChineseChef(Chef):

    def make_special_dish(self):   # 子类和父类同名函数，但做的事情不同,override
        print("The chef makes orange chicken.")

    def make_traditional(self):   # 子类特有的属性
        print("The chef makes fried rice.")
