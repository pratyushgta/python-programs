num = input("Enter a number: ")
num_lst = list(num)
cum_sum = list()
for i in range(1, len(num) + 1):
    sum = 0
    for j in range(i):
        sum += int(num_lst[j])
    cum_sum.append(sum)

print(cum_sum)
