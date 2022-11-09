# Q1
s = {1, 2, 3, 4, 5, 6}
s2 = set([5, 6, 7, 8])

print("Before Removing: ", s)
s.remove(3)
print("After Removing: ", s)
print("Union: ", s.union(s2))
print("Intersection: ", s.intersection(s2))
print("Difference: ", s.difference(s2))

# Q2
str = input()
s = (str.lower()).replace(" ", '')
print(s)
unique_lst = list()
lst = list()
for i in s:
    lst.append(i)
    if i not in unique_lst:
        unique_lst.append(i)

student = dict()
for i in unique_lst:
    student[i] = lst.count(i)
print(student)

# Q3
comb_dict = dict()

n = int(input("Enter total no. of dictionaries to add: "))
x = 1

for i in range(n):
    dct = dict()
    print(">>>DICT", i + 1, "<<<<")
    for j in range(2):
        value = input("Enter value: ")
        dct[x] = value
        x += 1

    comb_dict = comb_dict | dct

print("\n>>Combined Dictionary<<")
print(comb_dict)

# Q4
dct = dict()

n = int(input("Enter total no. of dictionaries to add: "))
x = 1

for i in range(n):
    dct[x] = x * x
    x += 1

print(">>Dictionary<<")
print(dct)

# Q5
customer_details = {
    "1001": "John",
    "1004": "Jill",
    "1005": "Joe",
    "1003": "Jack"
}

# Details of customers
print(">>Customer Details<<")
for key, value in customer_details.items():
    print("\nID:", key)
    print("Customer name:", value)

# Number of customers
print("\nCount of customers: ")
count = 0
for key in customer_details.keys():
    count += 1
print("Total customers:", count)

# Customer names in ascending order
print("\nCustomer names in ascending order: ")
lst = list()
for names in customer_details.values():
    lst.append(names)
lst.sort()
print(lst)

# Deletion
customer_details.pop("1005")
print("\nUpdated dictionary: ")
print(customer_details)

# Updation
customer_details.update({'1003': "Mary"})
print("\nUpdated dictionary: ")
print(customer_details)

# Check
check = 0
for key in customer_details.keys():
    if key == '1002':
        check = 1
        break

if check == 1:
    print("\nCustomer ID= 1002 exists!")
else:
    print("\nCustomer ID= 1002 does not exist!")

# Q6
student = dict()

for i in range(3):
    name = input("Enter student name: ")
    marks = list()
    print("Enter marks of 2 subjects")
    for j in range(2):
        marks.append(int(input()))
    student[name] = marks

print(">>STUDENT DETAILS<<")
print(student)

x = input("\nEnter the key to search: ")

if x in student:
    print("\nKey exists in the dictionary")
else:
    print("\nKey does not exist in the dictionary")

# Q7
java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}

print("Total students in Python:", len(python_course))
print("Total students in Java ONLY:", len(java_course - python_course), java_course - python_course)
print("Total students in Python ONLY:", len(python_course - java_course), python_course - java_course)
print("Students in both courses:", len(java_course & python_course), java_course & python_course)
print("Students in either course but not both:", len(java_course ^ python_course), java_course ^ python_course)
print("Students in either courses:", len(java_course | python_course), java_course | python_course)
