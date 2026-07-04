class room:
    def __init__(self,room_no):
        self.room_no=room_no
        self.booked=False
    def book(self):
        if not self.booked:
            self.booked=True
            print("room booked")
        else:
            print("room already booked")
    def cancel(self):
        self.booked=False
        print("room cancelled")
    def display(self):
        print("room no: ",self.room_no)
        print("booked:",self.booked)
r1=room(101)
r1.book()
r1.cancel()
r1.display()       
        