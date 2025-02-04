#this program is a project about the library management system.
#there are three key classes Book, member and library to manage.
#this is the first version of the library management system.

class Book:
    #initial declaration of the book details
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
   
    def __str__(self):
        return f"{self.title} by {self.author} (isbn:{self.isbn})"
   
class Member:
    #initial declaration of the members
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    #borrow books details
   
    def borrow_book(self, book):  #borrowed books details
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
           
        else:
            print(f"Sorry {book.title} is not available.")
   
    def return_book(self, book): #return books details
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} has not borrowed {book.title}.")
           
    def __str__(self):
        return f"{self.name}, ID: {self.member_id} has borrowed books:{[book.title for book in self.borrowed_books]}."

#create a library class
class Library:
   
    def __init__(self): #to intialize books and members
        self.books = []
        self.members = []
       
    def add_book(self, book): #add new books
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
       
    def remove_book(self, book): #remove books
        if book in self.books:
            self.books.remove(book)
            print(f" Book '{book.title}' removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")
   
    def register_member(self, member): #members registration
        self.members.append(member)
        print(f"member '{member.name}' registered successfully.")
       
    def borrow_book(self, book_title, member_id): #borrowing the book
        member = next((m for m in self.members if member_id == member_id), None)
        book = next((b for b in self.books if b.title.lower() ==book_title.lower() and b.available), None)
       
        if member and book:
            member.borrow_book(book)
        elif not member:
            print("Member not found.")
           
        else:
            print(f"{book.title} is currently available.")
           
   
    def return_book(self, book_title, member_id): #returning the book
        member =next((m for m in self.members if m.member_id ==member_id), None)
       
        if member:
            book = next((b for b in member.borrowed_books if b.title ==book_title), None)
           
            if book:
                member.return_book(book)
           
            else:
                print(f"'{book_title}' was not borrowed by {member.name}.")
               
        else:
            print("member not found.")
           
   
    def display_available_books(self):  #displaying the available books
        available_books = [book for book in self.books if book.available]
       
        if available_books:
            print("\nAvailable books")
            for book in available_books:
                print(book)
       
        else:
            print("No books available at the moment.")
           
library = Library()

book1 = Book("python programming", "John Doe", "12345")
book2 = Book("Data structure", "Alice Smith", "67890")

library.add_book(book1)
library.add_book(book2)

member1 = Member ("Alice", "M001")
member2 = Member ("Bob", "M002")

library.register_member(member1)
library.register_member(member2)

library.borrow_book("Python programming", "M001")
library.display_available_books()
library.return_book("Python programming", "M002")
library.display_available_books()