# -------------- Classes ------------------
class Book:

    def __init__(self, ID, Title, author):
        self.__id = ID
        self.__title = Title
        self.__author = author
        self.__availability = True # all the books are available by default
    
    # Getters
    def getID(self):
        return self.__id

    def getTitle(self):
        return self.__title
    
    def is_available(self):
        return self.__availability
    
    def get_author(self):
        return self.__author


    # Behaviors (Use in other classes later)
    def borrow_book(self):
        if self.__availability:
            self.__availability = False 
        else:
            print(f"The {self.__title} book is not available")
    def return_book(self):
        self.__availability = True

class Member:
    def __init__(self, MemberID, Name, library):
        self.__id = MemberID
        self.__name = Name
        self.borrowed_books = {} # Stores list of IDs and Names of borrowed books
        self.library = library # Stores object of class library to use it's methods in this class
    # Getters
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    
    # Behaviors
    def borrow_book(self, bookID):
        return self.library.borrow_book(self, bookID)

    def return_book(self, bookID):
        return self.library.return_book(self, bookID)
    
    def canBorrow(self): # Checks whether the person exceeds the quantity of allowed borrow books or not
        return True # Person is allowed to borrow maximum books by default
    
    def Display_borrowed_books(self):
        if len(self.borrowed_books) != 0:
            print(f"{self.__name} has borrowed following books from {self.library.getName()}:")
            print(f"{'ID':<3} | {'Book Name':<15} | {'Author':<15}")
            print("-" * 35)
            for i,n in self.borrowed_books.items(): # Iterate over the list and print the name of borrowed books
                print(f"{i:<3} | {n:<15} | {n.get_author():<15}")
            print("-" * 35)
        else:
            print(f"{self.__name} does not has any book of the {self.library.getName()}.")

class Student(Member): # Rule: Student can only borrow three books at a time
    def __init__(self, MemberID, Name, library):
        super().__init__(MemberID, Name, library) # Call member constructor
    
    # Getters
    def getId(self):
        return super().getId()
    def getName(self):
        return super().getName()
    
    # Behaviors
    def canBorrow(self):
        return len(self.borrowed_books) < 3 # checks whether the student already borrowed three books.                         
    def borrow_book(self, bookID):
        if self.canBorrow():
            return self.library.borrow_book(self, bookID) # Library method checks further conditions before borrowing the selected book
        else:
            print(f"{self.getName()} has borrowed three books already")

    def return_book(self, bookID):
            return self.library.return_book(self, bookID)
    
    def Display_borrowed_books(self):
        return super().Display_borrowed_books() 

class Teacher(Member): # Rule: Teacher can only borrow five books at a time
    def __init__(self, MemberID, Name, library):
        super().__init__(MemberID, Name, library) # Call member constructor
    
    # Getters
    def getId(self):
        return super().getId()
    def getName(self):
        return super().getName()
    
    # Behaviors
    def canBorrow(self):
        return len(self.borrowed_books) < 5 # checks whether the teacher already borrowed five books
            
    def borrow_book(self, bookID):
        if self.canBorrow():
            return self.library.borrow_book(self, bookID)
        else:
            print(f"{self.getName()} has borrowed five books already")

    def return_book(self, bookID):
            return self.library.return_book(self, bookID)
    
    def Display_borrowed_books(self):
        return super().Display_borrowed_books()
class Library:
    def __init__(self,name):
        self.books = {} # dictionary of books
        self.members = {} # dictionary of members
        self.__name = name
    def getName(self):
        return self.__name
    
    def addBook(self, book): # Object of book passed as argument
        self.books[book.getID()] = book
        # Dictionary of book updates by writing id as a key and book(object) as a value
        print(f"The book, {book.getTitle()} by {book.get_author()} is added in {self.__name}")
    
    def addMember(self, mem): 
        self.members[mem.getId()] = mem
        # Dictionary of members updates by writing id as a key and member(object) as a value
        print(f"{mem.getName()} has been enrolled in {self.__name}")
    
    def borrow_book(self, person, bookID): # person is the object of class member/student/teacher
        if bookID not in self.books.keys(): # Checks that if the book of given ID exist in the library or not
            print(f"The book with ID {bookID} does not exist in {self.__name} yet.")
            return
        if self.books[bookID].is_available(): # Checks that if, the book of given id is available or someone already borrowed
            self.books[bookID].borrow_book() # Runs the boorrow book method of class book.
            print(f"The book, {self.books[bookID].getTitle()} by {self.books[bookID].get_author()} is borrowed by {person.getName()}")
            person.borrowed_books[bookID] = self.books[bookID]  # append the dictionary of borrowed books of individual member, with ID as a key and book as a value
        else:
            print(f"The {self.books[bookID].getTitle()} by {self.books[bookID].get_author()} book is not available now") # self.library.books[ID].getTitle() means:
            # 'self' is an obj of library, 'books' is a dict of library, books[ID] corresponds to key of book(object) in the dictionary, 'getTitle()' is a getter of book(object)
    
    def return_book(self, person, bookID):
        if bookID not in person.borrowed_books:
            print(f"This book was not borrowed by {person.getName()}")
            return
        if bookID in self.books: # Checks that if the book of given ID exist in the library or not
            self.books[bookID].return_book() # Runs the return book method of class book.
            del person.borrowed_books[bookID] # Remove item book from borrow dictionary of a person
            print(f"The book, {self.books[bookID].getTitle()} by {self.books[bookID].get_author()} is returned by {person.getName()}")
        else:
            print(f"The book with ID {bookID} does not exist in the {self.__name} yet.")
    
    def ShowBooks(self):
        print(f"Followings books are stored in the {self.__name}\n")
        # Prints record of books in tabular format
        print(f"{'ID':<3} | {'Book Name':<15} | {'Author':<15}")
        print("-" * 35)
        for k,v in self.books.items():
            print(f"{k:<3} | {v.getTitle():<15} | {v.get_author():<15}")
        print("-" * 35)
    
    def ShowMembers(self):
        print(f"Followings members often come in {self.__name}\n")
        # Prints record of members in tabular format
        print(f"{'ID':<3} | {'Member Name':<15}")
        print("-" * 18)
        for k,v in self.members.items():
            print(f"{k:<3} | {v.getName():<15}")
        print("-" * 18)
