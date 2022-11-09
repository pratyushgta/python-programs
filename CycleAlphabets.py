def reverse(char, num):
    asc = ord(char)

    new_char = asc - num

    if asc <= 90 and new_char < 65:
        diff = 65 - new_char
        new_char = 90 - diff + 1
        return chr(new_char)
    elif asc <= 122 and new_char < 97:
        diff = 97 - new_char
        new_char = 122 - diff + 1
        return chr(new_char)
    else:
        return chr(new_char)


s = input("Enter a string: ") # can also use tuples
n = int(input("Enter a number: "))

word_lst = list(s)
new_word = ""
for i in s:
    new_word += reverse(i, n)
print("New word: ", new_word)
