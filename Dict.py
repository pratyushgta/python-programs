name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle:
    sp = line.rstrip().split()
    if not line.startswith('From '):
        continue

    d[sp[1]] = d.get(sp[1], 0) + 1

biggestWord = None
biggestCount = None
for word,count in d.items():
    if biggestCount is None or count > biggestCount:
        biggestWord = word
        biggestCount = count

print(biggestWord,biggestCount)




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
