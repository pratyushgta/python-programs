# ASSIGNMENT QUESTIONS

# Balanced String Parentheses
def check(str):
    stack = list()
    for i in str:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')' or i == '}' or i == ']':
            if len(stack) > 0:
                if stack[len(stack) - 1] == '(' and i == ')' or stack[len(stack) - 1] == '{' and i == '}' or stack[len(stack) - 1] == '[' and i == ']':
                    stack.pop()
                else:
                    return "0"
            else:
                return "0"

    if len(stack) == 0:
        return "1"
    else:
        return "0"


T = int(input())
while T != 0:
    s = input()
    r = check(s)
    print(r)
    T -= 1


# Optimal Adjacent Removal
T = int(input())
while T != 0:
    str = input()
    stack = list()

    for i in range(0, len(str)):
        if len(stack) > 0 and stack[-1] == str[i]:
            stack.pop(-1)
        else:
            stack.append(str[i])
    print(len(stack))
    T -= 1



# PRACTICE QUESTIONS

# Sudhanva and Books
Q = int(input())
lst = list()
while Q > 0:
    N = input()
    if N == '-1':
        if len(lst) == 0:
            print("kuchbhi?")
        else:
            print(lst.pop())
    else:
        a, b = N.split()
        lst.append(int(b))

    Q -= 1

# Chefs in Queue
N, K = input().split()
A = list()

for i in input().split():
    A.append(int(i))

st = []
f = 1

for i in range(int(N)):
    while len(st) > 0 and A[i] < A[st[-1]]:
        f = f * (i - st.pop() + 1) % 1000000007
    st.append(i)
print(f)


# Largest Rectangle Area
T = int(input())
while T != 0:
    N = int(input())
    hist = list()
    stack = list()

    max_area = 0

    for i in input().split():
        hist.append(int(i))

    i = 0

    while i < len(hist):
        if (not stack) or (hist[stack[-1]] <= hist[i]):
            stack.append(i)
            i += 1

        else:
            top = stack.pop()
            hist_area = (hist[top] * ((i - stack[-1] - 1) if stack else i))
            max_area = max(max_area, hist_area)

    while stack:
        top = stack.pop()
        hist_area = (hist[top] * ((i - stack[-1] - 1) if stack else i))
        max_area = max(max_area, hist_area)
    print(max_area)

    T -= 1


# Nikhil and Commands
T = int(input())
while T != 0:
    N = int(input())
    stack = list()

    for i in range(N):
        x = input().split()

        if x[0] == 'cd':
            if x[1][0] == '/':
                stack = []
            y = x[1].split('/')
            for j in y:
                if j == '..':
                    stack.pop()
                elif j != '..' and j != '':
                    stack.append(j)
        else:
            if len(stack) == 0:
                print('/')
            else:
                print('/' + '/'.join(stack) + '/')
    print()
    T -= 1

# Compilers and parsers
T = int(input())

while T != 0:
    str = input()
    count = 0
    stack = list()

    sym = 0

    if str[0] == '>':
        print(count)
    else:
        for i in range(len(str)):
            if str[i] == '<':
                sym += 1
            elif str[i] == '>':
                sym -= 1
            if sym == 0:
                count = i + 1
            elif sym < 0:
                break
        print(count)
    T -= 1
