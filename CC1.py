# ASSIGNMENT PROBLEMS

#Q1
R, O, C = input("").split()

rem = 20 - int(O) #runs remaining
possible = rem * 6 * 6 #maximum score that can be achieved

total = int(C) + possible #max total score

if total > int(R):
    print("YES")
else:
    print("NO")


#Q2
T = int(input(""))
ans = list()

while T != 0:
    A, B, C, D = input("").split()
    if int(A) + int(C) and int(B) + int(D) == 180:
        rep = "YES"
    else:
        rep = "NO"
    T-=1
    ans.append(rep)
    rep=""

for i in ans:
    print(i)


# PRACTICE PROBLEMS

# ATM
try:
    n, atm = input("").split()
    n = int(n)
    atm = float(atm)
    if (n + 0.5 <= atm and n % 5 == 0):
        print(atm - n - 0.5)
    else:
        print(atm)

except EOFError as e:
    print(e)

# Miami GP
T = int(input())
while (T > 0):
    X, Y = map(int, input().split())

    if (((107 * X) / 100) >= Y):
        print("YES")
    else:
        print("NO")

    T = T - 1

# Enormous Input
(n, k) = map(int, input().split(' '))

ans = 0

for i in range(n):
    x = int(input())
    if x % k == 0:
        ans += 1

print(ans)

# Finding Square Roots
import math
t=int(input())
for i in range(t):
    n=int(input())
    print(int(math.sqrt(n)))

# Mahasena
try:
    T = input()
    A = list()
    even = 0
    odd = 0

    X = input().split()

    #while T > 0:

     #   A.append(input())
      #  T = T - 1


    for i in range(int(T)):
        if int(X[i]) % 2 == 0:
            even += 1
        else:
            odd += 1

    if even>odd:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")

except EOFError as e:
    print(e)


