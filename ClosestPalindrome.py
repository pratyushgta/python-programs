def palindrome(num):
    lst = list(num)
    num_list = lst
    lst.reverse()
    if lst == num_list:
        return True
    else:
        return False

def closest(n):
    max = n+1
    min = n-1
    while not palindrome(max):
        max = max+1

    while not palindrome(min):
        min = min-1

    if n-min < n-max:
        return n-min
    else:
        return n-max

num = 121
print(closest(num))


