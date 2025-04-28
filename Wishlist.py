class Wishlist:
    # Creating an empty wishlist
    def __init__(self):
        self.books = []

    # Displaying your wishlist if you have a wishlist
    def displayWishList(self) -> None:
        if not self.books:
            print('Your Wishlist is empty.')
        else:
            print('----Your Wishlist-----')
            for book in self.books:
                print(f'{book.getBookPublishing()} - ${book.getPrice():.2f}')

    # Adding a book from the BookListing to the Wishlist
    def addToWishlist(self, Wishlistbook: 'BookListing') -> str:
        self.books.append(Wishlistbook)
        print(f'Book: {Wishlistbook.getBookID()} added to the wishlist.')

    # Removing a book from the Wishlist if the book is in the wishlist
    def removeBook(self, bookID: int) -> str:
        for book in self.books:
            if book.getBookID() == bookID:
                self.books.remove(book)
                print(f'Book: {bookID} was removed from the wishlist.')
                return
        print(f'Book with ID {bookID} was not found in the wishlist.')

