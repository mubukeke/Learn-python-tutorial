from Object_Fucntion_Students import Student

student1 = Student("Oscar", "Accountant", 3.2)
student2 = Student("Mike", "Law", 3.5)
student3 = Student("Nicolas", "Law", 2.8)

print(student1.on_honor_roll())
print(student2.on_honor_roll())

print(student1.more_excellent(student2))
print(student1.same_major(student2))
print(student2.same_major(student3))
