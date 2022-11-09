# This first line is provided for you


def computepay(hrs,rate):
    if float(hrs) > 40:
        extra = float(hrs) - 40
        extra_pay = 1.5 * float(rate) * extra
        total = 40 * float(rate) + extra_pay
    else:
        total = float(hrs) * float(rate)

    return total



h = float(input("Enter Hours:"))
r = float(input("Enter rate per hour:"))
result=computepay(h,r)
print("Pay",result)

