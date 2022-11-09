# Q1
x = lambda a: a + 15
x2 = lambda a, b: a * b
N = int(input("Enter a number: "))
print(x(N))
m, n = input("Enter 2 numbers to multiply: ").split()
print(x2(int(m), int(n)))


# Q2
lst = list()

N = input("Enter list elements: ").split()

for i in N:
    lst.append(int(i))

print("\nOriginal list of integers:")
print(lst)

print("\nSquare every number of the said list:")
sq = list(map(lambda x: x ** 2, lst))
print(sq)

print("\nCube every number of the said list:")
cu = list(map(lambda x: x ** 3, lst))
print(cu)


# Q3
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filterDays = filter(lambda day: day if len(day) == 6 else "", days)  # method 1
filterDays2 = list(filter(lambda x: (len(x) == 6), days))  # method 2

print("Output of Method 1: ")
for i in filterDays:
    print(i)

print("\nOutput of Method 2: ")
print(filterDays2)


# Q4
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

sum = list(map(lambda x, y: x + y, lst1, lst2))
print(sum)


# Q5
students = []
second_low = 0

n = int(input("Input number of students: "))
for i in range(n):
    name = input("Student Name: ")
    grade = float(input("Grade: "))
    students.append([name, grade])

print("\nNames and Grades of all students:")
print(students)

SortedStudents = sorted(students, key=lambda x: int(x[1]))

for i in range(n):
    if SortedStudents[i][1] != SortedStudents[0][1]:
        second_low = SortedStudents[i][1]
        break

print("\nSecond lowest grade: ", second_low)

secLow_student = [x[0] for x in SortedStudents if x[1] == second_low]
secLow_student.sort()

print("\nNames:")
for name in secLow_student:
    print(name)


# Q6
lst = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

divCheck = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, lst))

print("Numbers divisible 13 or 19:", divCheck)


# Q7
lst = list()

names = input("Enter the names: ").split()

for i in names:
    lst.append(i)

UppercaseNames = list(filter(lambda x: x if x[0].isupper() else "", lst))
total_Len = lambda x: sum(len(i) for i in x)

print(total_Len(UppercaseNames))


# Q8
lst = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

max_list = max(lst, key=lambda i: len(i))
min_list = min(lst, key=lambda i: len(i))

print("Original list:")
print(lst)

print("\nList with maximum length of lists:")
print(len(max_list), ",", max_list)

print("\nList with minimum length of lists:")
print(len(min_list), ",", min_list)

