import mysql
import pandas as pd
import mysql.connector as sql

conn = mysql.connector.connect(host='localhost', user='root', passwd='ayush@31', port='3306', database='airline')
if conn.is_connected():
    print("Successfully Connected")

def choose_module():
    choice = int(input(">>Choose a module<<\n1. User\n2. Admin\n"))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()


def admin_menu():
    print(">>ADMIN MODULE<<".center(50))
    choice2 = int(input("1. Add pax\n2. Add class\n3. Add route\n"))
    if choice2 == 1:
        passenger()
    #elif choice2 == 2:
        #classtype()
    elif choice2 == 3:
        routes()


def user_menu():
    print(">>USER MODULE<<".center(50))
    choice3 = int(input("1. See routes\n2. Book ticket\n"))
    if choice3 == 1:
        routes()
    elif choice3 == 2:
        passenger()


def routes():
    print(">>Available Routes<<")

    c = conn.cursor()
    c.execute('SELECT * FROM route_details')

    users = c.fetchall()

    for user in users:
        print(user)


def passenger():
    c = conn.cursor()
    n = input("Enter name: ")
    a = input("Enter address: ")
    s = input("Enter source: ")
    d = input("Enter destination: ")


choose_module()

