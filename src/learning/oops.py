import logging
from datetime import date, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,  #
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

class Library: 
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__book_collection = []
        self.__members = []
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, address):
        self.__address = address
    
    def addBook(self, book):
        self.__book_collection.append(book)
        logging.info(f"Added book: {book.getTitle()}")

    def removeBook(self, book):
        if book in self.__book_collection:
            self.__book_collection.remove(book)
            logging.info(f"Removed book: {book.getTitle()}")
        else:
            logging.error(f"{book.getTitle()} does not exist in our collection!")
    
    def showAllBooks(self):
        return self.__book_collection
    
    def showAllMembers(self):
        return self.__members  # Return the list of all members
    
    def addMember(self, member):
        self.__members.append(member)
        logging.info(f"Added member: {member.getName()}")

    @staticmethod
    def calculate_fine(book, return_date):
        if book.getDueDate() is None or return_date <= book.getDueDate():
            return 0
        
        # Calculate Extra Days Taken and add fine (15) per day
        extra_days = (return_date - book.getDueDate()).days
        fine = extra_days * 15
        return fine
    
    def __repr__(self) -> str:
        return f"Library: {self.__name}, {self.__address}, Books: {[book.getTitle() for book in self.__book_collection]}"
        
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = False
        self.__due_date = None
        
    def getTitle(self):
        return self.__title
    
    def setTitle(self, title):
        self.__title = title

    def getAuthor(self):
        return self.__author    
    
    def setAuthor(self, author):
        self.__author = author
        
    def getIsbn(self):
        return self.__isbn
    
    def setIsbn(self, isbn):
        self.__isbn = isbn
        
    def getIsBorrowed(self):
        return self.__is_borrowed
    
    def setIsBorrowed(self, is_borrowed):
        self.__is_borrowed = is_borrowed
        if self.__is_borrowed:  
            current_date = date.today() #Gets Current Date
            self.__due_date = current_date + timedelta(15) # Sets Due Date 15 days from the current day
            logging.info(f"Book {self.__title} is now borrowed. Due date set to {self.__due_date}.")
        else:
            self.__due_date = None  # Reset the due date when the book is returned
            logging.info(f"Book {self.__title} is now returned.")

    def getDueDate(self):
        return self.__due_date
        
    def __repr__(self) -> str:
        return f'Book({self.getTitle()}, {self.getAuthor()}, {self.getIsbn()}, {"Borrowed" if self.getIsBorrowed() else "Available"}, Due Date: {self.getDueDate()})'
           
class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getMemberId(self):
        return self.__member_id
    
    def setMemberId(self, member_id):
        self.__member_id = member_id
        
    def borrowBook(self, book):
        if not book.getIsBorrowed():
            book.setIsBorrowed(True)
            self.__borrowed_books.append(book)
            logging.info(f"{book.getTitle()} borrowed successfully by {self.getName()} ({self.getMemberId()})")
        else:
            logging.warning(f"{book.getTitle()} is already borrowed!")
            
    def returnBook(self, book, library):
        if book in self.__borrowed_books:
            return_date = date.today() + timedelta(20)
            fine = library.calculate_fine(book, return_date)
            book.setIsBorrowed(False)
            self.__borrowed_books.remove(book)
            logging.info(f"{book.getTitle()} returned successfully! Fine: ${fine}")
        else:
            logging.error(f"{book.getTitle()} is not borrowed by this member!")
    
    def __repr__(self) -> str:
        return f"Member Name: {self.__name}, Member ID: {self.__member_id}, Borrowed Books: {[book.getTitle() for book in self.__borrowed_books]}"

# Example usage
b1 = Book("1984", "George Orwell", "1234567890")
b2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

# Creating a member
Alice = Member("Alice", "M001")
Bob = Member("Bob", "M002")

# Creating a library
library = Library("Central Library", "123 Library St")

# Adding books and members to the library
library.addBook(b1)
library.addBook(b2)
library.addMember(Alice)
library.addMember(Bob)

# Member borrows a book
Alice.borrowBook(b1)
logging.info(f"Member details: {Alice}")

# Member returns a book
Alice.returnBook(b1, library)
logging.info(f"Member details: {Alice}")
