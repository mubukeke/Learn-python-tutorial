"""
创建类时初始化列表中的参数会传递给类内的 init 函数，完成该类的一些属性的初始化。

The name of the StudentClass's name, is going be equal to the name that we passed in.
The name of the StudentClass's major, is going be equal to the major that we passed in.
The name of the StudentClass's gpa, is going be equal to the gpa that we passed in.
The name of the StudentClass's is_to_probation, is going be equal to the is_to_probation that we passed in.
"""


class StudentClass:

    def __init__(self, name, major, gpa, is_to_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_to_probation = is_to_probation
