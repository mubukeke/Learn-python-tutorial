import os.path

# employee_file = open("ReadingFiles_employee.txt", "r")
# employee_file = open("ReadingFiles_employee.txt", "a")    # "a" means append behind
employee_file = open("ReadingFiles_employee.txt", "w")   # only "w" means override

try:
    print("------------------")
    employee_file.write("\nToby - Human Resources")
    employee_file.write("\nKelly - Customer Servers")

except ValueError as readErr:
    print(readErr)

employee_file.close()

# write in a new file
employee_new_file = open("WritingNewFiles.txt", "w")

employee_new_file.write("TaiWan is China.")

employee_new_file.close()
