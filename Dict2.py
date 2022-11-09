aircraft = dict()

n = int(input("Enter values: "))

while n > 0:
    number = "Aircraft"+str(n)
    model = input("Enter mode no.: ")
    capacity = int(input("Enter seat capacity: "))
    aircraft[number] = model, capacity
    n = n - 1

print(aircraft)

for x in aircraft:
    print("model:",aircraft.values)

