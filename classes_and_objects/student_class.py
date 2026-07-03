class student:
    def __init__(self,name,marks,grade):
        self.name=name
        self.marks=marks
        self.grade=grade
    def display(self):
        print(f"{self.name} has scored {self.marks} and got {self.grade} grade")
student1=student("manya",90,"distinction")
student2=student("moulya",80,"excellent")
student1.display()
print()
student2.display()
        