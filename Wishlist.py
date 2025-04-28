class Wishlist:
    def __init__(self):
        self.books = []

    def displayWishlist(self) -> None:
        if not self.books:
            print('Your Wishlist is empty.')
        else:
            print('----Your Wishlist-----')
            for book in self.books:
                print(f'{book.getTitle()} by {book.getAuthor()}')

    def displayWishlistMenu(self) -> None:
        while True:
            print("\n--- Wishlist Menu ---")
            print("1. View Wishlist")
            print("2. Add Book to Wishlist")
            print("3. Remove Book from Wishlist")
            print("4. Return to Customer Menu")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.displayWishlist()
                elif choice == 2:
                    bookTitle = input("Enter book title: ")
                    bookID = int(input("Enter book ID: "))
                    bookPublisher = input("Enter publisher: ")
                    bookAuthor = input("Enter author: ")
                    bookGenre = input("Enter genre: ")
                    newBook = BookListing(bookTitle, bookID, bookPublisher, bookAuthor, bookGenre)
                    self.addBook(newBook)
                elif choice == 3:
                    try:
                        bookID = int(input("Enter Book ID to remove: "))
                        self.removeBook(bookID)
                    except ValueError:
                        print("Invalid Book ID.")
                elif choice == 4:
                    break
                else:
                    print("Invalid Entry. Please enter 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter 1-4.")

    def addBook(self, Wishlistbook: 'BookListing') -> str:
        self.books.append(Wishlistbook)
        print(f'Book: {Wishlistbook.getTitle()} added to the wishlist.')

    def removeBook(self, bookID: int) -> str:
        for book in self.books:
            if book.getBookID() == bookID:
                self.books.remove(book)
                print(f'Book ID {bookID} was removed from the wishlist.')
                return
        print(f'Book with ID {bookID} was not found in the wishlist.')
