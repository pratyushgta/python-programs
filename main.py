# Q3
class bill:
    def __init__(self):
        self.product = list()

    def readproduct_info(self):
        print(">> INPUT PRODUCT INFO <<\nEnter space separated Prod_id, Prod_name, Prod_price")
        for i in range(3):
            s = input(">> \n").split(" ")
            temp = tuple(s)
            self.product.append(temp)

    def printproductinfo(self):
        id = int(input("\nEnter product id to view its info: "))
        for i in self.product:
            if int(i[0]) == id:
                print(i)


class customerbill(bill):
    def __init__(self):
        super().__init__()
        super().readproduct_info()
        super().printproductinfo()

    def customerbill(self):
        print("\n>> GENERATE BILL << ")
        idx = int(input("Enter product id: "))
        qty = int(input("Enter quantity: "))

        price = 0
        for i in self.product:
            if int(i[0]) == idx:
                price = int(i[2])

        amt = price * qty
        total = (15 / 100) * amt + amt
        if total > 800:
            total = (12 / 100) * total - total

        print("\nTotal: ", total)


ob = customerbill()
ob.customerbill()