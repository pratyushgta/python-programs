"""
 * This file contains client-side code that connects to the server and calls the calculator methods remotely
 * DC-E4
 *
 * @author Pratyush Kumar (github.com/pratyushgta)
"""
import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:6363")

print(">> SIMPLE CALCULATOR <<", "\n-> Input:")
num1 = int(input("Enter no. 1: "))
num2 = int(input("Enter no. 2: "))

print("\n-> Results:")
print(num1, "+", num2, "=", server.add(num1, num2))
print(num1, "-", num2, "=", server.subtract(num1, num2))
print(num1, "*", num2, "=", server.multiply(num1, num2))
