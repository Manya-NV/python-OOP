class bill:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def cal_bill(self):
        bill=self.price*self.quantity
        return bill
name=input("enter the name of the product: ") 
price=int(input("enter price of the product: ")) 
quantity=int(input("enter the quantity in kg ")) 
p1=bill(name,price,quantity)
print(p1.cal_bill())    
name=input("enter the name of the product: ") 
price=int(input("enter price of the product: ")) 
quantity=int(input("enter the quantity in kg ")) 
p2=bill(name,price,quantity)
print(p2.cal_bill())  