#school management system
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no
class graduate_student(student):
    def __init__(self, name, age, roll_no,marks):
        super().__init__(name, age, roll_no)
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=70:
            return "B"
        else:
            return "C"
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Roll no: ",self.roll_no)
d=graduate_student("manya",21,60,80)
d.display()
print("garde:",d.grade())


