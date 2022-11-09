## Method 1
lst = [input("Enter a number: ")]
num = ""
reverse = ""

for i in lst:
    num += i
lst.reverse()
for i in lst:
    reverse += i

if int(num) == int(reverse):
    print("Palindrome")
else:
    print("Not palindrome")

## Method 2
lstx = [input("Enter a number: ")]

num_list = lstx
lstx.reverse()

if lstx == num_list:
    print("Palindrome")
else:
    print("Not Palindrome")
