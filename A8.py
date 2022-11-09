import os.path
import time


def create():
    open("studentData.txt", 'w')
    print("\nNew text file created!")
    read()


def read():
    if not os.path.exists("studentData.txt"):
        print("\nText file does not exist. Creating a new file...")
        create()
    else:
        x = int(input("\nEnter no. of names to insert: "))
        f = open("studentData.txt", "a")
        for i in range(x):
            n = input("Enter student name: ")
            f.writelines(n)
            f.writelines("\n")
        print("\nNames inserted!")
        f.close()


def display():
    f = open("studentData.txt", "r")
    print(f.read())


def display_index():
    f = open("studentData.txt", "r")
    index = int(input("\nEnter the student number you want to retrieve: "))
    str = f.read().split()

    if index > len(str):
        print("\nName at given position does not exist!")
    else:
        for i in range(len(str)):
            if i == index - 1:
                print(str[i])
    f.close()


def display_string():
    f = open("studentData.txt", "r")
    name = input("\nEnter name of student to retrieve: ")
    str = f.read().split()
    check = 0
    ## METHOD 1
    if name in str:
        print("Exists")
    else:
        print("Does not exist")
    ## METHOD 2
    for i in str:
        if i == name:
            print(i)
            check = 1

    if check == 0:
        print("\n", name, "does not exist in the file!")

    f.close()


def total():
    f = open("studentData.txt", "r")
    str = f.read().split()
    print("\nTotal names in the file: ", len(str))
    f.close()


def total_char():
    f = open("studentData.txt", "r")
    print("\nTotal no. of characters in file: ", len((f.readlines())))
    f.close()


def M_names():
    f = open("studentData.txt", "r")
    str = f.read().split()
    count = 0
    for i in str:
        if i.startswith("M"):
            count += 1

    print("\nTotal no. of names starting with M:", count)

    f.close()


def clear():
    # open("studentData.txt", "w").close()
    os.remove("studentData.txt")
    print("\nAll data has been erased!")


while True:
    print("\n>>>>MENU<<<<")
    print("1. Input")
    print("2. Display")
    print("3. Display name @ index")
    print("4. Display particular student")
    print("5. Total names")
    print("6. Total characters")
    print("7. Count of names starting with 'M'")
    print("8. EXIT")
    print("9. ***Erase data***")
    choice = int(input("Enter choice: "))

    if choice == 1:
        read()
    elif choice == 2:
        display()
    elif choice == 3:
        display_index()
    elif choice == 4:
        display_string()
    elif choice == 5:
        total()
    elif choice == 6:
        total_char()
    elif choice == 7:
        M_names()
    elif choice == 9:
        clear()
    elif choice == 8:
        exit("Goodbye!")