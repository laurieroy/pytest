class Checkout:
    class Discount:
        def __init__(self, numberItems, price):
            self.numberOfItems = numberItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}




    def addDiscount(self, item, numberOfItems, price):
        discount = self.Discount(numberOfItems, price)
        self.discounts[item] = discount


    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.prices[item] * count
        return total

