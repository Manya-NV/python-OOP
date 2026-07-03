class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def comparision(self,other):
        if self.price > other.price:
            print(f"{self.brand} is expensive")
        elif self.price < other.price:
            print(f"{other.brand} is expensive")
        else:
            print("both laptops are of same price")
l1=laptop("dell",110000)
l2=laptop("hp",17899)
l1.comparision(l2)
        