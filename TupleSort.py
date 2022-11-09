n = int(input("Enter no. of list: "))
tup = tuple()
lst = list()
for i in range(n):
    print(">>LIST", i + 1, "<<")
    x = int(input("Enter no. of elements in tuple: "))
    print("Enter", x, "elements")
    temp = list()
    while x > 0:
        temp.append(int(input()))
        x = x - 1
    tup = tuple(temp)
    lst.append(tup)

print(lst)

t = list()
for i in range(len(lst)):
    temp = lst[i]
    a_sort = tuple(sorted(temp, reverse=False))
    d_sort = tuple(sorted(temp, reverse=True))

    if a_sort == temp or d_sort == temp:
        continue
    else:
        t.append(lst[i])

lst = t
print(lst)
