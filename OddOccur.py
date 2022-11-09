n = int(input("Enter no. of students: "))
lst = list()
for i in range(n):
    lst.append(str(input("Enter name: ")))
lst2 = list()

for i in lst:
    if i not in lst2:
        lst2.append(i)

for i in range(len(lst2)):
    counter = 0
    name = lst2[i]
    for j in range(n):
        if lst2[i] in lst[j]:
            counter = counter + 1
    if counter % 2 != 0:
        print(name)
