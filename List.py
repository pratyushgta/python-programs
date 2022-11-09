# fname = input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst = list()
for line in fh:
    sp = line.rstrip().split()
    if not line.startswith('From '):
        continue

    lst.append(sp[1])
    print(sp[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
