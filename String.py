#*
# str1 = "Hello"
# str2 = 'there
# bob = str1 + str2
# print(bob)
# print(dir(bob))

text = "X-DSPAM-Confidence:    0.8475"
f = text[text.find('0'):text.find('5')+1]
print(float(f))
