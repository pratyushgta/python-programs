"""
PATTERN:
2 1
4 3
7 6 5
11 10 9 8
16 15 14 13 12
"""
k = 0
for i in range(1, 6):
    print(end="\n")
    k = k + i
    temp = k
    if i == 1:
        k = k + 1
        print(temp+1, temp, end=" ")
    else:
        for j in range(0, i):
            print(temp, end=" ")
            temp = temp - 1


"""
PATTERN: [FLOYD'S TRIANGLE]
1
2 3
4 5 6
7 8 9 10
"""
k = 1
for i in range(5):
    print(end="\n")
    for j in range(0, i):
        print(k, end=" ")
        k=k+1

"""
PATTERN:
1
1 2
1 2 3
1 2 3 4
"""
k = 0
for i in range(5):
    print(end="\n")
    k = 1
    for j in range(0, i):
        print(k, end=" ")
        k = k+1

"""
PATTERN:
    A 
   B B 
  C	  C	 
 D	   D	 
E	    E	 
 D	   D	 
  C	  C	 
   B B 
    A 
"""
# UPPER TRIANGLE
k = 0
for i in range(6):
    print(end="\n")
    for l in range(6 - i - 1):
        print(' ', end='')

    if i > 2:
        for j in range(0, i):
            if j == 0 or j == i - 1:
                print(chr(i + 64), end=i*" ")
            else:
                print(end=" ")
    else:
        for j in range(0, i):
            print(chr(i + 64), end=" ")

# LOWER TRIANGLE
k = 0
for i in range(4, 0, -1):
    print(end="\n")
    for l in range(6 - i - 1):
        print(' ', end='')

    if i > 2:
        for j in range(0, i):
            if j == 0 or j == i - 1:
                print(chr(i + 64), end=i*" ")
            else:
                print(end=" ")
    else:
        for j in range(0, i):
            print(chr(i + 64), end=" ")


"""
PATTERN:
    A 
   B B 
  C C C 
 D D D D 
E E E E E 
 D D D D 
  C C C 
   B B 
    A 
"""
for i in range(6):
    print(end="\n")
    for l in range(6 - i - 1):
        print(' ', end='')
    for j in range(0, i):
        print(chr(i + 64), end=" ")


for i in range(4,0,-1):
    print(end="\n")
    for l in range(6 - i - 1):
        print(' ', end='')
    for j in range(0, i):
        print(chr(i + 64), end=" ")


"""
PATTERN:
* * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * * 
"""
for i in range(6):
    print(end="\n")
    for j in range(6):
        if i==0 or i==5 or j==0 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")

"""
PATTERN:
A B C D E F 
A         B 
A         B 
A         B 
A         B 
A B C D E F 
"""
ch = ord("A")
for i in range(6):
    print(end="\n")
    temp = ch
    for j in range(6):
        if i == 0 or i == 5:
            print(chr(temp), end=" ")
            temp = temp + 1
        elif j == 0 or j == 5:
            print(chr(temp), end=" ")
            temp = temp + 1
        else:
            print(" ", end=" ")

"""
PATTERN:
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
"""
ch = ord("A")
for i in range(5):
    print(end="\n")
    for j in range(5):
        print(chr(ch), end=" ")
        ch = ch + 1

