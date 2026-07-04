class library:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True
    def issue_book(self):
        if self.available:
            self.available=False
            print("book Issued")
    def return_book(self):
        self.available=True
        print("book returned")
    def display(self):
        print("title: ",self.title)
        print("author: ",self.author)
        print("availability: ",self.available)
title=input("enter the title of the book: ")
author=input("enter the author og the book: ")
b1=library(title,author)
b1.issue_book()
b1.display()