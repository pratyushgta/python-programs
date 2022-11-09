stack = []
size = 100
top = -1

push_counter = 0
pop_counter = 0


def push(ch, n):
    if top > (size - 1):
        return "Overflow"
    else:
        stack[++top] = int(ch)
        return "true"


def pop(ch, t):
    if t <= -1:
        return "Underflow"
    elif ch == ')' and stack[-1] == '(' or ch == '}' and stack[-1] == '{' or ch == ']' and stack[-1] == '[':
        t -= 1
        return "true"
    else:
        return "false"


over_under = False
T = int(input())
while T != 0:
    str = input()

    for i in str:
        if i == '(' or i == '{' or i == '[':
            rs = push(i, push_counter)

            if rs == 'Overflow':
                over_under = True
                print("0")
            elif rs == 'true':
                push_counter += 1
                continue

        elif i == ')' or i == '}' or i == ']':
            r = pop(i, top)
            if r == 'Underflow':
                over_under = True
                print("0")
                break
            elif r == "false":
                print("0")
                break
            elif r == "true":
                pop_counter += 1

if push_counter == 0:
    print("0")
elif pop_counter == push_counter and over_under == False:
    print("1")
elif push_counter < pop_counter or push_counter > pop_counter:
    print("0")
