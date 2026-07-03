class movie:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def display(self):
        print(f"{self.name} movie has {self.ratings} ratings")
m1=movie("gaja",7)
m2=movie("milana",10)
m1.display()
m2.display()