name = "mbox-short.txt"
handle = open(name)

d = dict()
lst = list()

for line in handle:
    sp = line.rstrip().split()
    if not line.startswith('From '):
        continue

    s1 = sp[5].split(':')
    s2 = s1[0]
    d[s2] = d.get(s2, 0) + 1



for v,k in d.items():
    newtup = (v,k)
    lst.append(newtup)

lst.sort()

for x,y in lst:
    print(x,y)



