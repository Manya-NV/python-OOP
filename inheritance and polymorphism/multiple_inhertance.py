#online course management
class student:
    def __init__(self,name):
        self.name=name
    def student_info(self):
        print("student name: ",self.name)
class course:
    def __init__(self,course_name):
        self.course_name=course_name
    def course_info(self):
        print("course name: ",self.course_name)
class enrollment(student,course):
    def __init__(self,name,course_name,fee):
        student.__init__(self,name)
        course.__init__(self,course_name)
        self.fee=fee
    def display(self):
        print("\n enrollment details")
        self.student_info()
        self.course_info()
        print("course fee: ",self.fee)
e=enrollment("manya","python",3450)
e.display()
        
        