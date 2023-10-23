def pour_water(jug_a, jug_b, max1, max2, fill):
    print("%d\t\t%d" % (jug_a, jug_b))
    if jug_b == fill:
        return
    elif jug_b == max2:
        pour_water(jug_a, 0, max1, max2, fill)
    elif jug_a != 0 and jug_b == 0:
        pour_water(0, jug_a, max1, max2, fill)
    elif jug_a == fill:
        pour_water(0, jug_b, max1, max2, fill)
    elif jug_a < max1:
        pour_water(max1, jug_b, max1, max2, fill)
    elif jug_a <= (max2 - jug_b):
        pour_water(0, jug_a + jug_b, max1, max2, fill)
    else:
        pour_water(jug_a - (max2 - jug_b), max2, max1, max2, fill)

print("JUG A \t JUG B")
max1, max2, fill = 5, 7, 4
pour_water(0, 0, max1, max2, fill)