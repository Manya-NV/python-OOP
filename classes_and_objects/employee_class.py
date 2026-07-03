class employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def display(self):
        print(f"{self.name} is {self.position} has salary of {self.salary} per year")
employee1=employee("manya","software engineer","6LPA")
employee2=employee("MOULYA","security engineer","5LPA")  
employee1.display()
employee2.display()