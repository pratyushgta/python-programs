# Q1
print("Enter total number elements to add: ")
n = int(input())

tup = tuple()  # Empty Tuple
lst = list()  # Empty List

print("Enter", n, "elements:")
while n > 0:
    lst.append(input())
    n = n - 1

tup = tuple(lst)  # Converting list to tuple
print('Tuple:', tup)

print("\nSlicing the Tuple: ")
for i in range(len(tup)):
    print(tup[i])

print("\nAppending elements the Tuple: ")
lst = list(tup)  # Converting tuple to list to append new elements

ele = None
pos = None

while ele is None or pos is None:
    print("Enter the element to add: ")
    ele = input()
    print("Enter the position # or enter e to append it at the end: ")
    pos = input()
    if pos.lower() == "e":
        break
    elif int(pos) > len(tup) or int(pos) <= 0:
        if int(pos) == len(tup) + 1:
            print("Enter 'e' in position to append the element at the end")
        pos = None
        ele = None
        print("Invalid position. Re-enter")

if pos.lower() == "e":
    lst.append(ele)
else:
    lst.insert(int(pos) - 1, ele)

tup = tuple(lst)
print("\nTuple after insertions: ", tup)
print("\nConverting Tuple to List: ", "\nTuple:", tup, "\nList:", list(tup))

# Q2
print("Enter total number elements to add: ")
n = int(input())

tup = tuple()
lst = list()

print("Enter", n, "elements:")
while n > 0:
    lst.append(input())
    n = n - 1

tup = tuple(lst)

print("Enter the element to search: ")
search = input()

counter = 0

for i in range(len(tup)):
    if tup[i] == search:
        print("Element Found :D")
        counter = 1

if counter == 0:
    print("Element Not Found :(")

# Q3
lst_1 = list()
lst_2 = list()
print("Enter total number of list elements: ")
total = int(input())
print("Enter", total, "elements")

while total > 0:
    lst_1.append(int(input()))
    total = total - 1

for i in lst_1:  # Extracting an element from the list
    if i not in lst_2:  # Checking if the extracted element is in list 2
        lst_2.append(i)

print("Original List:", lst_1, "\nUnique List:", lst_2)

# Q4
lst_1 = list()
lst_2 = list()
counter = 0
print("Enter total number of list elements: ")
total = int(input())
print("Enter", total, "elements")

while total > 0:
    lst_1.append(int(input()))
    total = total - 1

for i in lst_1:
    if i not in lst_2:  # Creating a unique list
        lst_2.append(i)

for i in range(len(lst_2)):
    for j in range(len(lst_1)):
        if lst_2[i] == lst_1[j]:
            counter += 1
    print(lst_2[i], "appeared", counter, "times")
    counter = 0

# Q5
print("Enter number of rows: ")
rows = int(input())
print("Enter number of columns: ")
cols = int(input())

mat_1 = list()
mat_2 = list()
sum_mat = list()
total = rows * cols

print("MATRIX 1 \nEnter", total, "elements row-wise:")
for i in range(rows):
    temp = list()
    for j in range(cols):
        temp.append(int(input()))  # Defining each row
    mat_1.append(temp)  # Adding each row to the list

print("MATRIX 2 \nEnter", total, "elements row-wise:")
for i in range(rows):
    temp = list()
    for j in range(cols):
        temp.append(int(input()))
    mat_2.append(temp)

# Creating an empty matrix
for i in range(rows):
    temp = list()
    for j in range(cols):
        temp.append(0)
    sum_mat.append(temp)

for k in range(rows):
    for l in range(cols):
        sum_mat[k][l] = mat_1[k][l] + mat_2[k][l]

print("\nSum of Matrices is:")
for i in range(rows):
    for j in range(cols):
        print(sum_mat[i][j], end=" ")
    print()

# Q6
print("Enter total number of students: ")
total = int(input())

stud = list()

print(">>>INPUT STUDENT DETAILS<<<")
for i in range(total):
    print("\nStudent", i + 1, ":")
    temp = list()
    print("Enter Name:")
    temp.append(input())
    print("Enter Roll no.:")
    temp.append(input())
    print("Enter GPA:")
    temp.append(float(input()))

    stud.append(temp)

print("\nStudent details Saved\n")
print(">>STUDENT DETAILS<<")
print("Name\t\tRoll no.\t\t\tGPA")

for i in range(total):
    if stud[i][2] > 3.5:
        for j in range(3):
            print(stud[i][j], end="\t\t\t")
        print("\n")

s = set()