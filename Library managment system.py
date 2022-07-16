from pickle import FALSE


class Library:

    def __init__(self, listofbooks):
        self.books= listofbooks

    def displayAvailableBooks(self):
        print("Books which are presently available are: ")
        for books in self.books:
            print("   *"+books)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print("you have been issued  book return it withim 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("sorry the book is not available at this moment check within a week")
            return False

    def returnbook(self,bookname):
        self.book.append(bookname)
        print("thankx for returning {bookname} within 30 days ")
        

class Student:

    def requestbook(self):
        self.book = input("enter name of book you want to borrow")
        return self.book
    
    def returnbook(self):
        self.book= input("enter the book you want to return")
        return self.book

if __name__ == "__main__":
    centralLibrary =Library(["algo","django","clrs" , "python"])
    student= Student()
   # centralLibrary.displayAvailableBooks()

   
    while(True):
        wlcmmsg= '''======welcome to central library=====
                 please choose an option
                 1. listing all the book
                 2. request a book
                 3. return a book
                 4. exit lib'''

        print(wlcmmsg)

        a=int(input("enetr a choice"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowbook(student.requestbook())

        elif a==3:
            centralLibrary.returnbook(student.returnbook())

        elif a==4:
            print("thanks for using central library")
            exit()
        else:
            print("invalid choice")

        

