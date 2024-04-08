stu = []
n = int(input("Enter how many students: "))
for i in range (n):
    nm = input("Enter the student name: ")
    age = int(input("Enter the student's age: "))
    mk = int(input("Enter the student's marks: "))

    d = dict(zip("Name","Age","Marks"),(nm,age,mk))
    stu.append(d)
print (stu)

