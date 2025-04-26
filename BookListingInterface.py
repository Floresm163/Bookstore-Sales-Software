class BookListingInterface:

    @staticmethod
    def displayBookListing(book: 'BookListing'):
        # Display the details of a BookListing object
        print("\n--- Book Listing ---")
        print(f"The book ID: {book.getBookID()}")
        print(f"The book was published by: {book.getBookPublishing()}")
        print(f"The date the book was published: {book.getPublishingDate()}")
        print(f"The price of the book: ${book.getPrice():.2f}")
