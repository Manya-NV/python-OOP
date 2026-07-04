#employee management system
class employee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id=emp_id
        self.name=name
        self.basic_salary=basic_salary
    def display(self):
        print("ID:",self.emp_id)
        print("Name: ",self.name)
        print("salary: ",self.basic_salary)
class manager(employee):
    def __init__(self,emp_id,name,basic_salary,bonous):
        super().__init__(emp_id,name,basic_salary)
        self.bonous=bonous
    def cal_salary(self):
        total_salary=self.basic_salary+self.bonous
        print(total_salary)
m1=manager(10,"manya",10000,500)
m1.display()
m1.cal_salary()