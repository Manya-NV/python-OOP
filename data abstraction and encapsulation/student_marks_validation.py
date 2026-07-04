class student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,marks):
        if 0<marks<100:
            self.__marks=marks
            print(self.__marks)
        else:
            print("marks should be between 1 to 100")
    def get_marks(self):
        return self.__marks
s=student()
s.set_marks(80)
s.get_marks()
