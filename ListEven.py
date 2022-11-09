t = int(input("Enter number of lists: "))
lst = list()
list2 = list()

print("Enter", t, "lists")
while t > 0:
    print("Enter 2 elements: ")
    temp = list()
    temp.append(int(input()))
    temp.append(int(input()))

    lst.append(temp)
    t = t - 1

print("List with both even numbers: ")
for i in lst:
    counter = 0
    for j in i:
        if j % 2 != 0:
            counter = 1
            break
    if counter == 0:
        print(i)

print("List with 1st val > 2nd val: ")
for i in lst:
    counter = 0
    if i[0] > i[1]:
        print(i)