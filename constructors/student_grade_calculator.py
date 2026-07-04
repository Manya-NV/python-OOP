class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print("Grade A")
        elif self.marks>=80:
            print("Grade B")
        elif self.marks>=80:
            print("Grade C+")
        else:
            print("Grade C")
s1=student("manya",90)
s2=student("moulya",80) 
s1.grade()       
s2.grade()