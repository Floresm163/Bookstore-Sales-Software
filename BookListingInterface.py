class BookListingInterface:
    def __init__(self):
        self.bookCatalog = []

    def displayBookListing(self, book: 'BookListing'):
        print("\n--- Book Listing ---")
        print(f"Title: {book.getTitle()}")
        print(f"Book ID: {book.getBookID()}")
        print(f"Publisher: {book.getPublisher()}")
        print(f"Author: {book.getAuthor()}")
        print(f"Genre: {book.getGenre()}")

    def viewBookList(self):
        if not self.bookCatalog:
            print("No books available.")
        else:
            print("\n--- Book Catalog ---")
            for book in self.bookCatalog:
                self.displayBookListing(book)

    def searchBookList(self):
        if not self.bookCatalog:
            print("No books to search.")
            return
        title = input("Enter title to search: ").strip().lower()
        found = False
        for book in self.bookCatalog:
            if title in book.getTitle().lower():
                self.displayBookListing(book)
                found = True
        if not found:
            print("Book not found.")

    def addEntry(self):
        bookTitle = input("Enter book title: ")
        bookID = int(input("Enter book ID: "))
        bookPublisher = input("Enter publisher: ")
        bookAuthor = input("Enter author: ")
        bookGenre = input("Enter genre: ")
        newBook = BookListing(bookTitle, bookID, bookPublisher, bookAuthor, bookGenre)
        self.bookCatalog.append(newBook)
        print("Book added successfully.")

    def deleteEntry(self):
        bookID = int(input("Enter Book ID to delete: "))
        for book in self.bookCatalog:
            if book.getBookID() == bookID:
                self.bookCatalog.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")

    def updateEntry(self):
        bookID = int(input("Enter Book ID to update: "))
        for book in self.bookCatalog:
            if book.getBookID() == bookID:
                book.bookTitle = input("Enter new title: ")
                book.bookPublisher = input("Enter new publisher: ")
                book.bookAuthor = input("Enter new author: ")
                book.bookGenre = input("Enter new genre: ")
                print("Book updated successfully.")
                return
        print("Book not found.")
