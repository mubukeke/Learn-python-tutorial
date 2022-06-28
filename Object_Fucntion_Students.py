
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def more_excellent(self, Student):   # 自己定义的比较两个类分数
        return self.gpa >= Student.gpa

    def same_major(self, Student):   # 自己定义的判断是否同专业
        result = ""
        if self.major == Student.major:
            result = self.name + " and " + Student.name + " are classmate."
        else:
            result = self.name + " and " + Student.name + " are not classmate."
        return result
