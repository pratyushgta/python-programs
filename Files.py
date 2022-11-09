# Use words.txt as the file name
fname = input("Enter file name: ")
fh = input(fname)

for i in fh:
    line = i.rstrip()
    print(line.upper())


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
pointer = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    pointer = float(line[line.find(':')+1:len(line)])+pointer
    count = count+1

total = pointer / count
print("Average spam confidence:",total)

