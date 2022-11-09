# ASSIGNMENT QUESTIONS

#ICPC Balloons
T = int(input())

while T > 0:
    N = int(input())
    A = [int(i) for i in input().split()]
    temp = []
    for i in range(N):
        for j in range(1, 8):
            if A[i] == j:
                temp.append(i + 1)

    print(max(temp))
    T -= 1


#Chef and IPC Certificates
N, M, K = input().split()
cert_counter = 0
N = int(N)
M = int(M)
K = int(K)

while N > 0:
    stud_details = [int(i) for i in input().split()]
    sum = 0
    ques_asked = stud_details[K]
    for i in range(0, K):
        sum += stud_details[i]

    if sum >= M and ques_asked <= 10:
        cert_counter += 1

    N -= 1

print(cert_counter)




# PRACTICE QUESTIONS

#Practice makes us perfect
P1, P2, P3, P4 = input("").split()
counter = 0

if int(P1) >= 10:
    counter = counter + 1
if int(P2) >= 10:
    counter = counter + 1
if int(P3) >= 10:
    counter = counter + 1
if int(P4) >= 10:
    counter = counter + 1

print(counter)


#Small Factorials
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
for i in range(n):
    num=int(input())
    print(factorial(num))


#Problems in your to-do list
T = int(input())
lst = list()
while T > 0:
    N = int(input())
    lst = [int(i) for i in input().split()]

    counter = 0

    for i in lst:
        if i >= 1000:
            counter += 1

    print(counter)

    T -= 1


#The Lead Game
T = int(input())
p1 = 0
p2 = 0
max_p1 = [0]
max_p2 = [0]

while T > 0:
    Si, Ti = input().split()
    Si = int(Si)
    Ti = int(Ti)

    p1 += Si
    p2 += Ti

    if p1 >= p2:
        max_p1.append(p1 - p2)
    elif p2 > p1:
        max_p2.append(p2 - p1)
    T -= 1

if max(max_p1) >= max(max_p2):
    print("1", max(max_p1))
elif max(max_p2) > max(max_p1):
    print("2", max(max_p2))


#Recent contest problems
T = int(input())

while T > 0:
    N = int(input())
    lst = [i for i in input().split()]

    counter1 = 0
    counter2 = 0

    for i in lst:
        if i == "START38":
            counter1 += 1
        else:
            counter2 += 1

    print(counter1, counter2)

    T -= 1

