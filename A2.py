a = 5
for i in range(0, a):
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

# Q1
import math

for i in range(1, 100):
    num = i
    sumx = 0
    while num > 0:
        digit = num % 10
        sumx = sumx + math.factorial(digit)
        num = num // 10

    if sumx == i:
        print(i, "is a Strong Number")
# Q2
lst = list()
print("Enter total number of list elements: ")
total = int(input())
print("Enter", total, "elements")

while total > 0:
    lst.append(int(input()))
    total = total - 1

print("Enter the element to search: ")
search = int(input())
print(search)

counter = 0

for i in range(len(lst)):
    if lst[i] == search:
        print("Found!")
        counter = 1

if counter == 0:
    print("Not Found!")
# Q3
print("Enter total number of terms: ")
terms = int(input())

first = 0
second = 1

for i in range(0, terms):
    print(first, end=" ")
    nextTerm = first + second
    first = second
    second = nextTerm

# Q4
print("Enter a noomber: ")
n = int(input())
rev = " "
while n > 0:
    digit = n % 10
    rev += str(digit)
    n = n // 10

print("Reversed number: ", rev)

# Q5
print("Enter n: ")
n = int(input())
print("Boneless Chicken")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

# Q6
for i in range(5, 0, -1):
    for k in range(i, 6):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("")

# Q7
print("Enter total number of subjects: ")
n = int(input())
total_marks = n * 100
print("Enter", n, "marks")

total = 0
while n > 0:
    x = int(input())

    if x < 0 or x > 100:
        print("Invalid marks")
        continue
    else:
        total += x
        n = n - 1

p = (total / total_marks) * 100

if p >= 92:
    print("Merit")
elif 75 <= p <= 91:
    print("Distinction")
elif 60 <= p <= 74:
    print("First class")
elif 45 <= p <= 59:
    print("Second class")
else:
    print("Fail")
