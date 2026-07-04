class bus:
    def __init__(self,bus_no,seats):
        self.bus_no=bus_no
        self.available=seats
    def reserve(self,seats):
        if seats<=self.available:
            self.available-=seats
            print("seats reserved")
    def cancel(self,seats):
        self.available+=seats
        print("seats cancelled")
    def display(self):
        print("bus no: ",self.bus_no)
        print("available_seats: ",self.available)
b1=bus(1023,60)   
b1.reserve(53) 
b1.display()
b2=bus(1542,21)   
b2.cancel(10)
b2.display()