# ----------- Function Definitions for main -------------

# These Functions take object of class Library as a parameter
def addBook(library):
    # Attributes for object of class Book
    id = int(input("Enter ID of the book:\n> "))

    if  id in library.books: # Checks whether the given ID is free or not
        print(f"The given ID is already alotted to the book named, {library.books[id].getTitle()}.")
        return
    
    title = input("Write title of the book:\n> ")
    author = input("Write author of the book:\n> ")

    # Object of class book
    book = Book(id, title, author)

    # Passing object of book to the method of class library
    library.addBook(book)


def add_Member(library):
    # Attributes for object of class Member
    print("Information about roles of a person")
    print("----------------------------------")
    print("1 - Member")
    print("2 - Student")
    print("3 - Teacher")
    print("----------------------------------")
    role = int(input("Write role of the reader:\n> "))
    id = int(input("Enter ID of the reader:\n> "))

    if  id in library.members: # Checks whether the given ID is free or not
        print(f"The given ID is already alotted to the reader named, {library.members[id].getName()}.")
        return
    
    name = input("Write name of the reader:\n> ")

    # Object of class Member/Student/Teacher
    if role == 1:
        reader = Member(id, name, library)
    elif role == 2:
        reader = Student(id, name, library)
    elif role == 3:
        reader = Teacher(id, name, library)
    else:
        print("The given role is not valid")

    # Passing object of class Member/Student/Teacher to the method of class library
    library.addMember(reader)


def borrowBook(library):
    readerID = int(input("Enter id of the reader:\n> "))
    if readerID in library.members:
        reader = library.members[readerID]  # Finds reader from the dictionary by his id
        bookID = int(input(f"Enter ID of the book, {reader.getName()} wants to borrow:\n> "))
        reader.borrow_book(bookID)  # calls method of reader's class.
    else:
        print(f"reader with ID {readerID} is not enrolled in {library.getName()}")


def return_book(library):
    readerID = int(input("Enter id of the reader:\n> "))
    if readerID in library.members:
        reader = library.members[readerID]  # Finds reader from the dictionary by his id
        bookID = int(input(f"Enter ID of the book {reader.getName()} wants to return:\n> "))
        reader.return_book(bookID)  # calls method of reader's class.
    else:
        print(f"reader with ID {readerID} is not enrolled in {library.getName()}")


def record_of_borrowed_books(library):
    readerID = int(input("Enter id of the reader:\n> "))
    if readerID in library.members:
        reader = library.members[readerID]  # Finds reader from the dictionary by his id
        return reader.Display_borrowed_books()
    else:
        print(f"reader with ID {readerID} is not enrolled in {library.getName()}")


def all_books(library):
    return library.ShowBooks()


def all_members(library):
    return library.ShowMembers()

def file_of_readers_records(library):
    with open("readers.txt", "w") as f:
        f.write(f"{'ID':<3} | {'Member Name':<15}\n")
        f.write("-" * 18 + "\n")

        for k, v in library.members.items():
            f.write(f"{k:<3} | {v.getName():<15}\n")

    print("All the records of members are stored in the file successfully.")

def file_of_books_records(library):
    with open("books.txt", "w") as f:
        f.write(f"{'ID':<3} | {'Book Name':<15} | {'Author':<15}\n")
        f.write("-" * 35 + "\n")

        for k, v in library.books.items():
            f.write(f"{k:<3} | {v.getTitle():<15} | {v.get_author():<15}\n")

    print("All the records of books are stored in the file successfully.")


# ----------- Main -------------
def main():

    Oxford_Library = Library("Oxford Library")

    def printMenu():
        print("Library management system")
        print("=========================")
        print("1 - Add Book")
        print("2 - Add Member")
        print("3 - Borrow Book")
        print("4 - Return Book")
        print("5 - Show record of borrowed book(s) of a reader")
        print("6 - Show All books in a library")
        print("7 - Show all members of a library")
        print("8 - Upload reader(s) data into readers file")
        print("9 - Upload book(s) data into books file")
        print("10 - Exit")
    while True:
        printMenu()
        choice = int(input("Choose choice:\n> "))

        if choice == 1:
            addBook(Oxford_Library)
        elif choice == 2:
            add_Member(Oxford_Library)
        elif choice == 3:
            borrowBook(Oxford_Library)
        elif choice == 4:
            return_book(Oxford_Library)
        elif choice == 5:
            record_of_borrowed_books(Oxford_Library)
        elif choice == 6:
            all_books(Oxford_Library)
        elif choice == 7:
            all_members(Oxford_Library)
        elif choice == 8:
            file_of_readers_records(Oxford_Library)
        elif choice == 9:
            file_of_books_records(Oxford_Library)
        elif choice == 10:
            print("Exiting from library management system...")
            break
        else:
            print("The entered choice is not valid")
if __name__ == "__main__":
    main()









