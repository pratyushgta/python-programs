t = int(input("Enter number of elements to add: "))
list1 = list()
list2 = list()

print("Enter", t, "elements")
while t > 0:
    list1.append(int(input()))
    t = t - 1
for i in list1:
    temp = tuple()
    temp = temp + (str(i), str(i ** 3),)
    # temp = temp + (str(i**3),)

    list2.append(temp)

print(list2)
