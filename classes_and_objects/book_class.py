class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f"the book tiltled {self.title} is written by {self.author}")
b1=book("python","manya")
b2=book("unix","moulya")
b3=book("network","dhanya")
b1.display()
b2.display()
b3.display()
        