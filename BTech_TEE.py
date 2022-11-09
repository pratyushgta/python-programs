# Q1
L1 = list()
L2 = list()


def F1():
    for i in range(5):
        s = input("Enter a pair: ")
        tup = tuple(s)

        L1.append(tup)

    for i in range(len(L1)):
        if i % 2 == 0:
            L2.append(L1[i])

    print("OG L1= ", L1, "\nEVEN L2= ", L2)
    F2()


def F2():
    print("PRIME F2= ")
    counter = 0
    for i in range(len(L2)):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    print(L2[i])
                    counter += 1

    if counter == 0:
        print("Null set")


F1()


# Q2 a
def create():
    open("file1.txt", "w")
    print("\nNew text file created!")
    read()


def read():
    f = open("file1.txt", "a")
    print("Enter 10 sentences:\n")
    for i in range(5):
        s = input()
        f.write(s)
        f.write("\n")
    print("\nSentences inserted!")
    f.close()
    # process()


def process():
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt", "a")

    for lines in f1.readlines():
        fist_word = lines.split()
        if fist_word[0].startswith("A") or fist_word[0].startswith("B") or fist_word[0].startswith("C"):
            f2.write(lines)
            f2.write("\n")

    print("\nSentences Processed!")
    # display()


def display():
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt", "r")
    print(">>FILE 1 CONTENTS<<\n", f1.read())
    print(">>FILE 2 CONTENTS<<\n", f2.read())


# create()

##### MENU NOT REQUIRED | Uncheck above comments and remove whole while condition
while True:
    print("\n>>>>MENU<<<<")
    print("1. Read")
    print("2. Process")
    print("3. Display")
    choice = int(input("Enter choice: "))

    if choice == 1:
        read()
    elif choice == 2:
        process()
    elif choice == 3:
        display()

# Q2 b
tup = tuple(map(int, input("Enter space separated integers: ").split(" ")))
print(tup, type(tup))

even = filter(lambda a: a % 2 == 0, tup)
odd = filter(lambda b: b % 2 != 0, tup)

L2 = list(even)
L3 = list(odd)

print("Tuple:", tup, "\nL2:", L2, "\nL3:", L3)


# Q3
class bill:
    def __init__(self):
        self.product = list()

    def readproduct_info(self):
        print(">> INPUT PRODUCT INFO <<\nEnter space separated Prod_id, Prod_name, Prod_price")
        for i in range(3):
            s = input(">> \n").split(" ")
            temp = tuple(s)
            self.product.append(temp)

    def printproductinfo(self):
        id = int(input("\nEnter product id to view its info: "))
        for i in self.product:
            if int(i[0]) == id:
                print(i)


class customerbill(bill):
    def __init__(self):
        super().__init__()
        super().readproduct_info()
        super().printproductinfo()

    def customerbill(self):
        print("\n>> GENERATE BILL << ")
        idx = int(input("Enter product id: "))
        qty = int(input("Enter quantity: "))

        price = 0
        for i in self.product:
            if int(i[0]) == idx:
                price = int(i[2])

        amt = price * qty
        total = (15 / 100) * amt + amt
        if total > 800:
            total = (12 / 100) * total - total

        print("\nTotal: ", total)


ob = customerbill()
ob.customerbill()



# Q4
import pandas as pd

data = pd.read_csv("C:/Users/praty/Desktop/winequality.csv")

# a
print(data.head(10))

# c
print(">> Colum names: ")
for col in data.columns:
    print(col)

# c
print(data.info())

# d
s = sum(data["density"])
me = data["density"].mean()
mo = data["density"].mode()
print("Sum is: ", s, "\nMean is: ", me, "\nMode is: ", mo)

# e
min = data["pH"].min()
max = data["pH"].max()
print("Min:", min, "\nMax:", max)

# f
data["total_density_pH"] = data['density'] + data['pH']
print(data["total_density_pH"].head())

# g
df = data.copy()
df.rename(columns={"sulphates": "sulph", "alcohol": "alco", "chlorides": "chlor"}, inplace=True)
print(df["sulph"])


# Q5
import mysql
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='ayush@31', port='3306')

if conn.is_connected():
    print("Connected")
else:
    print("Not Connected")

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS University")

mydb = sql.connect(host='localhost', user='root', passwd='ayush@31', port='3306', database='University',
                   autocommit=True)

if mydb.is_connected():
    print("Connected")
else:
    print("Not Connected")

# Creating table
mycursor = mydb.cursor()
sql = 'create table Programme_Info(program_id int primary key, program_name varchar(20), campus_name varchar(20))'
mycursor.execute(sql)
print("Table Created")

sql2 = 'create table Course_Info(course_id int primary key, course_name varchar(20))'
mycursor.execute(sql2)
print("Table Created")

# Insert into Programme Info
for i in range(5):
    print("\nProgramme Info", i + 1)
    idx = int(input("Enter program ID: "))
    name = input("Enter program name: ")
    camp = input("Enter campus name: ")

    sql3 = 'insert into Programme_Info values(%s,%s,%s)'
    d = (idx, name, camp)
    mycursor.execute(sql3, d)

print("Programe Info values inserted")

# Insert into Course name
for i in range(5):
    print("\nCourse Info", i + 1)
    idx = int(input("Enter course ID: "))
    name = input("Enter course name: ")

    sql4 = 'insert into Course_Info values(%s,%s)'
    d = (idx, name)
    mycursor.execute(sql4, d)

print("Programe Info values inserted")

# Display from course info
sql5 = 'select * from Course_Info where course_name="Python"'
mycursor.execute(sql5)
record = mycursor.fetchall()

##print(tabulate.tabulate(record,headers=['ID','Programe Name','Location'],tablefmt='psql'))

for i in record:
    print(i)

# Display all
sql5 = 'select * from Programme_Info'
sql6 = 'select * from Course_Info'
mycursor.execute(sql5)
record = mycursor.fetchall()

print("\n\nPROGRAMME INFO")
##print(tabulate.tabulate(record,headers=['ID','Programe Name','Location'],tablefmt='psql'))

for i in record:
    print(i)

mycursor.execute(sql6)
record = mycursor.fetchall()

print("\n\nCOURSE INFO")
##print(tabulate.tabulate(record,headers=['ID','Course Name'],tablefmt='psql'))
for i in record:
    print(i)







