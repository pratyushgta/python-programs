student = dict()

for i in range(5):
    name = input("Enter student name: ")
    marks = list()
    print("Enter marks of 5 subjects")
    for j in range(5):
        marks.append(int(input()))
    student[name] = marks

print(">>STUDENT DETAILS<<")
print(student)


