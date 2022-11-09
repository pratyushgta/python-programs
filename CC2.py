# ASSIGNMENT QUESTIONS

# Which Division
try:
    T = int(input())
    lst = list()

    while T > 0:
        R = int(input())
        if 2000 <= R:
            lst.append("1")
        elif 1600 <= R < 2000:
            lst.append("2")
        else:
            lst.append("3")

        T = T-1

    for i in lst:
        print(i)

except EOFError as e:
    print(e)


# Chefland Visa
try:
    T = int(input())
    lst = list()

    while T > 0:
        x1, x2, y1, y2, z1, z2 = input("").split()

        if int(x2) >= int(x1) and int(y2) >= int(y1) and int(z2) <= int(z1):
            lst.append("YES")
        else:
            lst.append("NO")

        T = T-1

    for i in lst:
        print(i)

except EOFError as e:
    print(e)



# PRACTICE QUESTIONS

# Second Largest
try:
    T = int(input())
    sec_max = list()

    while T > 0:
        lst = list()
        a, b, c = input("").split()
        lst.append(int(a))
        lst.append(int(b))
        lst.append(int(c))

        lst.sort(reverse=T)
        sec_max.append(lst[1])
        T = T-1

    for i in sec_max:
        print(i)

except EOFError as e:
    print(e)


# Pass or Fail
try:
    T = int(input())
    result = list()

    while T > 0:
        N, X, P = input("").split()
        N = int(N)
        X = int(X)
        P = int(P)
        total_marks = 3*N

        correct = X*3
        incorrect = (N-X)*1

        marks_obt = correct-incorrect

        if marks_obt >= P:
            result.append("PASS")
        else:
            result.append("FAIL")

        T = T-1

    for i in result:
        print(i)

except EOFError as e:
    print(e)


# Sum OR Difference
try:
    N1 = int(input())
    N2 = int(input())

    if N1 > N2:
       print(N1 - N2)
    else:
        print(N1 + N2)

except EOFError as e:
    print(e)


# Decrement OR Increment
try:
    N = int(input())

    if N % 4 == 0:
        N = N + 1
    else:
        N = N - 1

    print(N)

except EOFError as e:
    print(e)


# Smol Factorial
import math
try:
    T = int(input())
    lst = list()

    while T > 0:
        N = int(input())
        lst.append(math.factorial(N))

        T = T-1

    for i in lst:
        print(i)

except EOFError as e:
    print(e)

