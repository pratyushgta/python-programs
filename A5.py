# Q1
def fibo(n):
    firstTerm = 0
    secondTerm = 1

    for i in range(1, n + 1):
        print(firstTerm)

        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm


T = int(input("Enter number of terms: "))
fibo(T)


# Q2
def prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


T = int(input("Enter number of terms: "))

for j in range(1, T + 1):
    if prime(j):
        print(j, end=" ")


# Q3
def mult(n, x):
    if x > 10:
        return
    print(n, "*", x, "=", n * x)
    return mult(n, x + 1)


T = int(input("Enter the number to find multiples of: "))
mult(T, 1)


# Q4
def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        print(n, "is a Perfect number!")
    else:
        print(n, "is Not a Perfect number!")


T = int(input("Enter any number: "))
perfect(T)


# Q5
def sum(l):
    sum = 0
    for i in l:
        sum += i

    if prime(sum):
        print("Sum is prime!")
    else:
        print("Sum is not prime!")


def prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


T = int(input("Enter total elements in a list: "))
lst = list()
print("Enter", T, "elements:")
for j in range(T):
    lst.append(int(input()))
sum(lst)


# Q6
def lowerTriangle(mat, size):
    for m in range(size):
        for n in range(size):
            if m < n:
                print("0", end=" "),
            else:
                print(mat[m][n], end=" "),

        print("")


n = int(input("Enter the size of matrix:"))
matrix = list()

print("Enter", n * n, "values: ")

for i in range(n):
    temp = list()
    line = input().split()
    for j in line:
        temp.append(int(j))
    matrix.append(temp)

lowerTriangle(matrix, n)


# Q7
def total(m):
    sum = 0
    for i in m:
        sum += i

    return sum


def avg(m):
    average = total(m) / len(m)
    return average


def max_min(m):
    sorted(m)
    print("Max marks: ", m[len(m) - 1])
    print("Min marks: ", m[0])


name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

marks = list()
for i in range(5):
    print("Enter marks in subject", i + 1, ":")
    marks.append(int(input()))

print(">>>STUDENT DETAILS<<<\nName:", name, "\nRoll No.:", roll)
print("\nTotal marks: ", total(marks))
print("Average marks: ", avg(marks))
max_min(marks)
