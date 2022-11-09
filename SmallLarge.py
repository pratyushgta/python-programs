'''largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None or smallest is None:
        largest = n
        smallest = n
    elif n > largest:
        largest = n
    elif n < smallest:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)

fname = input("Enter file name: ")
fh = input(fname)
lst = list()
for line in fh:
    sp = line.rstrip().split()
    for i in sp:
        if not i in lst:
            lst.append(i)

lst.sort()
print(lst)'''

# Q1
'''no1 = int(input("Enter no. 1 "))
no2 = int(input("Enter no. 2 "))
no3 = int(input("Enter no. 3 "))
no4 = int(input("Enter no. 4 "))
no5 = int(input("Enter no. 5 "))

sum = no1+no2+no3+no4+no5

avg=sum/5

if sum<100:
    print("True")
else:
    print("False")'''

# Q2
'''import math

r = int(input("Enter radius: "))
area = math.pi * r * r

print("Area is: ", area)'''

# Q3 a
'''a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

add = a + b
dif = b - a
prod = a * b
div = b/a

print(">>>>CALCULATOR<<<<","\nSum: ",add,"\nDifference: ",dif,"\nProduct: ",prod,"\nDivision: ",div)'''

#Q3 b
'''a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

rem = b%a
floor = b//a
power = a**b

print(">>>>OPERATIONS<<<<","\nRemainder: ",rem,"\nFloor Division: ",floor,"\nPower: ",power)'''

#Q3 c
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
age = int(input("Enter Age: "))

print("Age of ", first_name, last_name, " is ", age)
