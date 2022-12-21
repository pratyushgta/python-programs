import math
import random

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        return 1
    else:
        return 0


def ramanujan(n):
    cubes = dict()
    i = 1
    while i * i * i <= n:
        cubes[i * i * i] = i
        i += 1

    for j in cubes:
        first = j
        second = n - j

        if second in cubes:
            return 1
    return 0



T = int(input("Enter percentage of marks: "))

if T < 50:
    room_no = list()
    check = 0
    for i in range(1, 500 + T):
        r = perfect(i)
        if r == 1:
            room_no.append(i)
            check = check + 1

    if check > 0:
        # print("Room number alloted: ", random.choice(room_no))
        print("Room number alloted: ", room_no)
    else:
        print("No room alloted")

elif T > 50:
    room_no = list()
    check = 0
    for i in range(500 + T, 1000):
        r = ramanujan(i)
        if r == 1:
            room_no.append(i)
            check = check + 1

    if check > 0:
        # print("Room number alloted: ", random.choice(room_no))
        print("Room number alloted: ", room_no)
    else:
        for i in range(500 + T, 1000):
            sr = int(math.sqrt(i))
            if (sr * sr) == i:
                room_no.append(i)
        #print("Room number alloted: ", random.choice(room_no))
        print("Room number alloted: ", room_no)
